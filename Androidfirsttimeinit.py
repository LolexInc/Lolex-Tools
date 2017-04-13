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
	shutil.rmtree("./Lolex-Tools")
except(IOError, OSError):
	pass
try:
	shutil.copytree("/sdcard/Lolex-Tools/", "./Lolex-Tools")
	with open("./start.py", "a") as outf: pass
except(IOError, OSError):
	print("Please ensure all files are present in /sdcard/Lolex-Tools")
try:
	with open ("./isnottravisci.py","a") as outf: pass
except(IOError):
	exit(None)
