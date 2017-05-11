#! python3
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
local = time.asctime( time.localtime(time.time()) )
print(local,"    Attempting to remove folders...")
try:
	shutil.rmtree("./sys")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./update")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./Logs")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./resources")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./main")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./ci")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./lib")
except(IOError, OSError):
	pass
try:
	shutil.rmtree("./setup")
except(IOError, OSError):
	pass
print("Removing files...")
try:
	os.remove("./start.py")
except(IOError, OSError):
	pass
try:
	os.remove("./Androidfirsttimeinit.py")
except(IOError, OSError):
	pass
try:
	os.remove("./ver.py")
except(IOError, OSError):
	pass
try:
	os.remove("./requiredpatches.py")
except(IOError, OSError):
	pass
try:
	local = time.asctime(time.localtime(time.time()))
	print(local, "    Copying files...")
	shutil.copy("/sdcard/Lolex-Tools/start.py", "./")
	shutil.copy("/sdcard/Lolex-Tools/Androidfirsttimeinit.py", "./")
	shutil.copy("/sdcard/Lolex-Tools/ver.py", "./")
	shutil.copy("/sdcard/Lolex-Tools/requiredpatches.py", "./")
	print("Copying folders...")
	shutil.copytree("/sdcard/Lolex-Tools/ci/" ,"./ci/")
	shutil.copytree("/sdcard/Lolex-Tools/setup/", "./setup/")
	shutil.copytree("/sdcard/Lolex-Tools/main/", "./main/")
	shutil.copytree("/sdcard/Lolex-Tools/resources/", "./resources/")
	shutil.copytree("/sdcard/Lolex-Tools/lib/", "./lib")
	shutil.copytree("/sdcard/Lolex-Tools/Logs", "./Logs")
	shutil.copytree("/sdcard/Lolex-Tools/sys", "./sys")
	shutil.copytree("/sdcard/Lolex-Tools/update", "./update")
except(IOError, OSError) as e:
	print(e)
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
