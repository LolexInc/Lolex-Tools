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
print("CI version 1.8.0")
files = dirdisc(1, 0, "./")
print(files)
flen = len(files)
arraypos = 0
print("Compiling...")
while arraypos<flen:
	currfile = files[arraypos]
	aarraypos = 0
	py_compile.compile(currfile)
	while aarraypos < len(currfile):
		if currfile[aarraypos] == "." and currfile[aarraypos  + 1] == "." and currfile[aarraypos + 2] == "/":
			del currfile[aarraypos]
			del currfile[aarraypos + 1]
			del currfile[aarraypos + 2]
		else:
			aarraypos = aarraypos + 3
	print("Successfully compiled " + (str(currfile)))
	arraypos = arraypos + 1