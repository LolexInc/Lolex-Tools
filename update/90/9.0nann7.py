import os, py_compile
array = os.listdir("./")
for i in range(0, len(array) - 1):
	if array[i].endswith("settings.py"):
		py_compile.compile(array[i])
		os.remove(array[i])
try:
	os.remove("./patches.py")
except(IOError, OSError):
	pass
with open("./patches.py", "a") as outf: outf.write('\napplied = "90/9.0nann4", "/90/9.0nann7"')
print("Finished updating to 9.0nann7")