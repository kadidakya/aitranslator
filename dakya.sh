#!/bin/bash

# أداة Dakya للحماية والفحص السريع
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}==================================${NC}"
echo -e "${CYAN}    مرحباً بك في سكريبت Dakya       ${NC}"
echo -e "${CYAN}    أداة الحماية والفحص المبدئي      ${NC}"
echo -e "${CYAN}==================================${NC}\n"

# 1. التحقق من تحديثات الحزم
echo -e "${GREEN}[+] جاري فحص تحديثات الحزم والنظام...${NC}"
if command -v apt &> /dev/null; then
    apt update -y && echo -e "${GREEN}-> الحزم محدثة.${NC}"
elif command -v pkg &> /dev/null; then
    pkg update -y && echo -e "${GREEN}-> الحزم محدثة.${NC}"
fi

# 2. فحص الأجهزة المتصلة بالشبكة المحلية (إذا توفرت أداة nmap)
echo -e "\n${GREEN}[+] فحص المنافذ المفتوحة والشبكة...${NC}"
if command -v nmap &> /dev/null; then
    echo "جاري فحص الجهاز المحلي (localhost):"
    nmap -F 127.0.0.1
else
    echo -e "${RED}[!] أداة nmap غير مثبتة، يمكنك تثبيتها لفحص الشبكة.${NC}"
fi

# 3. تنظيف الملفات المؤقتة لحماية الخصوصية
echo -e "\n${GREEN}[+] تنظيف الملفات المؤقتة والذاكرة المؤقتة...${NC}"
rm -rf ~/.cache/* 2>/dev/null
echo -e "${GREEN}-> تم تنظيف المخلفات بنجاح.${NC}"

echo -e "\n${CYAN}==================================${NC}"
echo -e "${CYAN}    اكتمل فحص Dakya بنجاح!        ${NC}"
echo -e "${CYAN}==================================${NC}"

#!/bin/bash

# أداة Dakya للحماية والفحص السريع
RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

clear
echo -e "${CYAN}==================================${NC}"
echo -e "${CYAN}    مرحباً بك في سكريبت Dakya       ${NC}"
echo -e "${CYAN}    أداة الحماية والفحص المبدئي      ${NC}"
echo -e "${CYAN}==================================${NC}\n"

# 1. التحقق من تحديثات الحزم
echo -e "${GREEN}[+] جاري فحص تحديثات الحزم والنظام...${NC}"
if command -v apt &> /dev/null; then
    apt update -y && echo -e "${GREEN}-> الحزم محدثة.${NC}"
elif command -v pkg &> /dev/null; then
    pkg update -y && echo -e "${GREEN}-> الحزم محدثة.${NC}"
fi

# 2. فحص المنافذ المفتوحة والشبكة
echo -e "\n${GREEN}[+] فحص المنافذ المفتوحة والشبكة...${NC}"
if command -v nmap &> /dev/null; then
    echo "جاري فحص الجهاز المحلي (localhost):"
    nmap -F 127.0.0.1
else
    echo -e "${RED}[!] أداة nmap غير مثبتة، يمكنك تثبيتها عبر: pkg install nmap${NC}"
fi

# 3. تنظيف الملفات المؤقتة لحماية الخصوصية
echo -e "\n${GREEN}[+] تنظيف الملفات المؤقتة والذاكرة المؤقتة...${NC}"
rm -rf ~/.cache/* 2>/dev/null
echo -e "${GREEN}-> تم تنظيف المخلفات بنجاح.${NC}"

# 4. دمج أداة Zphisher (فحص التثبيت أو التثبيت التلقائي)
echo -e "\n${CYAN}==================================${NC}"
echo -e "${CYAN}      إدارة أدوات إضافية (Zphisher)    ${NC}"
echo -e "${CYAN}==================================${NC}"

if [ -d "$HOME/zphisher" ]; then
    echo -e "${GREEN}[✓] أداة Zphisher مثبتة مسبقاً في جهازك.${NC}"
    read -p "هل تريد تشغيل Zphisher الآن؟ (y/n): " run_zph
    if [ "$run_zph" = "y" ] || [ "$run_zph" = "Y" ]; then
        cd "$HOME/zphisher" && bash zphisher.sh
    fi
else
    read -p "أداة Zphisher غير مثبتة. هل تريد تثبيتها الآن؟ (y/n): " install_zph
    if [ "$install_zph" = "y" ] || [ "$install_zph" = "Y" ]; then
        echo -e "${YELLOW}[+] جاري تثبيت المتطلبات و Zphisher...${NC}"
        pkg update -y && pkg install git curl php proot -y
        git clone https://github.com/htr-tech/zphisher.git "$HOME/zphisher"
        echo -e "${GREEN}[✓] تم تثبيت Zphisher بنجاح! يمكنك تشغيلها الآن.${NC}"
        read -p "هل تريد تشغيلها فوراً؟ (y/n): " run_now
        if [ "$run_now" = "y" ] || [ "$run_now" = "Y" ]; then
            cd "$HOME/zphisher" && bash zphisher.sh
        fi
    fi
fi

echo -e "\n${CYAN}==================================${NC}"
echo -e "${CYAN}    اكتمل عمل سكريبت Dakya بنجاح!   ${NC}"
echo -e "${CYAN}==================================${NC}"

# 4. دمج أداة Zphisher (فحص التثبيت أو التثبيت التلقائي)
echo -e "\n${CYAN}==================================${NC}"
echo -e "${CYAN}      إدارة أدوات إضافية (Zphisher)    ${NC}"
echo -e "${CYAN}==================================${NC}"

if [ -d "$HOME/zphisher" ]; then
    echo -e "${GREEN}[✓] أداة Zphisher مثبتة مسبقاً في جهازك.${NC}"
    read -p "هل تريد تشغيل Zphisher الآن؟ (y/n): " run_zph
    if [ "$run_zph" = "y" ] || [ "$run_zph" = "Y" ]; then
        cd "$HOME/zphisher" && bash zphisher.sh
    else
        echo -e "${YELLOW}[i] تم تخطي تشغيل Zphisher. يمكنك تشغيلها يدوياً لاحقاً بالأمر: cd ~/zphisher && bash zphisher.sh${NC}"
    fi
else
    read -p "أداة Zphisher غير مثبتة. هل تريد تثبيتها الآن؟ (y/n): " install_zph
    if [ "$install_zph" = "y" ] || [ "$install_zph" = "Y" ]; then
        echo -e "${YELLOW}[+] جاري تثبيت المتطلبات و Zphisher...${NC}"
        pkg update -y && pkg install git curl php proot -y
        git clone https://github.com/htr-tech/zphisher.git "$HOME/zphisher"
        echo -e "${GREEN}[✓] تم تثبيت Zphisher بنجاح!${NC}"
    else
        echo -e "${YELLOW}[i] تم تخطي التثبيت.${NC}"
    fi
fi

echo -e "\n${CYAN}==================================${NC}"
echo -e "${CYAN}    اكتمل عمل سكريبت Dakya بنجاح!   ${NC}"
echo -e "${CYAN}==================================${NC}"

