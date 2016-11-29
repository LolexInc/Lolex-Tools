#! python3
import sys, time, subprocess, os, shutil, py_compile, platform
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
    import JTToolsMethods
except(ImportError):
    print("Missing library. Please redownload this application.")
try:
    import verifonboot, JTToolsOptions, runningsys, startplugins, theme
except(ImportError):
    system = platform.system()
    if system == "Windows":
    	subprocess.call("./JTToolsInstaller.py", shell = True)
    else:
    	os.system("python3 ./JTToolsInstaller.py")
    exit(None)
print("Welcome to Lolex-Tools version 8.11patch1 13:41 GMT+0.0 29/11/16")
try:
    oneswappins = verifonboot.oneswappins
    twoswappins = verifonboot.twoswappins
    runtimeone = verifonboot.runtimeone
    runtimetwo = verifonboot.runtimetwo
    oneswapwords = verifonboot.oneswapwords
    twoswapwords = verifonboot.twoswapwords
    wordtimeone = verifonboot.wordtimeone
    wordtimetwo = verifonboot.wordtimetwo
    oneuseword = JTToolsOptions.oneuseword
    twouseword = JTToolsOptions.twouseword
    if JTToolsOptions.useusername == True:
        usernameenter = True
        while usernameenter != (JTToolsOptions.username1 or JTToolsOptions.username2):
            usernameenter = input("Please enter a valid username.")
    elif JTToolsOptions.useusername == False:
        usernameenter = JTToolsOptions.username1
    if JTToolsOptions.username1 == usernameenter:
        if verifonboot.oneswappins == True:
            if JTToolsOptions.onepintwo == False:
                oneswappins = False
            elif((JTToolsOptions.onepinthree == False) and (runtimeone == 2) or ((JTToolsOptions.onepinfour == False) and (runtimeone == 3)) or ((JTToolsOptions.onepinfive == False) and (runtimeone == 4)) or ((JTToolsOptions.onepinfive != False) and (runtimeone == 5)) or runtimeone == 0):
                 runtimeone = 1
            else:
                 runtimeone = runtimeone +1
        if verifonboot.oneswapwords == True:
            if JTToolsOptions.onewordtwo == False:
                oneswapwords = False
            elif ((JTToolsOptions.onewordthree == False) and (wordtimeone == 2) or ((JTToolsOptions.onewordfour == False) and (wordtimeone == 3)) or ((JTToolsOptions.onewordfive == False) and (wordtimeone == 4)) or ((JTToolsOptions.onewordfive != False) and (wordtimeone == 5)) or wordtimeone == 0):
                wordtimeone = 1
            else:
                wordtimeone = wordtimeone + 1
    elif JTToolsOptions.username2 == usernameenter:
        if verifonboot.twoswappins == True:
            if JTToolsOptions.onepintwo == False:
                twoswappins = False
            elif((JTToolsOptions.twopinthree == False) and (runtimetwo == 2) or ((JTToolsOptions.twopinfour == False) and (runtimetwo == 3)) or ((JTToolsOptions.twopinfive == False) and (runtimeone == 4)) or ((JTToolsOptions.twopinfive != False) and (runtimetwo == 5)) or runtimetwo == 0):
                    runtimetwo = 1
            else:
                runtimetwo = runtimetwo + 1
        if verifonboot.twoswapwords == True:
            if JTToolsOptions.twowordone == False:
                twoswapwords = False
            elif((JTToolsOptions.twowordthree == False) and (wordtimetwo == 2) or ((JTToolsOptions.twowordfour == False) and (wordtimetwo == 3)) or ((JTToolsOptions.twowordfive == False) and (wordtimeone == 4)) or ((JTToolsOptions.twowordfive != False) and (wordtimetwo == 5)) or wordtimetwo == 0):
                wordtimetwo = 1
            else:
                wordtimetwo = wordtimetwo + 1
    if (JTToolsOptions.oneusepin == True and usernameenter == JTToolsOptions.username1) or (JTToolsOptions.twousepin == True and usernameenter == JTToolsOptions.username2):
        codeenter = int(input("Please enter your current PIN."))
        tries = 1
        if usernameenter == JTToolsOptions.username1:
            if oneswappins == False or runtimeone == 1:
                while codeenter != JTToolsOptions.onepinone:
                    if tries == 5:
                        print("Sorry! You got the code wrong five times.")
                        time.sleep(JTToolsOptions.onewait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
            else:
                if runtimeone == 2:
                    while codeenter != JTToolsOptions.onepintwo:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.onewait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimeone == 3:
                    while codeenter != JTToolsOptions.onepinthree:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.onewait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimeone == 4:
                    while codeenter != JTToolsOptions.onepinfour:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.onewait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimeone == 5:
                    while codeenter != JTToolsOptions.onepinfive:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.onewait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
        elif usernameenter == JTToolsOptions.username2:
            if runtimetwo == 1 or JTToolsOptions.twopintwo == False:
                while codeenter != JTToolsOptions.twopinone:
                    if tries == 5:
                        print("Sorry! You got the code wrong five times.")
                        time.sleep(JTToolsOptions.twowait)
                        tries = 0
                    codeenter = int(input("Please enter your current PIN."))
                    tries = tries + 1
            else:
                if runtimetwo == 2:
                    while codeenter != JTToolsOptions.twopintwo:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.twowait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimetwo == 3:
                    while codeenter != JTToolsOptions.twopinthree:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.twowait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimetwo == 4:
                    while codeenter != JTToolsOptions.twopinfour:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.twowait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
                elif runtimetwo == 5:
                    while codeenter != JTToolsOptions.twopinfive:
                        if tries == 5:
                            print("Sorry! You got the code wrong five times.")
                            time.sleep(JTToolsOptions.twowait)
                            tries = 0
                        codeenter = int(input("Please enter your current PIN."))
                        tries = tries + 1
    if ((oneuseword == True and usernameenter == JTToolsOptions.username1)or(twouseword == True and usernameenter == JTToolsOptions.username2)):
        wordenter = input("Please enter your current password.")
        tries = 1
        if usernameenter == JTToolsOptions.username1:
            if oneswapwords == False or wordtimeone == 1:
                while wordenter != JTToolsOptions.onewordone:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimeone == 2:
                while wordenter != JTToolsOptions.onewordtwo:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimeone == 3:
                while wordenter != JTToolsOptions.onewordthree:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimeone == 4:
                while wordenter != JTToolsOptions.onewordfour:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimeone == 5:
                while wordenter != JTToolsOptions.onewordfive:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.onewordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
        elif usernameenter == JTToolsOptions.username2:
            if twoswapwords == False or wordtimetwo == 1:
                while wordenter != JTToolsOptions.twowordone:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimetwo == 2:
                while wordenter != JTToolsOptions.twowordtwo:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimetwo == 3:
                while wordenter != JTToolsOptions.twowordthree:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimetwo == 4:
                while wordenter != JTToolsOptions.twowordfour:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
            elif wordtimetwo == 5:
                while wordenter != JTToolsOptions.twowordfive:
                    if tries == 5:
                        print("Sorry! You got the password wrong five times.")
                        time.sleep(JTToolsOptions.twowordwait)
                        tries = 0
                    wordenter = input("Please enter your current password.")
                    tries = tries + 1
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
        if JTToolsOptions.compiler == True:
            JTToolsMethods.compiler("verifonboot")
    useros = platform.system()
    while True:
        print ("Here is a list of modes available:")
        print ("1 = Restart")
        print ("2 = Logoff")
        if useros == "Windows":
            print ("3 = Alternative Logoff Method ")
        print ("4 = Hibernate")
        print ("5 = Shutdown")
        if useros == "Windows":
            print ("6 = Alternative Shutdown Method")
            print ("7 = Colour Flicker")
            print ("8 = Call CMD")
            print ("9 = Call Documents")
        print ("10 = Call A Python Shell")
        if useros == "Windows":
            print ("11 = Call Task Manager")
        print ("12 = Create folders in the same directory as this script.")
        print ("13 = Remove Directories")
        print ("14 = Create Files")
        print ("15 = Restart This Script (debug purposes)")
        print ("16 = Perform Operations With Numbers")
        print ("17 = Lock This Script")
        if useros == "Windows":
            print ("18 = Call Remote Desktop")
            print ("19 = Call Powershell")
            print ("20 = Print SystemInfo")
        print("21 = Start Installer")
        print("22 = Exit")
        modewanted = int(input("Please enter the number of the mode that you want."))
        if modewanted == 1:
            JTToolsMethods.mode1()
        elif modewanted == 2:
            logoff = float(input("Please enter 1 or 0 to confirm logoff."))
            if logoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -l -f")
                else:
                    os.system("logout")
        elif modewanted == 3 and useros == "Windows" :
            altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
            if altlogoff == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
                time.sleep(waittime * 60)
                subprocess.call ("logoff.exe")
        elif modewanted == 4:
            hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
            if hibernate == 1:
                waittime = float(input("How long, in minutes, do you wish to wait?"))
                time.sleep (waittime * 60)
                if useros == "Windows":
                    os.system ("shutdown -h -f")
                else:
                    os.system("systemctl suspend")
        elif modewanted == 5:
                shutdown = int(input("Please enter 1 or 0 (no) to confirm shutdown."))
                if shutdown == 1:
                    waittime = float(input("How long, in minutes, do you wish to wait?"))
                    time.sleep (waittime * 60)
                    if useros == "Windows":
                        os.system ("shutdown -s -f")
                    else:
                        os.system("shutdown now")
        elif modewanted == 6  and useros == "Windows" :
            altshutdown = int(input("Please enter 1 or 0 to confirm shutdown."))
            if altshutdown == 1:
                waittime = float(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
                time.sleep (waittime * 60)
                subprocess.call ("shutdown.exe")
        elif modewanted == 7  and useros == "Windows" :
            JTToolsMethods.flicker()
            import theme
        elif modewanted == 8  and useros == "Windows" :
            subprocess.call("cmd.exe")
        elif modewanted == 9 and useros == "Windows" :
            subprocess.call("explorer.exe")
        elif modewanted == 10:
            if useros == "Windows":
                os.system("python")
        elif modewanted == 11  and useros == "Windows" :
            subprocess.call("taskmgr.exe")
        elif modewanted == 12:
            foldername = input("Please input the name of your new folder.")
            os.makedirs (foldername)
            cont = input("Success! Press any key then enter to continue...")
        elif modewanted == 13:
            foldername = input("Please input the name of the folder you wish to delete.")
            os.rmdir (foldername)
            cont = input("Success! Press any key then enter to continue...")
        elif modewanted == 14:
            import io,time
            filename = input("Please enter your file name plus the extension, eg. B.txt.  ")
            with io.FileIO (filename, "w"):
                pass
        elif modewanted == 15:
            confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
            if confirmscriptrestart == 1:
                if useros == "Windows":
                    os.system("python ./start.py")
                else:
                    os.system("python3 ./start.py")
        elif modewanted == 16:
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
        elif modewanted == 17:
            print ("Locked!!!")
        elif modewanted == 18  and useros == "Windows" :
            subprocess.call("mstsc.exe")
        elif modewanted == 19 and useros == "Windows" :
            subprocess.call("powershell.exe")
        elif modewanted == 20 and useros == "Windows":
            os.system("systeminf")
        elif modewanted == 21:
            confirm = int(input("Please confirm (with a 1) to enter the installer."))
            if confirm == 1:
                if useros == "Windows":
                    os.system("python ./JTToolsInstaller.py")
                else:
                    os.system("python3 ./JTToolsInstaller.py")
        elif modewanted == 22:
            exit()
        else:
            print("Sorry! There is no such mode as the one specified. Please make a feature request on Github if you wish to see more functionality.")
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
