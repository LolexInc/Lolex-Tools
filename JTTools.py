import sys, time, subprocess, os, shutil
sys.path.insert(0,"\\")
try:
    import isnottravisci
except(ImportError):
    print("Running as Travis CI...\nIf you are human please create isnottravisci.py to continue.")
    time.sleep(10)
    exit()
try:
    sys.path.insert(0,"/Lolex Tools/User/Data/")
    import JTToolsOptions
except(ImportError):
    print("Starting installer due to missing options file...")
    sys.path.insert(0,"/Lolex Tools/System")
    subprocess.call("JTToolsInstaller.py", shell = True)
try:
    sys.path.insert(0,"/Lolex Tools/System/Lib")
    import JTToolsMethods
except(ImportError):
    print("Missing library. Please redownload this application.")
    time.sleep(10)
    exit()
try:
    sys.path.insert(0,"/Lolex Tools/User/Data")
    import theme
except(ImportError):
    pass
try:
    import verifonboot
except(ImportError):
    print("Starting installer due to missing data file...")
    sys.path.insert(0,"/Lolex Tools/System")
    subprocess.call("JTToolsInstaller.py", shell = True)
try:
    sys.path.insert(0,"/Lolex Tools/User/Data")
    import startplugins
except(ImportError, ValueError, SyntaxError, TypeError, OSError, NameError):
    print("Starting installer due to missing data file...")
    sys.path.insert(0,"/Lolex Tools/System")
    subprocess.call("JTToolsInstaller.py", shell = True)
print("Welcome to Lolex Tools version 8.002")
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
            sys.path.insert(0,"\\")
            os.remove("/Lolex Tools/User/Data/verifonboot.py")
        except():
            try:
                os.remove("/Lolex Tools/User/Data/verifoboot.pyc")
            except():
                pass
        try:
            shutil.copy("/Lolex Tools/Defaults/verifonboot.py","/Lolex Tools/User/Data/verifonboot.py")
        except():
            pass
						
					
            
    
    
    
    
    
except():
    pass
