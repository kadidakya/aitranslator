import os
import asyncio
import subprocess
from flask import Flask, render_template, request, send_file, jsonify
import edge_tts

app = Flask(__name__)

# المجلدات المؤقتة لتخزين الفيديوهات المرفوعة والمعالجة
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# قائمة الأصوات المجانية المتاحة
VOICES = {
    'en-male': 'en-US-ChristopherNeural',
    'en-female': 'en-US-JennyNeural',
    'fr-male': 'fr-FR-HenriNeural',
    'fr-female': 'fr-FR-DeniseNeural'
}

async def generate_speech(text, voice, output_path):
    communicator = edge_tts.Communicate(text, voice)
    await communicator.save(output_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_video():
    try:
        video_file = request.files.get('video')
        script_text = request.form.get('script_text', '').strip()
        lang = request.form.get('language', 'en-male')
        
        # معلمات الفلتر اليدوي والألوان
        brightness = float(request.form.get('brightness', 1.0))
        contrast = float(request.form.get('contrast', 1.0))
        saturation = float(request.form.get('saturation', 1.0))
        sharpness = float(request.form.get('sharpness', 0.0))

        if not video_file or not script_text:
            return jsonify({'error': 'يرجى تقديم الفيديو والنص المترجم'}), 400

        # حفظ الفيديو الأصلي
        input_video_path = os.path.join(UPLOAD_FOLDER, 'input.mp4')
        video_file.save(input_video_path)

        # توليد الصوت بالذكاء الاصطناعي (Edge TTS)
        tts_audio_path = os.path.join(UPLOAD_FOLDER, 'speech.mp3')
        selected_voice = VOICES.get(lang, 'en-US-ChristopherNeural')
        asyncio.run(generate_speech(script_text, selected_voice, tts_audio_path))

        # بناء الفلاتر المرئية باستعمال FFmpeg
        vf_filters = []
        vf_filters.append(f"eq=brightness={brightness - 1.0:.2f}:contrast={contrast:.2f}:saturation={saturation:.2f}")
        
        if sharpness > 0:
            lx = int(3 + (sharpness * 4))
            ly = int(3 + (sharpness * 4))
            la = round(sharpness * 1.5, 2)
            vf_filters.append(f"unsharp={lx}:{ly}:{la}:{lx}:{ly}:0.0")

        filter_complex_str = ",".join(vf_filters)

        # دمج الصوت الجديد وتطبيق الفلاتر وحفظ الفيديو بأعلى جودة
        final_output_path = os.path.join(OUTPUT_FOLDER, 'output.mp4')
        
        ffmpeg_cmd = [
            'ffmpeg', '-y',
            '-i', input_video_path,
            '-i', tts_audio_path,
            '-vf', filter_complex_str,
            '-map', '0:v:0',
            '-map', '1:a:0',
            '-c:v', 'libx264',
            '-crf', '18',
            '-pix_fmt', 'yuv420p',
            '-c:a', 'aac',
            '-b:a', '192k',
            '-shortest',
            final_output_path
        ]

        subprocess.run(ffmpeg_cmd, check=True)

        return jsonify({'status': 'success', 'download_url': '/download'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download')
def download():
    path = os.path.join(OUTPUT_FOLDER, 'output.mp4')
    return send_file(path, as_attachment=True, download_name="dubbed_video.mp4")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

