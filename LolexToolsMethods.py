import os, time, py_compile, shutil, sys, platform, threading
print ("Module LolexToolsMethods is running, using modules os and time.")
try:
	import ver
except(ImportError):
	if "arm" in platform.platform() == False:
		pass
	else:
		print("Please redownload this repository to access all features.")
try:
        import menusettings, restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
        pass
def version():
	print(ver.version)
def flicker():
    suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
    if suretoflash == 1:
        howlongtoflashfor = int(input("How many loops do you wish to occur?")) 
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
    colour = ("color " + input("Please enter your first colour "), "color " + input("Please enter your second colour "), "color " + input("Please enter your third colour "), "color " + input("Please enter your fourth colour "), "color " + input("Please enter your fifth colour  "))
    flickerthread = threading.Thread(target=flickerp2, args=[colour, howlongtoflashfor])
    flickerthread.start()
def flickerp2(colour, howlongtoflashfor):
    currentflashes= int(0)
    while howlongtoflashfor != currentflashes:
        os.system (colour[0])
        time.sleep(0.2) # these delays are needed otherwise outputs mess up
        os.system (colour[1])
        time.sleep(0.2)
        os.system (colour[2])
        time.sleep(0.2)
        os.system (colour[3])
        time.sleep(0.2)
        os.system (colour[4])
        time.sleep(0.2)
        currentflashes = currentflashes + 1
    import theme
    os.system(theme.theme)
    exit()
def windowspage(page):
    if page == 0 or page == -1:
        print("1  = Settings")
        if restartsettings.hidden == False:
            print("2  = Restart")
        if logoffsettings.hidden == False:
            print("3  = Logoff")
            print("4  = Alternative logoff method")
        if hibernatesettings.hidden == False:
            print("5  = Hibernate")
    if page == 1 or page == -1:
        if shutdownsettings.hidden == False:
            print("6  = Shutdown")
            print("7  = Alternative shutdown method")
        print("8  = Colour Flicker")
        print("9  = Call CMD")
        print("10 = Call documents")
    if page == 2 or page == -1:
            print("11 = Call a Python shell")
            print("12 = Call Task Manager")
            print("13 = Create folders")
            print("14 = Remove folders")
            print("15 = Create files")
    if page == 3 or page == -1:
            print("16 = Restart this script")
            print("17 = Perform arithmetic operations")
            print("18 = Lock this script")
            print("19 = Call Remote Desktop")
            print("20 = Call Powershell")
    if page == 4 or page == -1:
            print("21 = Print SystemInfo")
            print("22 = Start Installer")
            if exitsettings.hidden == False:
                print("23 = Exit")
    if page != -1:
            print("24 = Next Page")
            print("25 = Back a Page")
            
def linuxpage(page):
    if page == 0 or page == -1:
        print("1  = Settings")
        if restartsettings.hidden == False:
            print("2  = Restart")
        if logoffsettings.hidden == False:
            print("3  = Logoff")
        if hibernatesettings.hidden == False:
            print("4  = Hibernate")
        if shutdownsettings.hidden == False:
            print("5  = Shutdown")
    if page == 1 or page == -1:
        print("6  = Call a Python Shell")
        print("7  = Create folders")
        print("8  = Remove folders")
        print("9  = Create files")
        print("10 = Restart this script")
    if page == 2 or page == -1:
        print("11 = Perform arithmetic operations")
        print("12 = Lock this script")
        print("13 = Start Installer")
        print("14 = Show Uptime and Average load")
        print("15 = Print SystemInfo")
        if exitsettings.hidden == False:
            print("16 = Exit")
    if page != -1:
        print("17 = Next Page")
        print("18 = Back a Page")
def mode2():
    shutdown = int(input("Please enter 1 to confirm restart."))
    if shutdown == 1:
        waittime = int(input("How long, in minutes do you wish to wait."))
    restartthread = threading.Thread(target = restart, args = [waittime])
    restartthread.start()
def restart(waittime):
    time.sleep(waittime*60)
    print("RESTART thread: Restarting device...")
    useros = platform.system()
    if useros != "Linux":
        os.system("shutdown -r -f")
    else:
        if "arm" in platform.platform():
            if os.system("su -c reboot") != 0:
                os.system("reboot")
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
    py_compile.compile(name+".py","./"+name+".pyc")
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
