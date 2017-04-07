##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
## 
## authors = Monkeyboy2805
import shutil, os, time, platform
init1 = time.time()
try:
	with open ("./isnottravisci.py","a") as outf: pass
except(IOError):
	exit(None)
try:
	local = time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove folders...") 
	shutil.rmtree("./Defaults")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./Tests")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./sys")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./update")
except(IOError, OSError):
	pass
try:
	local = time.asctime( time.localtime(time.time()) )
	print(local,"    Attempting to remove files...")
	os.remove("./LolexTools.py")
except(IOError, OSError):
	pass
try:
	os.remove("./LolexToolsInstaller.py")
except(IOError, OSError):
	pass
try:
	os.remove("./LolexToolsMethods.py")
except(IOError, OSError):
	pass
try:
	os.remove("./start.py")
except(IOError, OSError):
	pass
try:
	os.remove("./Androidfirsttimeinit.py")
except(IOError, OSError):
	pass
try:
	os.remove("./Androidautoupdate.sh")
except(IOError, OSError):
	pass
try:
	os.remove("./ver.py")
except(IOError, OSError):
	pass
try:
	local = time.asctime(time.localtime(time.time()))
	print(local, "    Copying files...")
	shutil.copy("/sdcard/Lolex-Tools/LolexTools.py","./")
	shutil.copy("/sdcard/Lolex-Tools/LolexToolsInstaller.py","./")
	shutil.copy("/sdcard/Lolex-Tools/LolexToolsMethods.py","./")
	shutil.copy("/sdcard/Lolex-Tools/start.py","./")
	shutil.copy("/sdcard/Lolex-Tools/Androidfirsttimeinit.py","./")
	shutil.copy("/sdcard/Lolex-Tools/Androidautoupdate.sh","./")
	shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
	print("Copying folders...")
	shutil.copytree("/sdcard/Lolex-Tools/Defaults","./Defaults")
	shutil.copytree("/sdcard/Lolex-Tools/Tests","./Tests")
	shutil.copytree("/sdcard/Lolex-Tools/sys","./sys")
	shutil.copytree("/sdcard/Lolex-Tools/update","./update")
except(IOError, OSError):
	print("Please ensure that all files are present in /sdcard/Lolex-Tools")
	exit(None)
try:
	shutil.copytree("/sdcard/Lolex-Tools/Logs","./Logs")
except(IOError, OSError):
	pass
init2 = time.time()
print("Took ",((init2-init1)*1000)," milliseconds to setup Android environment")
with open ("./androidinit.py","a") as outf:pass
print("Initialized... Starting...")
