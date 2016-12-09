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
        import ver, ver_old
        if ver.version>ver_old.version:
        	print("Installing updates...")
        	os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
    except(ImportError):
        os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
try:
    import JTToolsOptions
    if JTToolsOptions.compiledon<8.127:
        if platform.system() == "Windows":
            os.system("python .\JTToolsInstaller.py")
        else:
            os.system("python3 ./JTToolsInstaller.py")
    try:
       import ver
       if ver.version <= 8.129211346:
           with open ("./exitsettings.py","a") as f: f.write("hidden = False")
    except(IOError, ImportError):
        pass
except(ImportError):
    if platform.system() == "Windows":
        os.system("python .\JTToolsInstaller.py")
    else:
        os.system("python3 ./JTToolsInstaller.py")
if system == "Windows":
    print("Starting on Windows...")
    os.system("python .\JTTools.py")
    exit(None)
else:
    print("Starting on Linux...")
    os.system("python3 ./JTTools.py")
    exit(None)
