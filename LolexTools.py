#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
import sys, time, subprocess, os, shutil, py_compile, platform, io, zipfile
try:
    import isnottravisci
except(ImportError):
    print("Please create isnottravisci.py to continue.")
    time.sleep(5)
    exit(None)
system = platform.system()
if system == "Windows":
    if sys.version_info.major != 3:
        print("Only Python 3 is currently supported. Please install Python 3.")
        time.sleep(3)
try:
    import LolexToolsMethods
except(ImportError):
    print("Missing library. Please redownload this application.")
    exit(None)
try:
    import verifonboot, LolexToolsOptions, runningsys, startplugins, theme, menusettings, restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
    system = platform.system()
    if system == "Windows":
        subprocess.Popen(".\LolexToolsInstaller.py", shell = True)
    else:
        os.system("python3 ./LolexToolsInstaller.py")
    exit(None)
try:
    import madeon
    LolexToolsOptions.compiledon = madeon.compiledon
except(ImportError):
    pass
if LolexToolsOptions.compiledon<9.00001:
    if LolexToolsOptions.compiledon<8.3:
        shutil.copy("./update/8.3release.py","./")
        if system == "Windows":
            if sys.version_info.minor>5:
                os.system ("py ./8.3release.py")
            else:
                os.system("python ./8.3release.py")
        else:
            os.system ("python3 ./8.3release.py")
        os.remove("./8.3release.py")
    if LolexToolsOptions.compiledon<9.0:
        shutil.copy("./update/9.0n1.py","./")
        if system == "Windows":
            if sys.version_info.minor>5:
                os.system ("py ./9.0n1.py")
            else:
                os.system("python ./9.0n1.py")
        else:
            os.system ("python3 ./9.0n1.py")
        os.remove("./9.0n1.py")
    shutil.copy("./update/9.0nann1.py","./")
    if system == "Windows":
        if sys.version_info.minor>5:
            os.system ("py ./9.0nann2.py")
        else:
            os.system("python ./9.0nann2.py")
    else:
        os.system ("python3 ./9.0nann2.py")
    os.remove("./9.0nann2.py")
    print("Restarting to finish updating...")
    if system == "Windows":
        if sys.version_info.minor>5:
          os.system("py .\start.py")
        else:
           os.system("python .\start.py")
    else:
        os.system("python3 ./start.py")
    exit(None)
if system == "Windows":
    os.system(theme.theme)
    os.system("mode 1000")
    os.system("title Lolex-Tools")
print("Welcome to Lolex-Tools version 9.0exp 10:24 GMT+0.0 17/1/17")
try:
    os.system(theme.theme)
    oneswappins = verifonboot.oneswappins
    twoswappins = verifonboot.twoswappins
    runtimeone = verifonboot.runtimeone
    runtimetwo = verifonboot.runtimetwo
    oneswapwords = verifonboot.oneswapwords
    twoswapwords = verifonboot.twoswapwords
    wordtimeone = verifonboot.wordtimeone
    wordtimetwo = verifonboot.wordtimetwo
    oneuseword = LolexToolsOptions.oneuseword
    twouseword = LolexToolsOptions.twouseword
    if LolexToolsOptions.useusername == True:
        usernameenter = input("Please enter your username.")
        while usernameenter != LolexToolsOptions.username1 and usernameenter != LolexToolsOptions.username2:
            usernameenter = input("Please enter a valid username.")
    elif LolexToolsOptions.useusername == False:
        usernameenter = LolexToolsOptions.username1
    if LolexToolsOptions.username1 == usernameenter:
        if runtimeone == LolexToolsOptions.onepintotal:
            runtimeone = 1
        else:
            runtimeone = runtimeone + 1
        if LolexToolsOptions.onepintotal != 0:
            try:
                os.remove("./onepinner.py")
            except(IOError, OSError):
                pass
            with open ("./onepinner.py","a") as outf:
                outf.write("import LolexToolsOptions\npin = LolexToolsOptions.onepin")
                outf.write(str(runtimeone))
            import onepinner
            codeenter = int(input("Please enter your current PIN."))
            tries = 1
            if codeenter != onepinner.pin:
                while codeenter != onepinner.pin:
                    if tries == 5:
                        print("You got your PIN wrong 5 times.")
                        time.sleep(LolexToolsOptions.onewait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
        if verifonboot.oneswapwords == True:
            if LolexToolsOptions.onewordtotal == wordtimeone:
                wordtimeone = 1
            else:
                wordtimeone = wordtimeone + 1
            if LolexToolsOptions.onewordtotal != 0:
                try:
                    os.remove("./oneworder.py")
                except(IOError, OSError):
                	pass
                with open("./oneworder.py","a") as outf:
                    outf.write("import LolexToolsOptions\nword = LolexToolsOptions.oneword")
                    outf.write(str(wordtimeone))
                wordenter = input("Please enter your current password.")
                tries = 1
                while wordenter != oneworder.word:
                    if tries == 5:
                        print("You got your password wrong 5 times.")
                        time.sleep(LolexToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
    elif LolexToolsOptions.username2 == usernameenter:
        if runtimetwo == LolexToolsOptions.twopintotal:
            runtimetwo = 1
        else:
            runtimetwo = runtimetwo + 1
        if LolexToolsOptions.twopintotal != 0:
            try:
                os.remove("./twopinner.py")
            except(IOError, OSError):
                pass
            with open ("./twopinner.py","a") as outf:
                outf.write("import LolexToolsOptions\npin = LolexToolsOptions.twopin")
                outf.write(str(runtimetwo))
            import twopinner
            codeenter = int(input("Please enter your current PIN."))
            tries = 1
            if codeenter != twopinner.pin:
                while codeenter != twopinner.pin:
                    if tries == 5:
                        print("You got your PIN wrong 5 times.")
                        time.sleep(LolexToolsOptions.twowait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
        if verifonboot.twoswapwords == True:
            if LolexToolsOptions.twowordtotal == wordtimetwo:
                wordtimetwo = 1
            else:
                wordtimetwo = wordtimetwo + 1
            if LolexToolsOptions.twowordtotal != 0:
                try:
                	os.remove("./twoworder.py")
                except(IOError, OSError):
                    pass
                with open ("./twoworder.py","a") as outf:
                    outf.write("import LolexToolsOptions\nword = LolexToolsOptions.twoword")
                    outf.write(str(wordtimetwo))
                import twoworder
                wordenter = input("Please enter your current password.")
                tries = 1
                while wordenter != twoworder.word:
                    if tries == 5:
                        print("You got your password wrong 5 times.")
                        time.sleep(LolexToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
# This probably isn't the way to go, so I will rewrite it
# Doesn't allow for reauth on reenter while loop
# Auto generating files will probably come
# if runtimeone == 1:
#   pinneeded = LolexToolsOptions.onepin1
# if runtimeone == 1000: #Highly doubtful
#   pinneeded == ___.onepin1000
# etc etc
    if (verifonboot.runtimeone != runtimeone) or (verifonboot.runtimetwo != runtimetwo) or (verifonboot.oneswappins != oneswappins) or (verifonboot.twoswappins != twoswappins) or (verifonboot.wordtimeone != wordtimeone) or (wordtimetwo != verifonboot.wordtimetwo) or (oneswapwords != verifonboot.oneswapwords) or (twoswapwords != verifonboot.twoswapwords):
        try:
            os.remove("./verifonboot.py")
        except(IOError):
            pass
        try:
            os.remove("./verifonboot.pyc")
        except(IOError):
                print("verifonboot.pyc was not found.")
        with open ("./verifonboot.py","a") as outf:
            outf.write("oneswappins = ")
            outf.write(str(oneswappins))
            outf.write("\ntwoswappins = ")
            outf.write(str(twoswappins))
            outf.write("\nruntimeone = ")
            outf.write(str(runtimeone))
            outf.write("\nruntimetwo = ")
            outf.write(str(runtimetwo))
            outf.write("\nwordtimeone = ")
            outf.write(str(wordtimeone))
            outf.write("\nwordtimetwo = ")
            outf.write(str(wordtimetwo))
            outf.write("\noneswapwords = ")
            outf.write(str(oneswapwords))
            outf.write("\ntwoswapwords = ")
            outf.write(str(twoswapwords))
        if LolexToolsOptions.compiler == True:
            LolexToolsMethods.compiler("verifonboot")
    useros = platform.system()
    layout = menusettings.layout
    if layout == 0:
        page = -1
    else:
        page = 0
    while True:
        if useros == "Windows":
            LolexToolsMethods.windowspage(page, menusettings.layout)
        elif useros == "Linux":
            LolexToolsMethods.linuxpage(page, menusettings.layout)
        modewanted = int(input("Please enter the number of the mode that you want."))
        if useros == "Windows":
            maxmode = 26
        else:
            maxmode = 18
        while modewanted > maxmode:
            modewanted = modewanted - maxmode
        while modewanted < 1:
            modewanted = modewanted + maxmode
        if modewanted == 1:
            print("1 = Menu Settings")
            setting = int(input("Please enter the group of settings you wish to modify."))
            if setting == 1:
                    print(" Modiy Menu Layout")
                    if layout != 0:
                        print(" 0 = Default")
                    elif layout != 1:
                        print(" 1 = Pages")
                    layout = int(input("Please input the number of the setting you wish to apply."))
                    try:
                        os.remove("./menusettings.py")
                        os.remove("./menusettings.pyc")
                    except(IOError, OSError):
                        pass
                    with open ("./menusettings.py","a") as outf:
                        outf.write("layout = ")
                        outf.write(str(layout))
                    if layout == 0:
                        page = -1
                    elif layout == 1:
                        page = 0
            elif setting == 2:
                print("1 = Hide power menu modes.")
                settinga = int(input("Please input the number of the setting you wish to modify."))
                if settinga == 1:
                    print("2 = Restart hidden = ", restartsettings.hidden)
                    print("3 = Logoff hidden = ", logoffsettings.hidden)
                    print("4 = Hibernate hidden = ", hibernatesettings.hidden)
                    print("5 = Shutdown hidden = ", shutdownsettings.hidden)
                    print("6 = Call a Python Shell hidden = ", pyshellsettings.hidden)
                    print("7 = Create folders hidden = ", foldercreatesettings.hidden)
                    print("8 = Remove folders hidden = ", exfoldersettings.hidden)
                    print("9 = Create files hidden = ", addfilesettings.hidden)
                    print("10 = Restart this script hidden = ", scriptloopsettings.hidden)
                    print("11 = Perform arithmetic operations hidden = ", mathmodesettings.hidden)
                    print("12 = Lock this script hidden = ", scriptlocksettings.hidden)
                    print("13 = Start Installer hidden = ", installerstartsettings.hidden)
                    print("14 = Print SystemInfo hidden = ", sysinfosettings.hidden)
                    print("15 = Exit hidden = ", exitsettings.hidden)
                    hidestate = int(input("Please select the number of the mode."))
                    if hidestate == 2:
                        LolexToolsMethods.modehide("restart", restartsettings.hidden)
                    elif hidestate == 3:
                        LolexToolsMethods.modehide("logoff", logoffsettings.hidden)
                    elif hidestate == 4:
                        LolexToolsMethods.modehide("hibernate", hibernatesettings.hidden)
                    elif hidestate == 5:
                        LolexToolsMethods.modehide("shutdown", shutdownsettings.hidden)
                    elif hidestate == 6:
                        LolexToolsMethods.modehide("pyshell", pyshellsettings.hidden)
                    elif hidestate == 7:
                        LolexToolsMethods.modehide("foldercreate", foldercreatesettings.hidden)
                    elif hidestate == 8:
                        LolexToolsMethods.modehide("exfolder", exfoldersettings.hidden)
                    elif hidestate == 9:
                        LolexToolsMethods.modehide("addfile", addfilesettings.hidden)
                    elif hidestate == 10:
                        LolexToolsMethods.modehide("scriptloop", scriptloopsettings.hidden)
                    elif hidestate == 11:
                        LolexToolsMethods.modehide("mathmode", mathmodesettings.hidden)
                    elif hidestate == 12:
                        LolexToolsMethods.modehide("scriptlock", scriptlocksettings.hidden)
                    elif hidestate == 13:
                        LolexToolsMethods.modehide("installerstart", installerstartsettings.hidden)
                    elif hidestate == 14:
                        LolexToolsMethods.modehide("sysinfo", sysinfosettings.hidden)
                    elif hidestate == 15:
                        LolexToolsMethods.modehide("exit", exitsettings.hidden)
                    #if useros == "Windows":
                        
                    if useros == "Windows":
                        if sys.version_info.minor>5:
                            os.system("py .\start.py")
                        else:
                            os.system("python .\start.py")
                    else:
                        os.system("python3 ./start.py")
                    exit(None)
        elif modewanted == 2:
            LolexToolsMethods.restart()
        elif modewanted == 3:
            logoff = float(input("Please enter 1 or 0 to confirm logoff."))
            if logoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -l -f")
                else:
                    os.system("gnome-session-quit --force")
        elif modewanted == 4 and useros == "Windows" :
            altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
            if altlogoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
                time.sleep(waittime * 60)
                subprocess.Popen ("logoff.exe")
        elif (modewanted == 5 and useros == "Windows") or (modewanted == 4 and useros == "Linux"):
            hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
            if hibernate == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -h -f")
                else:
                    os.system("systemctl suspend")
        elif (modewanted == 6 and useros == "Windows") or (modewanted == 5 and useros == "Linux"):
                shutdown = int(input("Please enter 1 or 0 (no) to confirm shutdown."))
                if shutdown == 1:
                    waittime = float(input("How long, in minutes, do you wish to wait?"))
                    time.sleep (waittime * 60)
                    if useros == "Windows":
                        os.system ("shutdown -s -f")
                    elif "arm" in platform.platform()==False:
                        os.system("poweroff")
                    else:
                        if os.system("su -c reboot -p") != 0:
                            if os.system("/system/bin/reboot -p") != 0:
                                print("Failed to execute reboot binary.")
        elif modewanted == 7 and useros == "Windows" :
            altshutdown = int(input("Please enter 1 or 0 to confirm shutdown."))
            if altshutdown == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
                time.sleep (waittime * 60)
                subprocess.Popen ("shutdown.exe")
        elif modewanted == 8 and useros == "Windows" :
            LolexToolsMethods.flicker()
        elif modewanted == 9 and useros == "Windows" :
            subprocess.call("cmd.exe")
        elif modewanted == 10 and useros == "Windows" :
            subprocess.Popen("explorer.exe")
        elif (modewanted == 11 and useros == "Windows") or (modewanted == 6 and useros == "Linux"):
            if useros == "Windows":
                subprocess.call("python.exe")
            else:
                os.system("python3")
        elif modewanted == 12 and useros == "Windows" :
            subprocess.Popen("taskmgr.exe")
        elif (modewanted == 13 and useros == "Windows") or (modewanted == 7 and useros == "Linux"):
            foldername = input("Please input the name of your new folder.")
            try:
                os.makedirs (foldername)
                cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Failed to create folder: ", foldername)
        elif (modewanted == 14 and useros == "Windows") or (modewanted == 8 and useros == "Linux"):
            foldername = input("Please input the name of the folder you wish to delete.")
            try:
                 os.rmdir (foldername)
                 cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Folder does not exist!")
        elif (modewanted == 15 and useros == "Windows") or (modewanted == 9 and useros == "Linux"):
            try:
                filename = input("Please enter your file name plus the extension, eg. B.txt.  ")
                with io.FileIO (filename, "w"):
                    pass
                cont = input("Success! Press any key then enter to continue...")
            except(IOError, OSError):
                print("Failed to create file: ",filename)
        elif (modewanted == 16 and useros == "Windows") or (modewanted == 10 and useros == "Linux"):
            confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
            if confirmscriptrestart == 1:
                if useros == "Windows":
                    if sys.version_info.minor<6:
                        os.system("python .\start.py")
                    else:
                        os.system("py .\start.py")
                else:
                    os.system("python3 ./start.py")
                exit(None)
        elif (modewanted == 17 and useros == "Windows") or (modewanted == 11 and useros == "Linux"):
            print ("Here is a list of operations:")
            print ("1 = Add")
            print ("2 = Take")
            submode = int(input("Please enter the number of the operatino you wish to perform."))
            if submode == 1 or 2:
                startnum = int(input("Please enter your starting number."))
                addortakenum = int(input("Please input the number to be added."))
                endnum = int(input("Please enter your end number."))
                waittime = int(input("How long do you wish to wait before each operation is performed?"))
                if endnum>startnum:
                    while endnum>startnum:
                        print(startnum)
                        if addortakenum<int(0):
                            startnum = startnum - addortakenum
                        elif addortakenum > int(0):
                            startnum = startnum + addortakenum
                        time.sleep(waittime)
                    if startnum == endnum or startnum>endnum:
                        print("The closest number to your target number was:" + (str(startnum)))
                        time.sleep (1)
                    elif startnum > endnum:
                        while startnum > endnum:
                            print (startnum)
                            if addortakenum < 0:
                                startnum = startnum + addortakenum
                            if addortakenum>0:
                                startnum = startnum = startnum - addortakenum
                                time.sleep (waittime)
                        if startnum == endnum or startnum<endnum:
                            print ("The closest number to your target end number was:" + (str(startnum)))
                            time.sleep (1)
        elif (modewanted == 18 and useros == "Windows") or (modewanted == 12 and useros == "Linux"):
            print ("Feature currently unavailable(under development).")
        elif modewanted == 19  and useros == "Windows" :
            path = input("Please input the full path of the RDP file.")
            length = len(path) - 1
            if path[length] == "p":
                length = length - 1
                if path[length] == "d":
                    length = length - 1
                    if path[length] == "r":
                        length = length - 1
                        if path[length] == ".":
                            os.system(path)
            else:
                print("Not a valid rdp file.")
        elif modewanted == 20 and useros == "Windows" :
            subprocess.call("powershell.exe")
        elif modewanted == 21 and useros == "Windows":
            os.system("systeminf")
        elif (modewanted == 22 and useros == "Windows") or (modewanted == 13 and useros == "Linux"):
            confirm = int(input("Please confirm (with a 1) to enter the installer."))
            if confirm == 1:
                if useros == "Windows":
                    if sys.version_info.minor>5:
                        os.system("py .\LolexToolsInstaller.py")
                    else:
                        os.system("python .\LolexToolsInstaller.py")
                else:
                    os.system("python3 ./LolexToolsInstaller.py")
                exit(None)
        elif (modewanted == 14 and useros == "Linux"):
            if "arm" in platform.platform():
                if os.system("su -c uptime") != 0:
                    if os.system("/system/bin/uptime")!= 0:
                        print("Failed to run uptime script.")
            else:
                os.system("uptime")
        elif modewanted == 15 and useros == "Linux":
            if "arm" in platform.platform():
                if os.system("su -c /system/bin/dumpsys") != 0:
                    print("Cannot load as much information due to lack of root.")
                    if os.system("/system/bin/dumpsys") != 0:
                        print("Failed to execute dumpsys binary. Please check your root and SELinux statuses.")
            else:
                os.system("sudo lshw")
        elif (modewanted == 24 and useros == "Windows"):
            print("Checking for updates...")
            print("Upon prompt for saving the file, please save as Lolex-Tools-master.zip in your Lolex-Tools folder.")
            if os.system("git clone https://github.com/lolexorg/Lolex-Tools.git") != 0:
                continueto = int(input("Git was not found. Please press 1 to initiate webbrowser method or 0 to cancel."))
                if continueto == 1:
                    print("Please save your zip to Lolex-Tools newversion folder.")
                    os.system("python -m webbrowser -t https://github.com/lolexorg/Lolex-Tools/zipball/master")
                    confirm = input("Press enter to continue...")
                    try:
                        os.remove("./newversion")
                    except(IOError, OSError):
                        pass
                    os.mkdirs("./newversion")
                    newver = os.listdirs("./newversion")
                                
        # search for zips instead :P
                    zip_ref = zipfile.ZipFile("./newversion"+newver[0], "r")
                    print("Extracting...")
                    zip_ref.extractall("newversion")
                    zip_ref.close()   
        elif (modewanted == 25 and useros == "Windows") or (modewanted == 17 and useros == "Linux") and menusettings.layout == 1:
            if (page < 5 and useros == "Windows") or (page < 2 and useros == "Linux"):
                page = page + 1
            else:
                page = 0
        elif (modewanted == 26 and useros == "Windows") or (modewanted == 18 and useros == "Linux") and menusettings.layout == 1:
            if page > 0:
                page = page - 1
            else:
                if useros == "Windows":
                    page = 5
                else:
                    page = 2
        elif (modewanted == 23 and useros == "Windows") or (modewanted == 16 and useros == "Linux"):
            print("Exiting...")
            print("Giving all threads 5 seconds to exit...")
            time.sleep(5)
            os._exit(0)
except(SyntaxError):
     print("Sorry! A SyntaxError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(TypeError):
     print("Sorry! A TypeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(ValueError):
     print("Sorry! A ValueError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(IOError):
     print("Sorry! An IOError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(NameError):
     print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(EOFError):
     print("Sorry! An EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(AttributeError):
     print("Sorry! An AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(OSError):
     print("Sorry! An OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(ZeroDivisionError):
    print("Sorry! A ZeroDivisionError occured. Please do not try to divide by zero.")
    time.sleep(10)
except(KeyboardInterrupt):
    print("User input caused a crash.")
    time.sleep(10)
