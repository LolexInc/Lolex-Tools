#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, shutil, sys, time
if sys.version_info.major != 3:
	print("Please install Python 3 to run this script.")
	time.sleep(5)
	exit(0)
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
try:
	from lib import LolexToolsMethods
except(ImportError, SyntaxError, TabError) as e:
	print(e)
	print("Missing library. Please redownload this application.")
	time.sleep(5)
	exit(0)
#if LolexToolsMethods.uos.useros == "Android":
	#try:
		#import androidinit
		#try:
			#os.remove("./ver_old.py")
		#except(IOError, OSError):
			#pass
		#os.rename("./ver.py", "ver_old.py")
		#shutil.copy("/sdcard/Lolex-Tools/ver.py", "./")
		#import ver, ver_old
		#if ver.version > ver_old.version:
			#print("Installing updates...")
			#os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
	#except(ImportError, SyntaxError, TabError):
		#os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
if LolexToolsMethods.uos.useros == "Windows":
	# TODO: MERGE THESE: IT'S EASY!
	os.system("TITLE Lolex-Tools")
	os.system("MODE 1000")
	os.system(LolexToolsMethods.pyo + " ." + os.sep + "sys" + os.sep + "bootanim.py")
	os.system(LolexToolsMethods.pyo + " ." + os.sep + "main" + os.sep + "LolexTools.py")
	exit(0)
elif LolexToolsMethods.uos.useros == "Linux" or LolexToolsMethods.uos.useros == "Android":
	sys.stdout.write("\x1b]2;Lolex-Tools\x07")
	if LolexToolsMethods.uos.useros == "Linux":
		os.system("python3 ." + ps.sep + "sys" + os.sep + "bootanim.py")
	os.system("python3 ." + os.sep + "main" + os.sep + "LolexTools.py")
	exit(0)
else:
	print("OS not supported!!!")
	time.sleep(5)
	exit(0)
