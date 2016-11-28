import subprocess,os, platform
system = platform.system()
	
if system == "Windows":
	subprocess.call("./JTTools.py",shell = True)
else:
	os.system("python3 ./JTTools.py")
