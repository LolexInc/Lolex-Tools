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
import py_compile
import sys
import time
a = time.time()
print("CI version 3.0.0 PRERELEASE")
sys.path.insert(0, "./ci/lib/")
import LolexToolsCIlib
del sys.path[sys.path.index("./ci/lib/")]
b = time.time()
print("Testing...")
LolexToolsCIlib.compile_files(LolexToolsCIlib.get_file_folders())
c = (str(round(time.time() - b, 0)))
c.replace("-", "")
print("Tests complete in " + c + " seconds")
