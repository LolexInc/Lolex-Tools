import os, platform, shutil, sys, time
a = time.time()
system = platform.system()

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
        exit()
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
    exit()
if system == "Windows":
    print("Starting on Windows...")
    os.system("TITLE Lolex-Tools")
    if sys.version_info.minor>5:
        os.system("py .\sys/bootanim.py")
        print("Starting...")
        b = time.time()
        local = time.asctime(time.localtime(time.time()))
        with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
            outf.write(local)
            outf.write("     Took ")
            outf.write((str(b-a)))
            outf.write("seconds to initilaize on Windows Python >3.5\n")
        time.sleep(3)
        os.system("py .\LolexTools.py")
    else:
        sys.stdout.write("\x1b]2;Lolex-Tools\x07")
        os.system("python .\sys/bootanim.py")
        print("Starting...")
        b = time.time()
        local = time.asctime(time.localtime(time.time()))
        with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
            outf.write(local)
            outf.write("     Took ")
            outf.write((str(b-a)))
            outf.write("seconds to initilaize on Windows Python < 3.6.\n")
        time.sleep(3)
        os.system("python LolexTools.py")
    exit(None)
else:
    print("Starting on Linux...")
    os.system("python3 ./sys/bootanim.py")
    print("Starting...")
    b = time.time()
    local = time.asctime(time.localtime(time.time()))
    with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
            outf.write(local)
            outf.write("     Took ")
            outf.write((str(b-a)))
            soutf.write("seconds to initilaize on Linux Python 3.\n")
    time.sleep(3)
    os.system("python3 ./LolexTools.py")
    exit(None)
