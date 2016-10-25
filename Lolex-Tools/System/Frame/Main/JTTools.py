import sys, time, subprocess, os, shutil, py_compile
sys.path.insert(0,"/Lolex-Tools/Lolex-Tools")
try:
    import isnottravisci
except(ImportError):
    print("Running as Travis CI...\nIf you are human please create isnottravisci.py to continue.")
    time.sleep(10)
    exit()
try:
    sys.path.insert(0,"/User/Data/")
    import JTToolsOptions
except(ImportError):
    print("Starting installer due to missing options file...")
    sys.path.insert(0,"/Lolex-Tools/Lolex-Tools/")
    subprocess.call("JTToolsInstaller.py", shell = True)

    
try:
    sys.path.insert(0,"/System/Lib/")
    import JTToolsMethods
except(ImportError):
    print("Missing library. Please redownload this application.")
    time.sleep(10)
    exit()
try:
    sys.path.insert(0,"/User/Data")
    import theme
except(ImportError):
    pass
try:
    import verifonboot
except(ImportError):
    print("Starting installer due to missing data file...")
    sys.path.insert(0,"/System/")
    subprocess.call("JTToolsInstaller.py", shell = True)
try:
    sys.path.insert(0,"/User/Data")
    import startplugins
except(ImportError, ValueError, SyntaxError, TypeError, OSError, NameError):
    print("Starting installer due to missing data file...")
    sys.path.insert(0,"/System/")
    subprocess.call("JTToolsInstaller.py", shell = True)
print("Welcome to Lolex-Tools version 8.002")
try:
    oneswappins = verifonboot.oneswappins
    twoswappins = verifonboot.twoswappins
    runtimeone = verifonboot.runtimeone
    runtimetwo = verifonboot.runtimetwo
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
                runtimeone = runtimeone + 1
    elif JTToolsOptions.username2 == usernameenter:
        if verifonboot.twoswappins == True:
            if JTToolsOptions.onepintwo == False:
                twoswappins = False
            elif((JTToolsOptions.twopinthree == False) and (runtimetwo == 2) or ((JTToolsOptions.twopinfour == False) and (runtimetwo == 3)) or ((JTToolsOptions.twopinfive == False) and (runtimeone == 4)) or ((JTToolsOptions.twopinfive != False) and (runtimetwo == 5)) or runtimetwo == 0):
                        runtimetwo = 1
            else:
                runtimetwo = runtimetwo + 1
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
            elif runtimeone == 2:
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
            elif runtimetwo == 2:
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
    if (verifonboot.runtimeone != runtimeone) or (verifonboot.runtimetwo != runtimetwo) or (verifonboot.oneswappins != oneswappins) or (verifonboot.twoswappins != twoswappins):
        try:
            sys.path.insert(0,"/Lolex-Tools/Lolex-Tools/")
            os.remove("/User/Data/verifonboot.py")
        except(IOError):
            try:
                os.remove("/User/Data/verifoboot.pyc")
            except(IOError):
                print("verifonboot.pyc was not found.")
        with open ("/User/Data/verifonboot.py","a") as outf:
            outf.write("oneswappins = ")
            outf.write(str(oneswappins))
            outf.write("\ntwoswappins = ")
            outf.write(str(twoswappins))
            outf.write("\nruntimeone = ")
            outf.write(str(runtimeone))
            outf.write("\nruntimetwo = ")
            outf.write(str(runtimetwo))


    while True:
         print ("Here is a list of modes available:")
         print ("1= Restart") #reboot for android
         print ("2 = Logoff") #disable for android
         print ("3 = Alternative Logoff Method ") #DISABLE
         print ("4 = Hibernate") #DISABLE
         print ("5= Shutdown") # shutdown -p?
         print ("6 = Alternative Shutdown Method") #Is there another way?
         print ("7 = Colour Flicker")#won't work on android
         print ("8 = Call CMD")#DISABLE
         print ("9 = Call Documents")#File Manager call?
         print ("10 = Call A Python Shell")#os.system("python")?
         print ("11 = Call Task Manager")#DISABLE
         print ("12 = Create folders in the same directory as this script.")
         print ("13 = Remove Directories")
         print ("14 = Create Files")
         print ("15 = Restart This Script (debug purposes)")
         print ("16 = Perform Operations With Numbers")
         print ("17 = Lock This Script")
         print ("18 = Call Auto-Clicker")#DISABLE
         print ("19 = Call Powershell")#DISABLE
         print ("20 = Exit")
         modewanted = int(input("Please enter the number of the mode that you want."))
         if modewanted == 1:
          shutdown = int(input("Please enter 1 or 0 to confirm restart."))
          local =time.asctime( time.localtime(time.time()) )
          with open("JT Tools Log File.txt", "a") as f: f.write(local)
          with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Restart (mode 1) entered.\n")
          if shutdown == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             os.system ("shutdown -r -f")
             os.system ("shutdown -l -f")
         elif modewanted == 2:
          logoff = int(input("Please enter 1 or 0 to confirm logoff."))
          if logoff == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             os.system ("shutdown -l -f")
         elif modewanted == 4:
          hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
          if hibernate == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             os.system ("shutdown -h -f")
         elif modewanted == 5:
          shutdown = int(input("Please enter 1 or 0 (no) to confirm shutdown."))
          if shutdown == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             os.system ("shutdown -s -f")
         elif modewanted == 7:
          suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
          if suretoflash == 1:
            howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
            currentflashes= int(0)                       
            while howlongtoflashfor != currentflashes:
             os.system ("color 4a")
             os.system ("color f9")
             currentflashes = currentflashes+1
         elif modewanted == 8:
            subprocess.call("cmd.exe")
         if modewanted == 20:
          print ("Closing!!!")
          closing = 5
          while closing !=6 and closing >0.015:
            closing = closing -0.017
            print ("Closing in",(round(closing, +3)),"seconds.")
            time.sleep (0.017)
          if closing == 0.002 or closing<0.002:
            exit(None)
         elif modewanted == 9:
            subprocess.call("explorer.exe")
         elif modewanted == 10:
           subprocess.call("python.exe")
         elif modewanted ==3:
          altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
          if altlogoff ==1:
            waittime =int(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
            time.sleep(waittime*60)
            subprocess.call ("logoff.exe")
         elif modewanted == 6:
          altshutdown =int(input("Please enter 1 or 0 to confirm shutdown."))
          if altshutdown ==1:
            waittime = int(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
            time.sleep (waittime*60)
            subprocess.call ("shutdown.exe")
         elif modewanted == 12:
           foldername = (str(input("Please input the name of your new folder.")))
           os.makedirs (foldername)
           cont = input("Success! Press any key then enter to continue...")
         elif modewanted == 15:
          confirmscriptrestart= int(input("Please input 1 to confirm restarting of this script."))
          if confirmscriptrestart == 1:
            subprocess.call("JT Tools.py",shell = True)
         elif modewanted == 16:
          print ("Here is a list of operations:")
          print ("1 =Add")
          print ("2 = Take")
          submode = int(input("Please enter the number of the operatino you wish to perform>"))
          if submode == 1 or 2:
            startnum = int(input("Please enter your starting number."))
            addortakenum = int(input("Please input the number to be added. If you wish to take a number please put a - and then the number you wish to be taken."))
            endnum=int(input("Please enter your end number."))
            waittime = int(input("How long do you wish to wait before each operation is performed?"))
            if endnum>startnum:
             while endnum>startnum:
                print(startnum)
                if addortakenum<int(0):
                    startnum = startnum-addortakenum
                if addortakenum>int(0):
                    startnum = startnum+addortakenum
                time.sleep(waittime)
             if startnum ==endnum or startnum>endnum:
                print("The closest number to your target number was:",startnum)
                time.sleep (1)
            elif startnum>endnum:
             while startnum>endnum:
                print (startnum)
                if addortakenum<0:
                    startnum = startnum+addortakenum
                if addortakenum>0:
                    startnum = startnum = startnum-addortakenum
                time.sleep (waittime)
             if startnum == endnum or startnum<endnum:
                print ("The closest number to your target end number was:",startnum)
                time.sleep (1)
         elif modewanted == 13:
           foldername = (str(input("Please input the name of the folder you wish to delete.")))
           os.rmdir (foldername)
           cont = input("Success! Press any key then enter to continue...")
         elif modewanted == 14:
            import io,time
            filename = (str(input("Please enter your file name plus the extension, eg. B.txt.  ")))
            with io.FileIO(filename, "w"):
              time.sleep (1)
         elif modewanted == 11:
           subprocess.call("taskmgr.exe")
         elif modewanted == 17:
             print ("Locked!!!")
         elif modewanted == 18:
          subprocess.call("\\Autoclicker.exe")
         elif modewanted == 19:
             subprocess.call("powershell.exe")
  
except():
    pass
