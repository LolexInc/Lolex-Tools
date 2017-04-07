##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import py_compile, shutil, os
def compiler(name):
	with open (name + ".py","a") as outf:
		pass
	py_compile.compile(name + ".py")
	shutil.copy("./__pycache__/"+name+".cpython-35.pyc","./")
	os.rename("./"+name+".cpython-35.pyc","./"+name+".pyc")
while True:
	names = input("...")
	compiler(names)
