import subprocess,os, platform
system = platform.system()
print("Starting...")
if "arm" in platform.platform():
    print("Starting on arm...")
    try:
        import androidinit
    except(ImportError):
        os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
        exit(None)
    
if system == "Windows":
    print("Starting on Windows...")
    os.system("python ./JTTools.py")
    exit()
else:
    print("Starting on Linux...")
    os.system("python3 ./JTTools.py")
    exit()
