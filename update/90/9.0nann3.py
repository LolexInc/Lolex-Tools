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
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
syslen = len(sys.path)
sys.path.append("./")
import os, LolexToolsMethods, verifonboot, LolexToolsOptions
try:
    os.remove("./verifonboot.py")
except(IOError, OSError):
    pass
try:
    os.remove("./verifonboot.pyc")
except(IOError, OSError):
    pass
with open ("./verifonboot.py","a") as outf:
    outf.write("compiledon = 9.00001002")
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
print("Finished updating to 9.0nann3...")
try:
    os.remove("./madeon.py")
except(IOError, OSError):
    pass
with open("./madeon.py", "a") as outf: outf.write("compiledon = 9.0001");
del sys.path[syslen]
print("Finished updating to 9.0nann3")