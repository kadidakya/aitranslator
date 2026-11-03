yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZNR3X1VTg/
cuting:
pkg install python-yt-dlp -y
pkg update -y && dpkg --configure -a
pkg upgrade -y
pkg install python-yt-dlp -y
yt-dlp -4 --force-ipv4 --no-check-certificate -o "$HOME/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZNR3X1VTg/
mv /data/data/com.termux/files/home/storage/downloads/*.mp4 /sdcard/Download/
termux-setup-storage
mv /data/data/com.termux/files/home/storage/downloads/*.mp4 /sdcard/Download/
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZNR3X1VTg/
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN81dRov7/
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN81f9bgk/
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVpmKq/
pip install -U yt-dlp
pip install curl-cffi
yt-dlp --impersonate chrome -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVpmKq/
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVpmKq/
pkg install python-curl-cffi -y
pkg install clang libxml2 libxslt libffi openssl -y
pip install --upgrade pip
pip install curl-cffi --no-cache-dir
/yt-dlp --list-impersonate-targets
yt-dlp --list-impersonate-targets
yt-dlp -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" "الرابط_الطويل_هنا"
yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVcK7M/
get --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVcK7M/
yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -4 --force-ipv4 --no-check-certificate -o "~/storage/downloads/%(title).50s.%(ext)s" https://vm.tiktok.com/ZN8dVcK7M/
curl -s "https://api.tiklydown.eu.org/api/download?url=https://vm.tiktok.com/ZN8dVcK7M/" | jq -r '.video.noWatermark' | xargs -I {} curl -o "~/storage/downloads/tiktok_video.mp4" "{}"
pkg install jq
curl -s "https://api.tiklydown.eu.org/api/download?url=https://vm.tiktok.com/ZN8dVcK7M/" | jq -r '.video.noWatermark' | xargs -I {} curl -o "~/storage/downloads/tiktok_video.mp4" "{}"
curl -s "https://api.tiklydown.eu.org/api/download?url=https://vm.tiktok.com/ZN8dVcK7M/" | jq -r '.video.noWatermark' | xargs -I {} curl -L -o "$HOME/storage/downloads/tiktok_$(date +%s).mp4" "{}"
cat << 'EOF' > $PREFIX/bin/get
#!/bin/bash
url="$1"
filename="$HOME/storage/downloads/tiktok_$(date +%s).mp4"

echo "جاري استخراج رابط الفيديو..."

# المحاولة الأولى عبر TikWm API
download_url=$(curl -s -X POST "https://www.tikwm.com/api/" -d "url=$url" | jq -r '.data.play')

# المحاولة الثانية عبر Tiklydown في حال فشل الأولى
if [ "$download_url" == "null" ] || [ -z "$download_url" ]; then
    download_url=$(curl -s "https://api.tiklydown.eu.org/api/download?url=$url" | jq -r '.video.noWatermark // .video.watermark')
fi

# تحميل الفيديو إذا تم إيجاد الرابط
if [ "$download_url" != "null" ] && [ -n "$download_url" ]; then
    curl -L -o "$filename" "$download_url"
    echo "تم التحميل بنجاح في مجلد Downloads!"
else
    echo "جاري المحاولة عبر yt-dlp..."
    yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -4 --force-ipv4 --no-check-certificate -o "$HOME/storage/downloads/%(title).50s.%(ext)s" "$url"
fi
EOF

chmod +x $PREFIX/bin/get
get https://vm.tiktok.com/ZN8dVcK7M/
get https://vm.tiktok.com/ZN8RM1mYT/
get Https://vm.tiktok.com/ZN8LvF2wa/
get Https://vm.tiktok.com/ZN8FdEHdT/
yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -4 --force-ipv4 --no-check-certificate -o "$HOME/storage/downloads/%(title).50s.%(ext)s" "https://www.facebook.com/share/v/1cQiT4AupU/"
cat << 'EOF' > $PREFIX/bin/get
#!/bin/bash
url="$1"
filename="$HOME/storage/downloads/video_$(date +%s).mp4"

echo "جاري استخراج الفيديو..."

if [[ "$url" == *"facebook.com"* || "$url" == *"fb.watch"* ]]; then
    # استخراج روابط فيسبوك عبر API مباشر
    download_url=$(curl -s -X POST "https://sssfbf.com/api/convert" -H "Content-Type: application/x-www-form-urlencoded" -d "url=$url" | jq -r '.url[0].url // empty')
    
    if [ -z "$download_url" ]; then
        download_url=$(curl -s "https://api.v2.fdown.net/parse?url=$url" | jq -r '.hd // .sd // empty')
    fi
else
    # استخراج روابط تيك توك عبر API مباشر
    download_url=$(curl -s -X POST "https://www.tikwm.com/api/" -d "url=$url" | jq -r '.data.play')
fi

# تنزيل الملف إذا تم جلب الرابط
if [ -n "$download_url" ] && [ "$download_url" != "null" ]; then
    curl -L -o "$filename" "$download_url"
    echo "تم التحميل بنجاح في مجلد Downloads!"
else
    echo "جاري المحاولة عبر yt-dlp..."
    yt-dlp --user-agent "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" -4 --force-ipv4 --no-check-certificate -o "$HOME/storage/downloads/%(title).50s.%(ext)s" "$url"
fi
EOF

chmod +x $PREFIX/bin/get
get "https://www.facebook.com/share/v/1cQiT4AupU/"
createdb msf_db && msfconsole
ls
pg_ctl -D ~/../usr/var/lib/postgresql start && createdb msf_db && unset TERM && msfconsole
msfconsole
pkg update && pkg upgrade -y && termux-setup-storage
pg_ctl -D ~/../usr/var/lib/postgresql start || (initdb ~/../usr/var/lib/postgresql && pg_ctl -D ~/../usr/var/lib/postgresql start) && createdb msf_db 2>/dev/null; unset TERM && msfconsole
ln -sf /data/data/com.termux/files/usr/opt/metasploit-framework/msfconsole $PREFIX/bin/msfconsole && msfconsole
cd /data/data/com.termux/files/usr/opt/metasploit-framework && bundle install && msfconsole
pkg install sqlite libsqlite clang make -y && gem install sqlite3 -v 2.9.4 -- --with-sqlite3-include=$PREFIX/include --with-sqlite3-lib=$PREFIX/lib && bundle install
gem install mini_portile2 && bundle config build.sqlite3 --with-sqlite3-include=$PREFIX/include --with-sqlite3-lib=$PREFIX/lib && bundle install
bundle config set build.sqlite3 --use-system-libraries && gem install sqlite3 -v 2.9.4 -- --use-system-libraries --with-sqlite3-dir=$PREFIX
NO_KEYRING=1 MAKE="make -j$(nproc)" NOKOGIRI_USE_SYSTEM_LIBRARIES=1 bundle config set --local force_ruby_platform true
gem install sqlite3 -v 2.9.4 -- --with-cflags="-I$PREFIX/include" --with-ldflags="-L$PREFIX/lib" --use-system-libraries
bundle install && msfconsole
pkg update && pkg install python
pip install google-genai
pkg update
pkg install python-cryptography python-cffi rust
pkg install rust clang make libffi openssl
pip install google-genai
pkg install python-cryptography
pip install --no-build-isolation google-genai
pkg install python-maturin
pip install google-genai==0.3.0
export ANDROID_API_LEVEL=24
pip install google-genai==0.3.0
nano bot.py
python bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
export LANG=en_US.UTF-8
echo "export LANG=en_US.UTF-8" >> ~/.bashrc
source ~/.bashrc
python bot.py
nano bot.py
python bot.py
ls
cd thc-hydra
hydra -l 
pkg update && pkg install unstable-repo
pkg install x11-repo
pkg install aircrack-ng
pkg install root-repo
pkg install aircrack-ng
termux-change-repo
pkg install aircrack-ng
pkg install reaver
pkg install bully
pkg namp
pkg install nmap
nmap --help
nmap -T4 -F 192.168.1.1
nmap -T4 -A 192.168.1.1
curl http://192.168.1.1
pkg update && pkg upgrade -y
pip install google-generativeai
pkg update && pkg upgrade -y
apt-get clean
apt-get autoclean
pkg update --fix-missing
apt --fix-broken install
apt list --upgradable
pkg upgrade -y
pip install pyTelegramBotAPI google-genai
nano my_ai_bot.py
python my_ai_bot.py
cd ~
nano my_ai_bot.py
python my_ai_bot.py
cat << 'EOF' > my_ai_bot.py
import telebot
from google import genai

TELEGRAM_TOKEN = "8514063282:AAEVMmZrIj8xgmH_kGb-eAjC-xXLySPPax4"
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = genai.Client(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda message: True)
def smart_reply(message):
    user_text = message.text
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=user_text,
        )
        reply_text = response.text
    except Exception as e:
        reply_text = "عذراً، حدث خطأ أثناء الاتصال بالذكاء الاصطناعي."

    bot.reply_to(message, reply_text)

print("البوت الخاص بك يعمل الآن ومربوط بي...")
bot.infinity_polling()
EOF

python my_ai_bot.py
ls
cd zphisher
bash zphisher.sh
bash phisher.sh
bash zphisher.sh
ls
cd dakya.sh
cd zphisher
nano zphisher.sh
bash zphisher.sh
/mybots
python bot.py
nano bot.py
python bot.py
rm bot.py
nano bot.py
python bot.py
ls
get https://www.facebook.com/share/r/1CAhvAGRuj/
get https://www.facebook.com/share/r/1QRot3xAvD/
get https://www.facebook.com/share/r/1EwziVnrPv/
get https://www.facebook.com/share/r/1KmVrv8T7z/
nano bot.py
python bot.py
pip install cgi-tools
pkg in sqlmap
pkg update && pkg install python git -y
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python sqlmap.py --help
sqlmap -u "https://www.tiktok.com/@lefebvrejeanjaques?_r=1&_t=ZN-9AdckQm9q5O/item.php?id=1"
cd ~/sqlmap
ln -s ~/sqlmap/sqlmap.py $PREFIX/bin/sqlmap
sqlmap --help
sqlmap -u "http://testphp.vulnweb.com/artists.php?artist=1" --batch
sqlmap -u "http://testphp.tiktok.com/artists.php?artist=1" --batch
sqlmap -u "http://tiktok. php/artists.php?artist=1" --batch
sqlmap -u "https://www.tiktok.com/@lefebvrejeanjaques?_r=1&_t=ZN-9AddeMtjVig" --batch
pkg update && pkg install nmap -y
ls
cd data
cd sqlmapapi.py
sqlmapapi.py
cd ..
cd
ls
cd sqlmap
cd
nano sqlmap.py
nano sqlmap.conf
nano sqlmap.py
cd sqlmap
nano sqlmap.py
cd
pkg update && pkg install john -y
chmod +x caido-cli
./caido-cli
curl -s https://api.github.com/repos/caido/caido/releases/latest | grep "browser_download_url.*cli-linux-aarch64.tar.gz" | cut -d '"' -f 4 | wget -qi -
tar -xzf caido-cli-linux-aarch64*.tar.gz
wget https://releases.caido.io/cli/caido-cli-v0.40.0-linux-aarch64.tar.gz
ping -c 3 google.com
curl -s https://api.github.com/repos/caido/caido/releases/latest | grep "browser_download_url.*cli-linux-aarch64.tar.gz" | cut -d '"' -f 4 | wget -qi -
tar -xzf caido-cli-linux-aarch64*.tar.gz
chmod +x caido-cli
./caido-cli
curl -L -o caido.tar.gz "https://github.com/caido/caido/releases/latest/download/caido-cli-linux-aarch64.tar.gz"
curl -s https://api.github.com/repos/caido/caido/releases/latest | grep "browser_download_url.*cli-linux-aarch64.tar.gz" | cut -d '"' -f 4 | xargs curl -L -o caido.tar.gz
wget -O caido.tar.gz https://github.com/caido/caido/releases/download/v0.42.0/caido-cli-v0.42.0-linux-aarch64.tar.gz
pkg in caido
curl -L -o caido.tar.gz "https://github.com/caido/caido/releases/download/v0.42.0/caido-cli-v0.42.0-linux-aarch64.tar.gz"
tar -xzf caido.tar.gz
pkg install ffuf -y
rm -f caido.tar.gz caido-cli
curl -L -o caido.tar.gz "https://github.com/caido/caido/releases/download/v0.43.0/caido-cli-v0.43.0-linux-aarch64.tar.gz"
ls -lh caido.tar.gz
tar -xzf caido.tar.gz
chmod +x caido-cli
./caido-cli
rm -f caido.tar.gz
python3 -c '
import urllib.request
import json
url = "https://api.github.com/repos/caido/caido/releases/latest"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        for asset in data.get("assets", []):
            if "cli-linux-aarch64.tar.gz" in asset["name"]:
                print("Downloading:", asset["browser_download_url"])
                urllib.request.urlretrieve(asset["browser_download_url"], "caido.tar.gz")
                break
except Exception as e:
    print("Error:", e)
'
ls -lh caido.tar.gz
python3 -c 'import urllib.request, json; u="https://api.github.com/repos/caido/caido/releases/latest"; d=json.loads(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent":"Mozilla"})).read().decode()); next(urllib.request.urlretrieve(a["browser_download_url"], "caido.tar.gz") for a in d["assets"] if "cli-linux-aarch64.tar.gz" in a["name"])'
ls -lh caido.tar.gz
curl -L -o caido.tar.gz "https://releases.caido.io/releases/v0.43.0/caido-cli-v0.43.0-linux-aarch64.tar.gz"
curl -L -o caido.tar.gz "https://github.com/caido/caido/releases/download/v0.43.0/caido-cli-v0.43.0-linux-aarch64.tar.gz"
ls -lh caido.tar.gz
tar -xzf caido.tar.gz
chmod +x caido-cli
./caido-cli
ls
ls -lh caido.tar.gz
tar -xzf caido.tar.gz
chmod +x caido-cli
./caido-cli
rm -f caido.tar.gz
wget https://github.com/caido/caido/releases/download/v0.40.0/caido-cli-v0.40.0-linux-aarch64.tar.gz -O caido.tar.gz
tar -xzf caido.tar.gz
chmod +x caido-cli
./caido-cli
curl -L -o caido.tar.gz "https://releases.caido.io/cli/caido-cli-linux-aarch64.tar.gz"
ls
cd caido.tar.gz
tar -xzf caido.tar.gz
chmod +x caido-cli
./caido-cli
rm -f caido.tar.gz caido-cli && curl -L -o caido.tar.gz "https://releases.caido.io/cli/caido-cli-linux-aarch64.tar.gz" && ls -lh caido.tar.gz && tar -xzf caido.tar.gz && chmod +x caido-cli && ./caido-cli
pkg install golang -y
~/go/bin/nuclei -u https://example.com
pkg install perl git -y
cd nikto/program
perl nikto.pl -h https://example.com
sqlmap -u "https://example.com/page.php?id=1" --batch
ls
cd sqlmap
sqlmap -u "http://testphp.vulnweb.com/artists.php?artist=1" --batch
sqlmap -u "http://testphp.vulnweb.com/artists.php?artist=1" --random-agent --batch
tar -xzf caido.tar.gz
pkg in get
cd 
pkg in hot
pkg in namp
pkg in namep
pkg in nampe
pkg in bs
pkg in +c
pkg in java
pkg install openjdk-17 -y
java -version
nano TechnicApp.java
javac TechnicApp.java
java TechnicApp
nano index.html
python -m http.server 8080
nano index.html
python -m http.server 8080
pkg install nano
pip install --upgrade pip
pip install httpx python-telegram-bot
python bot.py
pip install yt-dlp
nano bot.py
python bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
nano bot.py
python bot.py
d
nano make_english_video.py
python make_english_video.py
pip install gTTS pillow
python make_english_video.py
termux-setup-storage
cd ~/storage
ls
cp english_output.mp4 ~/storage/shared/Download/
cp ~/english_output.mp4 ~/storage/shared/Download/
cd ~
cp english_output.mp4 storage/shared/Download/
pip install pyttsx3
nano make_man_video.py
python make_man_video.py
pkg install espeak -y
pkg install espeak-ng -y
python make_man_video.py
nano make_man_video.py
python make_man_video.py
cp man_output.mp4 storage/shared/Download/
python bot.py
nano 
nano hafid daraji
python bot.py
pip install google-genai
nano hafid
python bot.py
nano hafid
python bot.py
nano daraji
python bot.py
nano hafid
python bot.py
killall python
python bot.py
killall -9 python
nano hafid
python bot.py
pyhton bot.py
python bot.py
pkg update && pkg upgrade
pkg install proot-distro
proot-distro install kali
proot-distro login kali
pkg update && pkg upgrade -y
pkg install proot-distro -y
proot-distro install kali
pkg update && pkg install wget curl git -y
curl -LO https://offs.ec/net-hunter-sh && chmod +x net-hunter-sh && ./net-hunter-sh
nethunter
rm -f net-hunter-sh
curl -LO https://raw.githubusercontent.com/Hax4us/Nethunter-In-Termux/master/nethunterinstallstorage
proot-distro install ubuntu
proot-distro login ubuntu
python3 mysite.py
proot-distro login ubuntu
mkdir -p templates
cd ~
mkdir -p templates
nano templates/index.html
python3 mysite.py
find . -name "mysite.py"
nano mysite.py
python3 mysite.py
Address already in use
Port 5000 is in use by another program.
pkg update && pkg upgrade
mkdir msf-video-editor
cd msf-video-editor
git init
git branch -M main
touch index.html style.sc script.js README.md
nano index.html
mv style.sc style.css
nano style.css
nano script.js
nano README.md
git remote add origin https://github.com/kadidakya/msf-video-editor.git
git branch -M main
git push -u origin main
git add .
git commit -m "Initial commit for msf video editor"
git push -u origin main
cd msf-video-editor
python -m http.server 8080
pkg in john
cd
ls
ls la
cd sudo
cd -h
bash: cd: -h: invalid option-
nano requirements.txt
dubbing-app/
├── app.py
├── requirements.txt
├── .gitignore
└── templates/
# إنشاء مجلد المشروع والدخول إليه
mkdir dubbing-app
cd dubbing-app
# إنشاء مجلد القوالب الداخلية
mkdir templates
nano requirements.txt
nano .gitignore
nano templates/index.html
nano app.py
videoai/
├── app.py
├── requirements.txt
├── .gitignore
└── templates/
pip install flask edge-tts moviepy
python app.py
pip install flask opencv-python numpy
