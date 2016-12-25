#! python3
import sys, time, subprocess, os, shutil, py_compile, platform, io
try:
    import isnottravisci
except(ImportError):
    print("Please create isnottravisci.py to continue.")
    time.sleep(5)
    exit(None)
system = platform.system()
if system == "Windows":
    os.system("mode 1000")
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
        subprocess.call(".\LolexToolsInstaller.py", shell = True)
    else:
        os.system("python3 ./LolexToolsInstaller.py")
    exit(None)
if system == "Windows":
    os.system(theme.theme)
print("Welcome to Lolex-Tools version 8.2exp 12:33 GMT+0.0 15/12/16")
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
            print(LolexToolsOptions.username1)
            print(LolexToolsOptions.username2)
            print(usernameenter, LolexToolsOptions.username1, LolexToolsOptions.username2)
            usernameenter = input("Please enter a valid username.")
            
    elif LolexToolsOptions.useusername == False:
        usernameenter = LolexToolsOptions.username1
    if LolexToolsOptions.username1 == usernameenter:
        if runtimeone == LolexToolsOptions.onepintotal:
            runtimeone = 1
        else:
            runtimeone = runtimeone + 1
        if LolexToolsOptions.onepintotal != 0:
            if runtimeone == 1 or oneswappins == False:
                pin = int(LolexToolsOptions.onepinone)
            elif runtimeone == 2:
                pin = int(LolexToolsOptions.onepintwo)
            elif runtimeone == 3:
                pin = int(LolexToolsOptions.onepinthree)
            elif runtimeone == 4:
                pin = int(LolexToolsOptions.onepinfour)
            elif runtimeone == 5:
                pin = int(LolexToolsOptions.onepinfive)
            else:
                pin = False
                print(False)
            codeenter = int(input("Please enter your current PIN."))
            print(pin)
            tries = 1
            if codeenter != pin:
                while codeenter != pin:
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
                if wordtimeone == 1 or oneswapwords == False:
                    word = LolexToolsOptions.onewordone
                elif wordtimeone == 2:
                    word = LolexToolsOptions.onewordtwo
                elif wordtimeone == 3:
                    word = LolexToolsOptions.onewordthree
                elif wordtimeone == 4:
                    word = LolexToolsOptions.onewordfour
                elif wordtimeone == 5:
                    word = LolexToolsOptions.onewordfive
                else:
                    word = False
            wordenter = input("Please enter your current password.")
            tries = 1
            while wordenter != word:
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
            if runtimetwo == 1 or twoswappins == False:
                pin = int(LolexToolsOptions.twopinone)
            elif runtimetwo == 2:
                pin = int(LolexToolsOptions.twopintwo)
            elif runtimetwo == 3:
                pin = int(LolexToolsOptions.twopinthree)
            elif runtimetwo == 4:
                pin = int(LolexToolsOptions.twopinfour)
            elif runtimetwo == 5:
                pin = int(LolexToolsOptions.twopinfive)
            else:
                pin = False
                print(False)
            codeenter = int(input("Please enter your current PIN."))
            print(pin)
            tries = 1
            if codeenter != pin:
                while codeenter != pin:
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
                if wordtimetwo == 1 or twoswapwords == False:
                    word = LolexToolsOptions.twowordone
                elif wordtimetwo == 2:
                    word = LolexToolsOptions.twowordtwo
                elif wordtimetwo == 3:
                    word = LolexToolsOptions.twowordthree
                elif wordtimetwo == 4:
                    word = LolexToolsOptions.twowordfour
                elif wordtimetwo == 5:
                    word = LolexToolsOptions.twowordfive
                else:
                    word = False
            wordenter = input("Please enter your current password.")
            tries = 1
            while wordenter != word:
                if tries == 5:
                    print("You got your password wrong 5 times.")
                    time.sleep(LolexToolsOptions.twowordwait)
                    tries = 0
                wordenter = input("Please enter your current password.")
                tries = tries + 1
##            if runtimetwo == 1 or LolexToolsOptions.twopintwo == False:
##                while codeenter != LolexToolsOptions.twopinone:
##                    if tries == 5:
##                        print("Sorry! You got the code wrong five times.")
##                        time.sleep(LolexToolsOptions.twowait)
##                        tries = 0
##                    codeenter = int(input("Please enter your current PIN."))
##                    tries = tries + 1
##            else:
##                if runtimetwo == 2:
##                    while codeenter != LolexToolsOptions.twopintwo:
##                        if tries == 5:
##                            print("Sorry! You got the code wrong five times.")
##                            time.sleep(LolexToolsOptions.twowait)
##                            tries = 0
##                        codeenter = int(input("Please enter your current PIN."))
##                        tries = tries + 1
##                elif runtimetwo == 3:
##                    while codeenter != LolexToolsOptions.twopinthree:
##                        if tries == 5:
##                            print("Sorry! You got the code wrong five times.")
##                            time.sleep(LolexToolsOptions.twowait)
##                            tries = 0
##                        codeenter = int(input("Please enter your current PIN."))
##                        tries = tries + 1
##                elif runtimetwo == 4:
##                    while codeenter != LolexToolsOptions.twopinfour:
##                        if tries == 5:
##                            print("Sorry! You got the code wrong five times.")
##                            time.sleep(LolexToolsOptions.twowait)
##                            tries = 0
##                        codeenter = int(input("Please enter your current PIN."))
##                        tries = tries + 1
##                elif runtimetwo == 5:
##                    while codeenter != LolexToolsOptions.twopinfive:
##                        if tries == 5:
##                            print("Sorry! You got the code wrong five times.")
##                            time.sleep(LolexToolsOptions.twowait)
##                            tries = 0
##                        codeenter = int(input("Please enter your current PIN."))
##                        tries = tries + 1
##    if ((oneuseword == True and usernameenter == LolexToolsOptions.username1)or(twouseword == True and usernameenter == LolexToolsOptions.username2)):
##        if usernameenter == LolexToolsOptions.username2:
##            wordenter = input("Please enter your current password.")
##    ##        tries = 1
##    ##        if usernameenter == LolexToolsOptions.username1:
##    ##            if oneswapwords == False or wordtimeone == 1:
##    ##                while wordenter != LolexToolsOptions.onewordone:
##    ##                    if tries == 5:
##    ##                        print("Sorry! You got the password wrong five times.")
##    ##                        time.sleep(LolexToolsOptions.onewordwait)
##    ##                        tries = 0
##    ##                    wordenter = input("Please enter your current password.")
##    ##                    tries = tries + 1
##    ##            elif wordtimeone == 2:
##    ##                while wordenter != LolexToolsOptions.onewordtwo:
##    ##                    if tries == 5:
##    ##                        print("Sorry! You got the password wrong five times.")
##    ##                        time.sleep(LolexToolsOptions.onewordwait)
##    ##                        tries = 0
##    ##                    wordenter = input("Please enter your current password.")
##    ##                    tries = tries + 1
##    ##            elif wordtimeone == 3:
##    ##                while wordenter != LolexToolsOptions.onewordthree:
##    ##                    if tries == 5:
##    ##                        print("Sorry! You got the password wrong five times.")
##    ##                        time.sleep(LolexToolsOptions.onewordwait)
##    ##                        tries = 0
##    ##                    wordenter = input("Please enter your current password.")
##    ##                    tries = tries + 1
##    ##            elif wordtimeone == 4:
##    ##                while wordenter != LolexToolsOptions.onewordfour:
##    ##                    if tries == 5:
##    ##                        print("Sorry! You got the password wrong five times.")
##    ##                        time.sleep(LolexToolsOptions.onewordwait)
##    ##                        tries = 0
##    ##                    wordenter = input("Please enter your current password.")
##    ##                    tries = tries + 1
##    ##            elif wordtimeone == 5:
##    ##                while wordenter != LolexToolsOptions.onewordfive:
##    ##                    if tries == 5:
##    ##                        print("Sorry! You got the password wrong five times.")
##    ##                        time.sleep(LolexToolsOptions.onewordwait)
##    ##                        tries = 0
##    ##                    wordenter = input("Please enter your current password.")
##    ##                    tries = tries + 1
##            if usernameenter == LolexToolsOptions.username2:
##                if twoswapwords == False or wordtimetwo == 1:
##                    while wordenter != LolexToolsOptions.twowordone:
##                        if tries == 5:
##                            print("Sorry! You got the password wrong five times.")
##                            time.sleep(LolexToolsOptions.twowordwait)
##                            tries = 0
##                        wordenter = input("Please enter your current password.")
##                        tries = tries + 1
##                elif wordtimetwo == 2:
##                    while wordenter != LolexToolsOptions.twowordtwo:
##                        if tries == 5:
##                            print("Sorry! You got the password wrong five times.")
##                            time.sleep(LolexToolsOptions.twowordwait)
##                            tries = 0
##                        wordenter = input("Please enter your current password.")
##                        tries = tries + 1
##                elif wordtimetwo == 3:
##                    while wordenter != LolexToolsOptions.twowordthree:
##                        if tries == 5:
##                            print("Sorry! You got the password wrong five times.")
##                            time.sleep(LolexToolsOptions.twowordwait)
##                            tries = 0
##                        wordenter = input("Please enter your current password.")
##                        tries = tries + 1
##                elif wordtimetwo == 4:
##                    while wordenter != LolexToolsOptions.twowordfour:
##                        if tries == 5:
##                            print("Sorry! You got the password wrong five times.")
##                            time.sleep(LolexToolsOptions.twowordwait)
##                            tries = 0
##                        wordenter = input("Please enter your current password.")
##                        tries = tries + 1
##                elif wordtimetwo == 5:
##                    while wordenter != LolexToolsOptions.twowordfive:
##                        if tries == 5:
##                            print("Sorry! You got the password wrong five times.")
##                            time.sleep(LolexToolsOptions.twowordwait)
##                            tries = 0
##                        wordenter = input("Please enter your current password.")
##                        tries = tries + 1
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
    page = 0
    layout = menusettings.layout
    while True:
        modeone = "1 = Settings" #all
        modetwo = "2 = Restart" #all
        modethree = "3 = Logoff" #Windows
        modefour = "4 = Alternative Logoff Method" #Windows
        modefourlinux = "4 = Hibernate"  #all
        modefive = "5 = Hibernate"
        modefivelinux = "5 = Shutdown" #all
        modesix = "6 = Shutdown"
        modesixlinux = "6 = Call A Python Shell" #all
        modesevenlinux = "7 = Create folders in the current location" #all
        modeseven = "7 = Alternative Shutdown Method" #Windows
        modeeight = "8 = Colour Flicker" #Windows
        modeeightlinux = "8 = Remove Directories" #all
        modenine = "9 = Call CMD"
        modeninelinux = "9 = Create files in the current location"
        modeten = "10 = Call Documents"
        modetenlinux = "10 = Restart This Script (debug purposes)"
        modeeleven = "11 = Call A Python Shell"
        modeelevenlinux = "11 = Perform Operations With Numbers"
        modetwelve = "12 = Call Task Manager"
        modetwelvelinux = "12 = Lock This Script"
        modethirteen = "13 = Create folders in the current location"
        modethirteenlinux = "13 = Start Installer"
        modefourteen = "14 = Remove Directories"
        modefourteenlinux = "14 = Show uptime and average load"
        modefifteenlinux = "15 = Dump system information into terminal"
        exitmodelinux = "16 = Exit"
        exitmodeandroid = "18 = Exit"
        modefifteen = "15 = Create files in the current location"
        modesixteen = "16 = Restart This Script (debug purposes)"
        modeseventeen = "17 = Perform Operations With Numbers"
        modeeightteen = "18 = Lock This Script"
        modenineteen = "19 = Call Remote Desktop"
        modetwenty = "20 = Call Powershell"
        modetwentyone = "21 = Print Systeminfo"
        modetwentytwo = "22 = Start Installer"
        exitmode = "23 = Exit"
        nextpage = "24 = Next Page"
        nextpageandroid= "17= Next Page"
        backpage = "25 = Back A Page"
        backpageandroid = "18 = Back A Page"
        nextpagelinux = "17 = Next Page"
        backpagelinux = "18 = Back A Page"
        if layout == 0:
            print(modeone)
            if restartsettings.hidden != True:
                print (modetwo)
            if logoffsettings.hidden != True:
                print (modethree)
            if useros == "Windows":
                if logoffsettings.hidden != True:
                    print (modefour)
                if hibernatesettings.hidden != True:
                    print(modefive)
                if shutdownsettings.hidden != True:
               	    print(modesix)
            else:
                if hibernatesettings.hidden != True:
                    print(modefourlinux)
                if shutdownsettings.hidden != True:
                    print(modefivelinux)
                print(modesixlinux)
                print(modesevenlinux)
            if useros == "Windows":
                print (modeseven)
                print (modeeight)
                print (modenine)
                print (modeten)
                print (modeeleven)
            if useros == "Windows":
                print (modetwelve)
                print (modethirteen)
                print (modefourteen)
                print (modefifteen)
                print(modesixteen)
                print(modeseventeen)
                print(modeeightteen)
            else:
                print(modeeightlinux)
                print(modeninelinux)
                print(modetenlinux)
                print(modeelevenlinux)
                print(modetwelvelinux)
                print(modethirteenlinux)
                print(modefourteenlinux)
                print(modefifteenlinux)
                print(exitmodelinux)
            if useros == "Windows":
                print (modenineteen)
                print (modetwenty)
                print (modetwentyone)
                print(modetwentytwo)
                print(exitmode)
        elif layout == 1:
            if page == 0:
                print(modeone)
                if restartsettings.hidden != True:
                    print (modetwo)
                if logoffsettings.hidden != True:
                    print (modethree)
                if useros == "Windows":
                    if logoffsettings.hidden != True:
                        print (modefour)
                    if hibernatesettings.hidden != True:
                        print (modefive)
                    print (nextpage)
                else:
                    if hibernatesettings.hidden != True:
                        print(modefourlinux)
                    if shutdownsettings.hidden != True:
                        print(modefivelinux)
                    print(nextpagelinux)
                    print(backpagelinux)
                    
            elif page == 1:
                if useros == "Windows":
                    if shutdownsettings.hidden != True:
                        print(modesix)
                    print (modeseven)
                    print (modeeight)
                    print (modenine)
                    print (modeten)
                    print(nextpage)
                    print(backpage)
                elif useros == "Linux":
                    page = page + 1
            if page == 2:
                if useros == "Linux":
                    print(modesixlinux)  
                elif useros == "Windows":
                    print(modeeleven)
                if useros == "Linux":
                    print(modesevenlinux)
                    print(modeeightlinux)
                    print(modeninelinux)
                    print(modetenlinux)
                    print(nextpagelinux)
                    print(backpagelinux)
                elif useros == "Windows":
                    print (modetwelve)
                    print (modethirteen)
                    print (modefourteen)
                    print (modefifteen)
                    print(nextpage)
                    print(backpage)
            elif page == 3:
                if useros != "Linux":
                    print (modesixteen)
                    print (modeseventeen)
                    print (modeeightteen)
                else:
                    print(modeelevenlinux)
                    print(modetwelvelinux)
                    print(modethirteenlinux)
                    print(modefourteenlinux)
                    print(modefifteenlinux)
                    print(exitmodelinux)
                if useros == "Windows":
                    print (modenineteen)
                    print (modetwenty)
                    
                if useros == "Windows":
                    print(nextpage)
                    print(backpage)
                else:
                        print(nextpagelinux)
                        print(backpagelinux)
            elif page == 4:
                if useros == "Windows":
                    print (modetwentyone)
                    print(modetwentytwo)
                    print(exitmode)
                    print(backpage)
                else:
                    print(backpagelinux)
        modewanted = int(input("Please enter the number of the mode that you want."))
        while modewanted > 25:
            modewanted = modewanted - 25
        while modewanted < 1:
            modewanted = modewanted + 25
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
            elif setting == 2:
                print("1 = Hide power menu modes.")
                settinga = int(input("Please input the number of the setting you wish to modify."))
                if settinga == 1:
                    print(modetwo, "hidden = ", restartsettings.hidden)
                    print(modethree, "hidden = ", logoffsettings.hidden)
                    print(modefourlinux, "hidden = ", hibernatesettings.hidden)
                    print(modefivelinux, "hidden = ", shutdownsettings.hidden)
                    hidestate = int(input("Please select the number of the mode."))
                    if hidestate == 2:
                        LolexToolsMethods.modehide("restart", restartsettings.hidden)
                        restartneeded = True
                    elif hidestate == 3:
                        LolexToolsMethods.modehide("logoff", logoffsettings.hidden)
                        restartneeded = True
                    elif hidestate == 4:
                        LolexToolsMethods.modehide("hibernate", hibernatesettings.hidden)
                        restartneeded = True
                    elif hidestate == 5:
                        LolexToolsMethods.modehide("shutdown", shutdownsettings.hidden)
                        restartneeded = True
                    if restartneeded == True:
                        if useros == "Windows":
                            os.system("python .\start.py")
                        else:
                            os.system("python3 ./start.py")
                        exit(None)
        elif modewanted == 2:
            LolexToolsMethods.mode2()
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
                subprocess.call ("logoff.exe")
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
                        os.system("shutdown now")
                    else:
                        os.system("/system/bin/reboot -p")
        elif modewanted == 7 and useros == "Windows" :
            altshutdown = int(input("Please enter 1 or 0 to confirm shutdown."))
            if altshutdown == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
                time.sleep (waittime * 60)
                subprocess.call ("shutdown.exe")
        elif modewanted == 8 and useros == "Windows" :
            LolexToolsMethods.flicker()
        elif modewanted == 9 and useros == "Windows" :
            subprocess.call("cmd.exe")
        elif modewanted == 10 and useros == "Windows" :
            subprocess.call("explorer.exe")
        elif (modewanted == 11 and useros == "Windows") or (modewanted == 6 and useros == "Linux"):
            if useros == "Windows":
                os.system("python")
            else:
                os.system("python3")
        elif modewanted == 12 and useros == "Windows" :
            subprocess.call("taskmgr.exe")
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
                    os.system("python .\start.py")
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
                    if startnum ==endnum or startnum>endnum:
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
            subprocess.call("mstsc.exe")
        elif modewanted == 20 and useros == "Windows" :
            subprocess.call("powershell.exe")
        elif modewanted == 21 and useros == "Windows":
            os.system("systeminf")
        elif (modewanted == 22 and useros == "Windows") or (modewanted == 13 and useros == "Linux"):
            confirm = int(input("Please confirm (with a 1) to enter the installer."))
            if confirm == 1:
                if useros == "Windows":
                    os.system("LolexToolsInstaller.py")
                else:
                    os.system("python3 ./LolexToolsInstaller.py")
                exit(None)
        elif (modewanted == 14 and useros == "Linux"):
            if "arm" in platform.platform():
                os.system("/system/bin/uptime")
            else:
                os.system("uptime")
        elif modewanted == 15 and useros == "Linux":
            if "arm" in platform.platform():
                if os.system("su -c /system/bin/dumpsys") != 0:
                    print("Cannot load as much information due to lack of root.")
                    os.system("/system/bin/dumpsys")
            else:
                os.system("sudo lshw")
        elif (modewanted == 24 and useros == "Windows") or (modewanted == 17 and useros == "Linux"):
            if (page < 4 and useros == "Windows") or (page < 3 and useros == "Linux"):
                page = page + 1
            else:
                page = 0
        elif (modewanted == 25 and useros == "Windows") or (modewanted == 18 and useros == "Linux"):
            if page == 2 and useros == "Linux":
                page = 0
            elif page == 3 and useros == "Linux":
                page = 1
            elif page < 0:
                page = page - 1
            else:
                if useros == "Windows":
                    page = 4
                else:
                    page = 3
            
        elif (modewanted == 23 and useros == "Windows") or (modewanted == 16 and useros == "Linux"):
            print("Exiting...")
            sys.exit()
            print("Should have exited...")
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
except():
     print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(EOFError):
     print("Sorry! An EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except():
     print("Sorry! An AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(OSError):
     print("Sorry! An OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(ZeroDivisionError):
    print("Sorry! A ZeroDivisionError occured. Please do not try to divide by zero.")
