#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, py_compile, sys
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
sys.path.append("./")
import LolexToolsOptions
array = os.listdir("./")
if LolexToolsOptions.compiler == True:
	for i in range(0, len(array) - 1):
		if array[i].endswith("settings.py"):
			py_compile.compile(array[i])
			os.remove(array[i])
try:
	os.remove("./patches.py")
except(IOError, OSError):
	pass
with open("./patches.py", "a") as outf: outf.write('\napplied = "/90/9.0nann4", "/90/9.0nann7"')
print("Finished updating to 9.0nann7")
