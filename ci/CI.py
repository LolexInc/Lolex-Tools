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
print("CI version 1.9.0")
folders = []
files = []
root = os.listdir("./")
arraypos = 0
filesl = 0
while arraypos < len(root):
	if (".git" in root[arraypos]) == False:
		readin = True
		try:
			r = open(root[arraypos], "a")
		except(IOError, OSError):
			readin = False
		if readin == True:
			if root[arraypos].endswith(".py"): #and ".pyc" not in root[arraypos]:
				files.append("./" + root[arraypos])
		else: pass
		if readin == False:
			readin2 = True
			try:
				os.listdir(root[arraypos])
			except(IOError, OSError):
				readin2 = False
			if readin2 == True:
				folders.append("./" + root[arraypos])
	arraypos = arraypos + 1
arraypos = 0
while arraypos<len(folders):
	path = folders[arraypos] + "/"
	currsub = os.listdir(path)
	tarraypos = 0
	sublen = len(currsub)
	while tarraypos<sublen:
		if (".git" in currsub[tarraypos]) == False:
			readin3 = True
			try:
				r = open(path + currsub[tarraypos])
			except(IOError, OSError):
				readin3 = False
			if readin3 == True:
				if currsub[tarraypos].endswith(".py"):
					files.append(path + currsub[tarraypos])
			else: pass
			if readin3 == False:
				readin4 = True
				try:
					os.listdir(path + currsub[tarraypos])
				except(IOError, OSError):
					readin4 = False
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
	print("Successfully compiled " + (str(currfile)))
	arraypos = arraypos + 1