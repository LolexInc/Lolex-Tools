try:
	os.remove("./../../patches.py")
except(IOError, OSError):
	pass
with open ("./../../patches.py") as outf: outf.write('applied = "/90/9.0nann4"')
try:
	os.remove("./../madeon.py")
except(IOError, OSError):
	pass
with open ("./../../madeon.py", "a") as outf: outf.write("compiledon = 9.00101")