import logging
import os
import yt_dlp
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "8514063282:AAEVMmZrIj8xgmH_kGb-eAjC-xXLySPPax4"

def download_video(url):
    ydl_opts = {
        'outtmpl': 'video.mp4',
        # اختيار أفضل جودة بحجم معقول
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    return 'video.mp4'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    chat_id = update.message.chat_id

    if text and text.startswith("http"):
        await context.bot.send_message(chat_id=chat_id, text="⏳ جاري تحميل الفيديو ورفعه، يرجى الانتظار قليلاً...")
        try:
            video_file = download_video(text)
            
            # زيادة مهلة الرفع إلى 600 ثانية (10 دقائق) لتفادي خطأ Timed out
            with open(video_file, 'rb') as vf:
                await context.bot.send_video(
                    chat_id=chat_id, 
                    video=vf, 
                    read_timeout=600, 
                    write_timeout=600, 
                    connect_timeout=600,
                    pool_timeout=600
                )
            
            if os.path.exists(video_file):
                os.remove(video_file)
        except Exception as e:
            await context.bot.send_message(chat_id=chat_id, text=f"❌ حدث خطأ أثناء التحميل: {str(e)}")
            if os.path.exists('video.mp4'):
                os.remove('video.mp4')
    else:
        response_text = f"أهلاً بك! أرسل لي رابط فيديو وسأقوم بتحميله لك فوراً."
        await context.bot.send_message(chat_id=chat_id, text=response_text)

def main():
    # زيادة مهلة الاتصال العامة للطلب
    application = ApplicationBuilder().token(TOKEN).read_timeout(600).write_timeout(600).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

    print("البوت المحدث يعمل الآن...")
    application.run_polling()

if __name__ == '__main__':
    main()

