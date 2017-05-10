#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import sys
syslen = len(sys.path)
sys.path.append("./")
import os, platform, LolexToolsMethods
try:
	import verifonboot, LolexToolsOptions
except(ImportError):
	system = platform.system()
	if system == "Windows":
		if platform.system() == "Windows":
			if sys.version_info.minor>5:
				os.system("py .\Lolex-Tools.py")
			else:
				os.system("python .\LolexTools.py")
		else:
			os.system("python3 ./LolexTools.py")
	elif system == "Linux":
		os.system("python3 ./LolexToolsInstaller.py")
	exit(0)
try:
    os.remove("./verifonboot.py")
except(IOError, OSError):
    pass
try:
    os.remove("./verifonboot.pyc")
except(IOError, OSError):
    pass
with open ("./verifonboot.py","a") as outf:
    if LolexToolsOptions.onepintotal>1:
        outf.write("oneswappins = True\nruntimeone = ")
        outf.write(str(verifonboot.runtimeone))
    else:
        outf.write("oneswappins = False\nruntimeone = 0")
    if LolexToolsOptions.onewordtotal>1:
        outf.write("\noneswapwords = True\nwordtimeone = ")
        outf.write(str(verifonboot.wordtimeone))
    else:
        outf.write("\noneswapwords = False\nwordtimeone = 0")
    if LolexToolsOptions.twopintotal>1:
        outf.write("\ntwoswappins = True\nruntimetwo = ")
        outf.write(str(verifonboot.runtimetwo))
    else:
        outf.write("\ntwoswappins = False\nruntimetwo = 0")
    if LolexToolsOptions.twowordtotal>1:
        outf.write("\ntwoswapwords = True\nwordtimetwo = ")
        outf.write(str(verifonboot.wordtimetwo))
    else:
        outf.write("\ntwoswapwords = False\nwordtimetwo = 0")
if LolexToolsOptions.compiler == True:
    LolexToolsMethods.compiler("verifonboot")
print("Finished updating to 9.0nann2...")
try:
    os.remove("./madeon.py")
except(IOError, OSError):
    pass
with open("./madeon.py", "a") as outf: outf.write("compiledon = 9.00001");
print("Finished updating to 9.0nann2")