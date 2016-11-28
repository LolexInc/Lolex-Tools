import os, time, py_compile, shutil, sys, platform
print ("Module JTToolsMethods is running, using modules os and time.")
def flicker():
 suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
 if suretoflash == 1:
    howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
    currentflashes= int(0)                       
    while howlongtoflashfor != currentflashes:
     os.system ("color 4a")
     os.system ("color f9")
     currentflashes = currentflashes+1
def mode1():
    shutdown = int(input("Please enter 1 to confirm shutdown."))
    if shutdown == 1:
        waittime = int(input("How long, in minutes do you wish to wait."))
        time.sleep(waittime*60)
        useros = platform.system()
        if useros != "Linux":
            os.system("shutdown -r -f")
        else:
            os.system('reboot')
def logo():
    print("This function has been deprecated.")
def exitnow():
    print("This function has been deprecated.")

def compiler(name):
    try:
        os.remove("./"+name+".pyc")
    except(IOError):
        pass
    py_compile.compile(name+".py")
    if sys.version_info.minor == 7:
        nextone = (".cpython-37.pyc")
    elif sys.version_info.minor == 6:
        nextone = (".cpython-36.pyc")
    elif sys.version_info.minor == 5:
        nextone = (".cpython-35.pyc")
    elif sys.version_info.minor == 4:
        nextone = (".cpython-34.pyc")
    elif sys.version_info.minor == 3:
        nextone = (".cpython-33.pyc")
    elif sys.version_info.minor == 2:
        nextone = (".cpython-32.pyc")
    elif sys.version_info.minor == 1:
        nextone = (".cpython-31.pyc")
    else:
        nextone = (".cpython-30.pyc")
    shutil.copy("./__pycache__/"+name+nextone,"./")
    os.rename("./"+name+nextone,"./"+name+".pyc")
    os.remove("./"+name+".py")
