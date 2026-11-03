import os, random, sqlite3, smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from flask import Flask, render_template_string, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'dakya_secure_admin_key'

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_email@gmail.com"       # بريدك الذي سترسل منه
EMAIL_APP_PASSWORD = "abcd fghe ijkl mnop" # كلمة مرور التطبيق من جوجل

# إعداد قاعدة البيانات المحلية للمالك
def init_db():
    conn = sqlite3.connect('admin.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS admin (email TEXT, password TEXT)''')
    conn.commit()
    conn.close()

init_db()
stored_otp = {}

HOME_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>متجري</title></head>
<body style="font-family:sans-serif; text-align:center; padding:50px; background:#f8f9fa;">
    <h1>🛍️ مرحباً بك في متجري الإلكتروني</h1>
    <div style="margin-top:20px;">
        <a href="/register" style="background:#28a745; color:white; padding:10px 20px; text-decoration:none; border-radius:5px; margin-left:10px;">إنشاء حساب المالك</a>
        <a href="/login" style="background:#007bff; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">دخول المالك</a>
    </div>
</body>
</html>
'''

REGISTER_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>إنشاء حساب المالك</title>
<style>
    body { font-family: sans-serif; background: #f8f9fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .box { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 320px; text-align: center; }
    input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
    .btn { background: #28a745; color: white; border: none; padding: 10px; width: 100%; border-radius: 6px; cursor: pointer; }
</style>
</head>
<body>
    <div class="box">
        <h2>📝 تسجيل حساب المالك</h2>
        {% if error %}<p style="color:red; font-size:0.9em;">{{ error }}</p>{% endif %}
        <form method="post">
            <input type="email" name="email" placeholder="البريد الإلكتروني" required>
            <input type="password" name="password" placeholder="كلمة المرور" required>
            <button type="submit" class="btn">حفظ وتسجيل</button>
        </form>
        <br><a href="/" style="color: #666; font-size: 0.9em;">الرئيسية</a>
    </div>
</body>
</html>
'''

LOGIN_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>تسجيل الدخول</title>
<style>
    body { font-family: sans-serif; background: #f8f9fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .box { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 320px; text-align: center; }
    input { width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 6px; box-sizing: border-box; }
    .btn { background: #007bff; color: white; border: none; padding: 10px; width: 100%; border-radius: 6px; cursor: pointer; }
</style>
</head>
<body>
    <div class="box">
        <h2>🔐 دخول مالك المتجر</h2>
        {% if error %}<p style="color:red; font-size:0.9em;">{{ error }}</p>{% endif %}
        <form method="post">
            <input type="email" name="email" placeholder="بريدك الإلكتروني المسجل" required>
            <input type="password" name="password" placeholder="كلمة المرور" required>
            <button type="submit" class="btn">إرسال رمز التحقق</button>
        </form>
        <br><a href="/" style="color: #666; font-size: 0.9em;">الرئيسية</a>
    </div>
</body>
</html>
'''

OTP_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>التحقق</title>
<style>
    body { font-family: sans-serif; background: #f8f9fa; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
    .box { background: white; padding: 30px; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.1); width: 320px; text-align: center; }
    input { width: 100%; padding: 10px; margin: 15px 0; border: 1px solid #ccc; border-radius: 6px; text-align: center; font-size: 1.2em; letter-spacing: 5px; box-sizing: border-box; }
    .btn { background: #28a745; color: white; border: none; padding: 10px; width: 100%; border-radius: 6px; cursor: pointer; }
</style>
</head>
<body>
    <div class="box">
        <h2>📩 أدخل رمز التحقق</h2>
        {% if error %}<p style="color:red; font-size:0.9em;">{{ error }}</p>{% endif %}
        <form method="post">
            <input type="text" name="otp" placeholder="123456" maxlength="6" required>
            <button type="submit" class="btn">تحقق ودخول</button>
        </form>
    </div>
</body>
</html>
'''

DASHBOARD_TEMPLATE = '''
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head><meta charset="UTF-8"><title>لوحة التحكم</title></head>
<body style="font-family:sans-serif; text-align:center; padding:50px;">
    <h1 style="color:green;">🟢 أهلاً بك يا صاحب المتجر في لوحة التحكم!</h1>
    <p><a href="/logout" style="background:red; color:white; padding:10px 20px; text-decoration:none; border-radius:5px;">تسجيل خروج</a></p>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HOME_TEMPLATE)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    conn = sqlite3.connect('admin.db')
    c = conn.cursor()
    c.execute("SELECT * FROM admin")
    existing_admin = c.fetchone()
    
    if request.method == 'POST':
        if existing_admin:
            error = "تم تسجيل حساب مسبقاً! لا يمكن إنشاء حساب آخر."
        else:
            email = request.form.get('email')
            password = generate_password_hash(request.form.get('password'))
            c.execute("INSERT INTO admin VALUES (?, ?)", (email, password))
            conn.commit()
            conn.close()
            return redirect(url_for('login'))
            
    conn.close()
    return render_template_string(REGISTER_TEMPLATE, error=error)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        conn = sqlite3.connect('admin.db')
        c = conn.cursor()
        c.execute("SELECT password FROM admin WHERE email = ?", (email,))
        row = c.fetchone()
        conn.close()
        
        if row and check_password_hash(row[0], password):
            otp = str(random.randint(100000, 999999))
            stored_otp['code'] = otp
            stored_otp['email'] = email
            try:
                msg = MIMEMultipart()
                msg['From'] = SENDER_EMAIL
                msg['To'] = email
                msg['Subject'] = "رمز التحقق لدخول المتجر"
                msg.attach(MIMEText(f"رمز التحقق الخاص بك هو: {otp}", 'plain'))
                server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
                server.starttls()
                server.login(SENDER_EMAIL, EMAIL_APP_PASSWORD)
                server.sendmail(SENDER_EMAIL, email, msg.as_string())
                server.quit()
                return redirect(url_for('verify_otp'))
            except Exception as e:
                error = f"خطأ في إرسال البريد: {e}"
        else:
            error = "البريد أو كلمة المرور غير صحيحة!"
    return render_template_string(LOGIN_TEMPLATE, error=error)

@app.route('/verify-otp', methods=['GET', 'POST'])
def verify_otp():
    error = None
    if request.method == 'POST':
        if request.form.get('otp') == stored_otp.get('code'):
            session['logged_in'] = True
            return redirect(url_for('dashboard'))
        else:
            error = "رمز التحقق غير صحيح!"
    return render_template_string(OTP_TEMPLATE, error=error)

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template_string(DASHBOARD_TEMPLATE)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
