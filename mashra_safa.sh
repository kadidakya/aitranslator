#!/bin/bash
clear

# طباعة الشعار الفني البارز (ASCII Art) بلون أخضر هكر مميز
echo -e "\033[1;32m"
echo "####################################################"
echo "##                                                ##"
echo "##  88b    db    d88  .d8888b.  8888888888  88    ##"
echo "##  88Y.  d88b  .88  d8P  Y88b 88          88    ##"
echo "##  88 Y88P  Y88P 88  88    88d 88800888    88    ##"
echo "##  88  P    Y88  88  88    888 88          88    ##"
echo "##  88        P   88  \`Y8888P'  8888888888  88    ##"
echo "##                                                ##"
echo "#################### Mashra'a ####################"
echo -e "\033[0m"

# رسالة الترحيب والحالة
echo -e "\033[1;36m[=] Mashra'a Safa Script initialized successfully\033[0m"
echo ""
echo -e "\033[1;33m[+] Select an option from the menu below:\033[0m"
echo -e "\033[1;32m[+] 1) \033[0mShow Current Directory   \033[1;32m# View path\033[0m"
echo -e "\033[1;32m[+] 2) \033[0mShow Storage Status      \033[1;32m# Check disk\033[0m"
echo -e "\033[1;32m[+] 3) \033[0mExit                     \033[1;32m# Quit script\033[0m"
echo ""
read -p "Select option: " choice

case $choice in
    1)
        echo -e "\n\033[1;32mCurrent path:\033[0m"
        pwd
        ;;
    2)
        echo -e "\n\033[1;32mStorage info:\033[0m"
        df -h /data/data/com.termux/files/home
        ;;
    3)
        echo -e "\n\033[1;31mExiting...\033[0m"
        exit 0
        ;;
    *)
        echo -e "\n\033[1;31mInvalid option selected.\033[0m"
        ;;
esac
echo ""
