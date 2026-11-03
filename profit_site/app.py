from flask import Flask, render_template, request, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import sqlite3
import uuid
import re
import os
import random

app = Flask(__name__)
app.secret_key = 'ai_chatgpt_secure_key_9988!'

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

email_verification_codes = {}

limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="memory://"
)

def clean_input(text):
    if not text:
        return text
    forbidden_patterns = [r"<script.*?>.*?</script>", r"--", r";", r"\'", r"\""]
    for pattern in forbidden_patterns:
        if re.search(pattern, text, re.IGNORECASE):
            return None
    return text.strip()

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT,
            user_id TEXT UNIQUE,
            balance REAL DEFAULT 0.0,
            referred_by TEXT,
            avatar TEXT DEFAULT 'default.png',
            gender TEXT DEFAULT 'ذكر'
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS withdrawals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            method TEXT,
            account_info TEXT,
            status TEXT DEFAULT 'معلق'
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = None
    step = '1'
    email = ''
    
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'send_code':
            email = clean_input(request.form.get('email'))
            if not email or '@' not in email:
                message = "الرجاء إدخال بريد إلكتروني صحيح."
                step = '1'
            else:
                code = str(random.randint(100000, 999999))
                email_verification_codes[email] = code
                print(f"\n[رمز التحقق] للبريد {email} هو: {code}\n")
                step = '2'
                
        elif action == 'verify_and_register':
            email = clean_input(request.form.get('email'))
            username = clean_input(request.form.get('username'))
            password = request.form.get('password')
            entered_code = clean_input(request.form.get('code'))
            ref_by = clean_input(request.args.get('ref'))
            step = '2'

            if not email or email_verification_codes.get(email) != entered_code:
                message = "رمز التحقق غير صحيح أو انتهت صلاحيته."
            elif not username or not password:
                message = "الرجاء ملء جميع الحقول المطلوبة."
            else:
                hashed_password = generate_password_hash(password, method='scrypt')
                user_id = str(uuid.uuid4())[:8]

                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                try:
                    cursor.execute("INSERT INTO users (username, email, password, user_id, referred_by) VALUES (?, ?, ?, ?, ?)",
                                   (username, email, hashed_password, user_id, ref_by))
                    if ref_by:
                        cursor.execute("UPDATE users SET balance = balance + 1.0 WHERE user_id = ?", (ref_by,))
                    conn.commit()
                    conn.close()
                    email_verification_codes.pop(email, None)
                    print(f"\n[نجاح] تم تسجیل المستخدم: {username} بنجاح!\n")
                    return redirect(url_for('login'))
                except sqlite3.IntegrityError:
                    message = "اسم المستخدم أو البريد الإلكتروني مستخدم مسبقاً."
                    conn.close()

    return render_template('register.html', message=message, step=step, email=email)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = None
    
    # طباعة كل المستخدمين الموجودين في قاعدة البيانات في شاشة Termux لمساعدتك
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username, email FROM users")
    all_users = cursor.fetchall()
    conn.close()
    print(f"\n[قائمة الحسابات المسجلة في القاعدة]: {all_users}\n")

    if request.method == 'POST':
        username = clean_input(request.form.get('username'))
        password = request.form.get('password')

        if not username or not password:
            message = "الرجاء ملء كافة الحقول."
        else:
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT user_id, password, username, email FROM users WHERE username = ? OR email = ?", (username, username))
            user = cursor.fetchone()
            conn.close()

            if user and check_password_hash(user[1], password):
                session['user_id'] = user[0]
                session['username'] = user[2]
                return redirect(url_for('referral'))
            else:
                message = "اسم المستخدم (أو البريد) أو كلمة المرور غير صحيحة."

    return render_template('login.html', message=message)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/referral', methods=['GET', 'POST'])
def referral():
    if 'user_id' not in session:
        return redirect(url_for('login'))
        
    user_id = session['user_id']
    username = session.get('username')
    referral_link = f"{request.host_url}register?ref={user_id}"
    
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    success_message = None
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        if form_type == 'profile':
            gender = clean_input(request.form.get('gender'))
            file = request.files.get('avatar')
            if file and file.filename != '':
                filename = secure_filename(f"{user_id}_{file.filename}")
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                cursor.execute("UPDATE users SET gender = ?, avatar = ? WHERE user_id = ?", (gender, filename, user_id))
            else:
                cursor.execute("UPDATE users SET gender = ? WHERE user_id = ?", (gender, user_id))
            conn.commit()
            success_message = "تم تحديث الملف الشخصي بنجاح!"
        elif form_type == 'withdraw':
            method = clean_input(request.form.get('withdrawal_method'))
            account_info = clean_input(request.form.get('account_info'))
            if method and account_info:
                cursor.execute("INSERT INTO withdrawals (user_id, method, account_info) VALUES (?, ?, ?)", 
                               (user_id, method, account_info))
                conn.commit()
                success_message = f"تم تقديم طلب السحب بنجاح عبر ({method})!"

    cursor.execute("SELECT balance, avatar, gender FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    balance = user_data[0] if user_data else 0.0
    avatar = user_data[1] if user_data and user_data[1] else 'default.png'
    gender = user_data[2] if user_data and user_data[2] else 'ذكر'

    cursor.execute("SELECT username FROM users WHERE referred_by = ?", (user_id,))
    referred_friends = [row[0] for row in cursor.fetchall()]

    conn.close()
    
    return render_template('referral.html', 
                           referral_link=referral_link, 
                           username=username,
                           balance=balance,
                           avatar=avatar,
                           gender=gender,
                           referred_friends=referred_friends,
                           message=success_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

