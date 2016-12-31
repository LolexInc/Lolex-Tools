import os, time, py_compile, shutil, sys, platform
print ("Module LolexToolsMethods is running, using modules os and time.")
try:
	import ver
except(ImportError):
	if "arm" in platform.platform() == False:
		pass
	else:
		print("Please redownload this repository to access all features.")
def version():
	print(ver.version)
def flicker():
    suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
    if suretoflash == 1:
        howlongtoflashfor = int(input("How many loops do you wish to occur?"))
        currentflashes= int(0)
    print("Here is a list of colours available:")
    print("a - Neon Green")
    print("b - Light Blue")
    print("c - Neon Red")
    print("d - Light Purple/Pink")
    print("e - Neon Yellow")
    print("f - White")
    print("1 - Dark Blue")
    print("2 - Dark Green")
    print("3 - Light Non-Neon Blue")
    print("4 - Dark Red/Brown")
    print("5 - Dark Purple")
    print("6 - Non Neon Yellow")
    print("7 - White/Light Gray")
    print("8 - Dark Gray")
    print("9 - Dark Neon Blue")
    colour = (input("Please enter your first colour with color prefixed.  "), input("Please enter your second colour, with color prefixed.  "), input("Please enter your third colour, with color prefixed.  "), input("Please enter your fourth colour, with color prefixed.  "), input("Please enter your fifth colour, with color prefixed.  "))
    while howlongtoflashfor != currentflashes:
        os.system (colour[0])
        os.system (colour[1])
        os.system (colour[2])
        os.system (colour[3])
        os.system (colour[4])
        currentflashes = currentflashes + 1
    import theme
    os.system(theme.theme)
def mode2():
    shutdown = int(input("Please enter 1 to confirm restart."))
    if shutdown == 1:
        waittime = int(input("How long, in minutes do you wish to wait."))
        time.sleep(waittime*60)
        useros = platform.system()
        if useros != "Linux":
            os.system("shutdown -r -f")
        elif "arm" in platform.platform():
            os.system("/system/bin/reboot")
        else:
            os.system("reboot")
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
def modehide(name, state):
    if state == False:
        newstate = True
    else:
        newstate = False
    try:
        os.remove("./"+name+".py")
        os.remove("./"+name+".pyc")
    except(IOError):
        pass
    with open ("./"+name+"settings.py","a") as outf: 
        outf.write("hidden = ")
        outf.write(str(newstate))
