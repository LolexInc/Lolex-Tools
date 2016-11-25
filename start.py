import subprocess,os, platform
system = platform.system()
try:
	import runningsys
	if runningsys.system == "Android":
		os.system("python Androidstart.py")
if system == "Windows":
	subprocess.call("./JTTools.py",shell = True)
else:
	os.system("python3 ./JTTools.py")
