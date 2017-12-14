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
if input("Do you want to enter the experimental installer? Please enter 1 if so. (DEVELOPERS TESTING ONLY!!!") == "1":
    sys.path.insert(0, "./lib")
    import LolexToolsMethods
    os.system(LolexToolsMethods.pyo + " ./setup/exp/LolexToolsSetup.py")
