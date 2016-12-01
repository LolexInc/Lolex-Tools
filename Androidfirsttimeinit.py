import shutil, os, time
init1 = time.time()
try:
	with open ("./isnottravisci.py","a") as outf: pass
except():
	exit(None)
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove folders...") 
	a = time.time()
	shutil.rmtree("./Defaults")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Defaults")
except(IOError):
	pass
try:
	a = time.time()
	shutil.rmtree("./Tests")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Tests.")
except(IOError):
	pass
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove files...")
	a = time.time()
	os.remove("./JTTools.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove JTTools.py.")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./JTToolsInstaller.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove JTToolsInstaller.py")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./JTToolsMethods.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove JTToolsMethods.py")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./start.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove start.py")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./Androidfirsttimeinit.py")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Androidfirsttimeinit.py")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./busybox-armeabi")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove busybox-armeabi")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./busybox-x86")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove busybox-x86")

except(IOError):
	pass
try:
	a = time.time()
	os.remove("./Androidupdate.sh")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to remove Androidupdate.sh")
except(IOError):
	pass
try:
	a = time.time()
	os.remove("./ver.py")
	b = time.time()
	print("Took ",((b-a)*1000),"milliseconds to remove ver.py")
except(IOError):
	pass
try:
	local =time.asctime( time.localtime(time.time()) )
	print(local, "    Copying files and folders...")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/JTTools.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy JTTools.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/JTToolsInstaller.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy JTToolsInstaller.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/JTToolsMethods.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy JTToolsMethods.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/start.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy start.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/Androidfirsttimeinit.py","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Androidfirsttimeinit.py")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/Androidupdate.sh","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Androidupdate.sh")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/busybox-armeabi","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy busybox-armeabi")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/busybox-x86","./")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy busybox-x86")
	a = time.time()
	shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
	b = time.time()
	print("Took",((b-a)*1000),"milliseconds to copy ver.py")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/Defaults","./Defaults")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Defaults")
	a = time.time()
	shutil.copytree("/sdcard/Lolex-Tools/Tests","./Tests")
	b = time.time()
	print("Took ",((b-a)*1000)," milliseconds to copy Tests.")
except(IOError, OSError):
	print("Please ensure that all files are present in /sdcard/Lolex-Tools")
	exit(None)
init2 = time.time()
print("Took ",((init2-init1)*1000),"milliseconds to setup Android environment")
local =time.asctime( time.localtime(time.time()) )
print(local,"    Running start.py")
with open ("./androidinit.py","a") as outf:pass

