import os, py_compile
array = os.listdir("./")
for i in range(0, len(array) - 1):
	if array[i].endswith("settings.py"):
		py_compile.compile(array[i])
		os.remove(array[i])
with open("./patches.py", "a") as outf: outf.write(', "/90/9.0nann7")