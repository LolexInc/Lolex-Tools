#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os
from lib import LolexToolsMethods
if os.path.exists("./update/90/9.0alpha0patch1.py") and (os.path.isdir("./update/90/9.0alpha0patch1.py")) == False:
	pass
else:
	LolexToolsMethods.addplugins(True)
