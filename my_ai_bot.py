import telebot

TELEGRAM_TOKEN = "8514063282:AAEVMmZrIj8xgmH_kGb-eAjC-xXLySPPax4"
bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(func=lambda message: True)
def auto_reply(message):
    user_text = message.text.lower()
    
    if "مرحبا" in user_text or "السلام" in user_text:
        reply_text = "وعليكم السلام ورحمة الله وبركاته! أهلاً بك في بوت RedotPay الرسمي 🤖\nكيف يمكنني مساعدتك اليوم؟"
    elif "كيف احصل" in user_text or "طلب بطاقة" in user_text:
        reply_text = "للحصول على بطاقة RedotPay:\n1. قم بتحميل التطبيق وสร้าง حساب.\n2. قم بتوثيق الحساب (KYC).\n3. اطلب البطاقة الافتراضية أو البلاستيكية من داخل التطبيق."
    elif "كيف اثبت" in user_text or "تثبيت" in user_text:
        reply_text = "يمكنك تثبيت تطبيق RedotPay مباشرة من متجر جوجل بلاي (Google Play) أو آبل ستور (App Store)."
    elif "شحن" in user_text or "رصيد" in user_text:
        reply_text = "يمكنك شحن حسابك في RedotPay عبر العملات المشفرة (مثل USDT) أو عبر القنوات المتاحة داخل التطبيق."
    elif "سعر" in user_text or "رسوم" in user_text:
        reply_text = "تختلف رسوم إصدار البطاقة والاستخدام حسب نوع البطاقة (افتراضية أو بلاستيكية)، يمكنك التحقق منها مباشرة من واجهة الأسعار داخل تطبيق RedotPay."
    else:
        reply_text = f"أهلاً بك! لقد وصلتني رسالتك: '{message.text}'\nيمكنك السؤال عن: (طريقة الحصول على البطاقة، الشحن، أو التثبيت)."

    bot.reply_to(message, reply_text)

print("البوت المطور يعمل الآن بكافة الإجابات...")
bot.infinity_polling()
