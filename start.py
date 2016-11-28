import subprocess,os, platform
system = platform.system()
if "armv7" in platform.platform():
	try:
		import androidlolextoolsinit
	except(ImportError):
		print("If ALL files are not present in /sdcard/Lolex-Tools this will fail...")
		os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
	
if system == "Windows":
	subprocess.call("./JTTools.py",shell = True)
else:
	os.system("python3 ./JTTools.py")
