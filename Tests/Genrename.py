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
