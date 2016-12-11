echo "Please be aware that this will NOT work if all files are not present in /sdcard/Lolex-Tools"
cd /sdcard/Lolex-Tools
echo "Installing/updating git..."
apt install git
git pull
echo "Please restart your terminal or type cd <PATH> to go back to the default path. Type your path in place of <PATH>."
exit
