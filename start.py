import os, platform, shutil, sys
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
    try:
        import JTToolsOptions
        try:
            os.rename("./JTToolsOptions.py","LolexToolsOptions.py")
        except(IOError, OSError):
            try:
                os.rename("./JTToolsOptions.pyc","LolexToolsOptions.pyc")
            except(IOError, OSError):
                pass
    except(ImportError):
        pass
    import LolexToolsOptions
    if LolexToolsOptions.compiledon<8.127:
        if platform.system() == "Windows":
            if sys.version_info.minor>5:
                os.system(" py .\LolexToolsInstaller.py")
            else:
                os.system("python .\LolexToolsInstaller.py")
        else:
            os.system("python3 ./LolexToolsInstaller.py")
        exit(0)
    try:
       import ver
       if ver.version <= 8.129211346:
           with open ("./exitsettings.py","a") as f: f.write("hidden = False")
    except(IOError, ImportError):
        pass
except(ImportError, IOError, OSError):
    if platform.system() == "Windows":
        if sys.version_info.minor>5:
            os.system("py .\LolexToolsInstaller.py")
        else:
            os.system("python .\LolexToolsInstaller.py")
    else:
        os.system("python3 ./LolexToolsInstaller.py")
    exit(0)
if system == "Windows":
    print("Starting on Windows...")
    if sys.version_info.minor>5:
        os.system("py .\LolexTools.py")
    else:
        os.system("python LolexTools.py")
    exit(0)
else:
    print("Starting on Linux...")
    os.system("python3 ./LolexTools.py")
    exit(0)
