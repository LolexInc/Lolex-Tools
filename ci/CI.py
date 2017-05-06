#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, py_compile
print("CI version 1.7.2")
folders = []
files = []
root = os.listdir("./../")
arraypos = 0
filesl = 0
while arraypos < len(root):
	if (".git" in root[arraypos]) == False:
		if "." in root[arraypos]:
			length = len(root[arraypos])
			p = root[arraypos][length - 2]
			y = root[arraypos][length - 1]
			dot = root[arraypos][length - 3]
			if p == "p" and y == "y" and dot == ".":
				files.append("./../" + root[arraypos])
		else:
			folders.append("./../" + root[arraypos])
	arraypos = arraypos + 1
arraypos = 0
print(folders)
while arraypos<len(folders):
	path = folders[arraypos] + "/"
	currsub = os.listdir(path)
	tarraypos = 0
	sublen = len(currsub)
	while tarraypos<sublen:
		if (".git" in currsub[tarraypos]) == False:
			if "." in currsub[tarraypos]:
				clen = len(currsub[tarraypos])
				p = currsub[tarraypos][clen - 2]
				y = currsub[tarraypos][clen - 1]
				dot = currsub[tarraypos][clen - 3]
				if p == "p" and y == "y" and dot == ".":
					files.append(path + currsub[tarraypos])
			else:
				folders.append(path + currsub[tarraypos])
		tarraypos = tarraypos + 1
	arraypos = arraypos + 1
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