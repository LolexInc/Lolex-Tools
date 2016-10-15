import sys, time, subprocess, os, shutil, py_compile
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
        except(IOError):
            try:
                os.remove("/Lolex Tools/User/Data/verifoboot.pyc")
            except(IOError):
                pass
        try:
            shutil.copy("/Lolex Tools/Defaults/verifonboot.py","/Lolex Tools/User/Data/verifonboot.py")
        except(IOError):
            print("Please do not remove system files. Please redownload the repository from https://github.com/LolexOrg/Lolex-Tools/tree/Internal-Beta and relaunch this.")
            time.sleep(5)
        with open ("/Lolex Tools/User/Data/verifonboot.py","a") as outf:
            outf.write("oneswappins = ")
            outf.write(str(oneswappins))
            outf.write("\ntwoswappins = ")
            outf.write(str(twoswappins))
            outf.write("\nruntimeone = ")
            outf.write(str(runtimeone))
            outf.write("\nruntimetwo = ")
            outf.write(str(runtimetwo))
        if JTToolsOptions.compiler == True:
            try:
                py_compile.compile("/Lolex Tools/User/Data/verifonboot.py")
                try:
                    os.remove("/Lolex Tools/User/Data/verifonboot.py")
                except(IOError, WindowsError):
                    pass
            except(IOError, SyntaxError):
                pass
            try:
                shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-36.pyc","/Lolex Tools/User/Data")
                os.rename("/Lolex Tools/User/Data/verifonboot.cpython-36.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
            except(IOError):
                try:
                    shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-35.pyc","/Lolex Tools/User/Data")
                    os.rename("/Lolex Tools/User/Data/verifonboot.cpython-35.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                except(IOError):
                    try:
                        shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-34.pyc","/Lolex Tools/User/Data")
                        os.rename("/Lolex Tools/User/Data/verifonboot.cpython-34.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                    except(IOError):
                        try:
                            shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-33.pyc","/Lolex Tools/User/Data")
                            os.rename("/Lolex Tools/User/Data/verifonboot.cpython-33.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                        except(IOError):
                            try:

                                shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-32.pyc","/Lolex Tools/User/Data")
                                os.rename("/Lolex Tools/User/Data/verifonboot.cpython-32.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                            except(IOError):
                                try:
                                    shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-31.pyc","/Lolex Tools/User/Data")
                                    os.rename("/Lolex Tools/User/Data/verifonboot.cpython-31.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                                except(IOError):
                                    try:
                                        shutil.copy("/Lolex Tools/User/Data/__pycache__/verifonboot.cpython-30.pyc","/Lolex Tools/User/Data")
                                        os.rename("/Lolex Tools/User/Data/verifonboot.cpython-30.pyc","/Lolex Tools/User/Data/verifonboot.pyc")
                                    except(IOError):
                                        print("Sorry! It appears you are not running Python 3.0 - 3.6 nightly. Python 2 is NOT supported.")
                                        time.sleep(3)
                                        exit()
    while True:
        modewanted = 10
        while modewanted == 5 or 10:
            if modewanted == 10:
                print("1 = ")
                print("2 = ")
                print("3 = ")
                print("4 = ")
                print("5 = Next Page")
            elif modewanted == 5:
                print("6 = ")
                print("7 = ")
                print("8 = ")
                print("9 = ")
                print("10 = Previous Page")
            modewanted = int(input("Please enter the number of the mode you want."))
						
					
            
    
    
    
    
    
except():
    pass
