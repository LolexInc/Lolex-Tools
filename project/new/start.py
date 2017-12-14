#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, sys, time
sys.path.insert(0, "./project/old/lib")
try:
    import LolexToolsMethods
except(ImportError):
    print("ERROR!")
    time.sleep(5)
    exit(0)
if LolexToolsMethods.uos.useros != "Android" and LolexToolsMethods.uos.useros != "Linux" and LolexToolsMethods.uos.useros != "Windows":
    print("OS not supported. Currently supported OSs are Linux(including Android) and Windows(newer than Windows ME at minimum, for higher than Python 3.5 you need at least Windows Vista.")
os.system(LolexToolsMethods.pyo + " ./project/new/main/_main_.py")
time.sleep(5)
