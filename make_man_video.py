import os
from PIL import Image

# 1. النص الإنجليزي المراد تحويله
text = (
    "Welcome to the TikTok Creator Rewards Program. "
    "To qualify, you need at least 10,000 followers and 100,000 views in the last thirty days. "
    "Make sure your videos are longer than one minute, and focus on original content!"
)

print("1. جاري توليد الصوت الرجالي باستخدام espeak...")
# استخدام أمر espeak مباشرة لتوليد ملف صوتي بصوت رجالي واضح
os.system(f'espeak -v en "{text}" -w man_audio.wav')

print("2. جاري إنشاء خلفية الفيديو...")
width, height = 1080, 1920
image = Image.new("RGB", (width, height), color=(10, 10, 20))
image.save("man_bg.png")

print("3. جاري دمج الصوت مع الخلفية عبر FFmpeg...")
cmd = (
    "ffmpeg -y -loop 1 -i man_bg.png -i man_audio.wav "
    "-c:v libx264 -tune stillimage -c:a aac -b:a 192k "
    "-pix_fmt yuv420p -shortest man_output.mp4"
)
os.system(cmd)

print("✅ تم إنشاء الفيديو بصوت رجل بنجاح: man_output.mp4")

