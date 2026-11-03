from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# مجلد حفظ الصور المرفوعة
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# تأكد من وجود مجلد الصور والقوالب
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs('templates', exist_ok=True)

# قائمة مؤقتة لتخزين المقالات
articles = []

@app.route('/')
def home():
    return render_template('index.html', articles=articles)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        image = request.files.get('image')
        
        image_url = ''
        if image and image.filename != '':
            image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
            image.save(image_path)
            image_url = f'/{image_path}'
            
        if title and content:
            articles.insert(0, {'title': title, 'content': content, 'image': image_url})
            
        return redirect(url_for('home'))
        
    return '''
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <title>لوحة التحكم - إضافة مقال</title>
        <style>
            body { font-family: Tahoma, sans-serif; background: #121212; color: #fff; padding: 20px; text-align: right; }
            .form-container { max-width: 500px; margin: 0 auto; background: #1e1e1e; padding: 20px; border-radius: 8px; border: 1px solid #333; }
            input, textarea { width: 100%; padding: 10px; margin: 10px 0; background: #2a2a2a; border: 1px solid #444; color: #fff; border-radius: 5px; box-sizing: border-box; }
            button { background: #e50914; color: #fff; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%; }
            a { color: #ff4d4d; display: inline-block; margin-top: 15px; text-decoration: none; }
        </style>
    </head>
    <body>
        <div class="form-container">
            <h2>لوحة التحكم - إضافة مقال جديد</h2>
            <form method="POST" enctype="multipart/form-data">
                <label>عنوان المقال:</label>
                <input type="text" name="title" required>
                
                <label>محتوى المقال:</label>
                <textarea name="content" rows="5" required></textarea>
                
                <label>صورة المقال:</label>
                <input type="file" name="image" accept="image/*">
                
                <button type="submit">نشر المقال</button>
            </form>
            <a href="/">العودة إلى الموقع الرئيسي</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

