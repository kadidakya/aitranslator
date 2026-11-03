import os
from gtts import gTTS
from PIL import Image

# 1. النص الإنجليزي المراد تحويله إلى فيديو
english_text = """
Welcome to the TikTok Creator Rewards Program.
To qualify, you need at least 10,000 followers and 100,000 views in the last thirty days.
Make sure your videos are longer than one minute, and focus on original, high-quality content!
"""

print("1. Converting English text to speech...")
# تغيير اللغة إلى الإنجليزية (en)
tts = gTTS(text=english_text, lang='en')
tts.save("english_audio.mp3")

print("2. Creating video background...")
# مقاس الفيديو العمودي لتيك توك (1080x1920)
width, height = 1080, 1920
image = Image.new("RGB", (width, height), color=(20, 20, 35))
image.save("english_bg.png")

print("3. Merging audio and background using FFmpeg...")
# دمج الصوت الإنجليزي مع الخلفية لإنتاج الفيديو النهائي
cmd = (
    "ffmpeg -y -loop 1 -i english_bg.png -i english_audio.mp3 "
    "-c:v libx264 -tune stillimage -c:a aac -b:a 192k "
    "-pix_fmt yuv420p -shortest english_output.mp4"
)
os.system(cmd)

print("✅ English video created successfully: english_output.mp4")

