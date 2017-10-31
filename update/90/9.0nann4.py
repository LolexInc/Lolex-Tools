#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, sys
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
try:
	os.remove("./patches.py")
except(IOError, OSError):
	pass
try:
	os.remove("./madeon.py")
except(IOError, OSError):
	pass
with open ("./madeon.py", "a") as outf: outf.write("compiledon = 9.00101")
print("Finished updating to 9.0nann4")
