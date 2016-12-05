import os, platform, shutil
system = platform.system()
print("Starting...")
if "arm" in platform.platform():
    try:
        import androidinit
        try:
        	os.remove("./ver_old.py")
        except(IOError, OSError):
        	pass
        os.rename("./ver.py","ver_old.py")
        shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
        import ver_old, ver
        if ver.version>ver_old.version:
        	print("Installing updates...")
        	os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
    except(ImportError):
        os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
if system == "Windows":
    print("Starting on Windows...")
    os.system("python .\JTTools.py")
    exit(None)
else:
    print("Starting on Linux...")
    os.system("python3 ./JTTools.py")
    exit(None)
