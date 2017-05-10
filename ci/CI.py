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
sys.path.append("./lib")
from LolexToolsMethods import dirdisc
print("CI version 1.8.0.1")
files = dirdisc(1, 0, "./lolexorg/lolex-tools")
flen = len(files)
arraypos = 0
print("Compiling...")
while arraypos<flen:
	currfile = files[arraypos]
	y = len(currfile) - 1
	p = len(currfile) - 2
	dot = len(currfile) - 3
	if y == "y" and p == "p" and dot == ".":
		print("Successfully compiled " + (str(currfile)))
		py_compile.compile(currfile)
	arraypos = arraypos + 1