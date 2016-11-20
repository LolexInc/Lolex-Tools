import shutil, os, time
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to copy isnottravisci.py...")
	shutil.copy("/sdcard/Lolex-Tools/isnottravisci.py","./")
except(IOError):
	print("Please create isnottravisci.py in /sdcard/Lolex-Tools. Ensure all files are present in /sdcard/Lolex-Tools. Please restart this script after this.")
	exit(None)
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove folders...")
	shutil.rmtree("./Defaults")
	shutil.rmtree("./Tests")
except(IOError):
	pass
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove files...")
	os.remove("./JTTools.py")
	os.remove("./JTToolsInstaller.py")
	os.remove("./JTToolsMethods.py")
	os.remove("./start.py")
	os.remove("./Androidfirsttimeinit.py")
	os.remove("./busybox-armeabi")
	os.remove("./busybox-x86")
except(IOError):
	pass

try:
	local =time.asctime( time.localtime(time.time()) )
	print(local, "    Copying files and folders...")
	shutil.copy("/sdcard/Lolex-Tools/JTTools.py","./")
	shutil.copy("/sdcard/Lolex-Tools/JTToolsInstaller.py","./")
	shutil.copy("/sdcard/Lolex-Tools/JTToolsMethods.py","./")
	shutil.copy("/sdcard/Lolex-Tools/start.py","./")
	shutil.copy("/sdcard/Lolex-Tools/Androidfirsttimeinit.py","./")
	shutil.copy("/sdcard/Lolex-Tools/busybox-armeabi","./")
	shutil.copy("/sdcard/Lolex-Tools/busybox-x86","./")
	shutil.copytree("/sdcard/Lolex-Tools/Defaults","./Defaults")
	shutil.copytree("/sdcard/Lolex-Tools/Tests","./Tests")
except(IOError):
	print("Please ensure that all files are present in /sdcard/Lolex-Tools")
	exit(None)
local =time.asctime( time.localtime(time.time()) )
print(local,"    Running start.py")
os.system("python ./start.py")
	
