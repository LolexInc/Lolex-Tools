import os, time, py_compile, shutil, sys
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
def logo():
    print("This function has been deprecated.")
def exitnow():
    closing = 5
    while closing> 0.05:
        print("Closing in", round (closing, +3),"seconds.")
        time.sleep(0.05)
        closing = closing -0.05
    exit(None)
def importtree():
    try:
        import isnottravisci
    except(ImportError):
        print("Running as Travis CI...\nIf you are human please create isnottravisci.py to continue.")
        time.sleep(10)
        exit()
    try:
        import JTToolsOptions
    except(ImportError):
        print("Starting installer due to missing options file...")
        subprocess.call("JTToolsInstaller.py", shell = True)
        time.sleep(10)
        exit()
    try:
        import theme
    except(ImportError):
        pass
    try:
        import verifonboot
    except(ImportError):
        print("Starting installer due to missing data file...")
        subprocess.call("JTToolsInstaller.py", shell = True)
    try:
        import startplugins
    except(ImportError, ValueError, SyntaxError, TypeError, OSError, NameError):
        print("Starting installer due to missing data file...")
        sys.path.insert(0,"./System")
        subprocess.call("JTToolsInstaller.py", shell = True)
def compiler(name):
    try:
        os.remove("./"+name+".pyc")
    except(IOError):
        pass
    py_compile.compile(name+".py")
    if sys.version_info[1] == 7:
        next = (".cpython-37.pyc")
    elif sys.version_info[1] == 6:
        next = (".cpython-36.pyc")
    elif sys.version_info[1] == 5:
        next = (".cpython-35.pyc")
    elif sys.version_info[1] == 4:
        next = (".cpython-34.pyc")
    elif sys.version_info[1] == 3:
        next = (".cpython-33.pyc")
    elif sys.version_info[1] == 2:
        next = (".cpython-32.pyc")
    elif sys.version_info[1] == 1:
        next = (".cpython-31.pyc")
    else:
        next = (".cpython-30.pyc")
    shutil.copy("./__pycache__/"+name+next,"./")
    os.rename("./"+name+next,"./"+name+".pyc")