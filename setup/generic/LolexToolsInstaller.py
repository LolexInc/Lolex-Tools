#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
## 
## authors = Monkeyboy2805
import sys, time, os, shutil, platform, py_compile
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
        IOError = OSError
syslen = len(sys.path)
sys.path.insert(0, "./")
import requiredpatches
print("Importing...")
sys.path.insert(0, "./lib/")
try:
        import LolexToolsMethods
except(ImportError) as e:
        print(e)
        print("Missing or corrupted library. Please redownload this application or make an issue if this persists.")
        time.sleep(5)
        exit(0)
print("This installer uses the following modules: sys, time, os, shutil, platform, LolexToolsMethods")
if sys.version_info.major != 3:
        print("Only Python 3 is currently supported. Please install Python 3.")
        time.sleep(5)
        exit(0)
try:
        continueon = int(input("Please enter 1 to continue, or 0 to exit."))
        if continueon != 1:
                exit(0)
except(ValueError, TypeError, SyntaxError):
        exit(0)
print("Welcome to Lolex-Tools Installer version 3.2.1.\nNOTICE: all instructions must be followed carefully.\nAny crashes due to ignorance is not our fault.\nInstallation commencing...")
try:
        print("Resetting...This process could take a couple of minutes.")
        try:
                os.remove("./LolexToolsOptions.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./verifonboot.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./startplugins.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./theme.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./runningsys.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./patches.py")
        except(IOError, OSError):
                pass
        try:
                os.remove("./lang.py")
        except(IOError, OSError):
                pass
        class settings:
                directories = os.listdir("./")
                arraypos = 0
        while settings.arraypos < len(settings.directories):
                if settings.directories[settings.arraypos].endswith("settings.py"):
                        try:
                                os.remove("./" + settings.directories[settings.arraypos])
                        except(IOError, OSError):
                                pass
                settings.arraypos = settings.arraypos + 1
        try:
                os.remove("./madeon.py")
        except(IOError, OSError):
                pass
        with open("./LolexToolsOptions.py", "w+") as outf:
                outf.truncate()
                a = input("STAGE 1")
        useros = platform.system()
        #if useros == "Linux":
                #print("This project requires Git for updating. Installing git...")
                #os.system("apt install git")
        howmanyunames = int(input("Please enter the number of usernames you wish to use."))
        while howmanyunames < 0 or howmanyunames > 2:
                print("Sorry! We only support 0 - 2 usernames currently.")
                howmanyunames = int(input("Please enter the number of usernames you wish to use."))
        if howmanyunames == 0:
                useusername = False
                username1 = False
        else:
                useusername = True
        if howmanyunames == 0 or howmanyunames == 1:
                username2 = "aFalse"
                twoswappins = False
                twousepin = False
                twouseword = False
                twowait = 0
                twowords = 0
                twowordwait = 0
        if useusername == True:
                username1 = input("Please set your username.")
                confirm = input("Please confirm your username.")
                while username1 != confirm:
                        username1 = input("Your usernames didn't match. Please set your username.")
                        confirm = input("Please confirm your username.")
        onepins = int(input("How many PINs do you wish to use?\nUsing more than 1 will enable a swap PINs function.\nThis, upon each startup, will use your next PIN."))
        if onepins == 0:
                onepintotal = 0
        else:
                onepintotal = 1
        done = 1
        while onepintotal < onepins + 1 and onepins != 0 and done != 0:
                onepin = int(input("Please set your PIN."))
                confirm = int(input("Please confirm your PIN."))
                while onepin != confirm:
                        onepin = int(input("Please set your PIN so it matches."))
                        confirm = int(input("Please confirm your PIN."))
                        with open ("./LolexToolsOptions.py", "a") as outf:
                                outf.write("\nonepin")
                                outf.write(str(onepintotal))
                                outf.write(" = ")
                                outf.write(str(onepin))
                                if onepintotal != onepins:
                                        onepintotal = onepintotal + 1
                                else:
                                        done = 0
        with open ("./LolexToolsOptions.py", "a") as outf:
                outf.write("\nonepintotal = ")
                outf.write(str(onepintotal))
                b = input("STAGE 2")
        if onepins == 0:
                onewait = False
        if onepins > 0:
                oneusepin = True
        else:
                oneusepin = False
        if onepins > 1:
                oneswappins = True
        else:
                oneswappins = False
        if onepins > 0:
                onewait = float(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
                while onewait < 0 or onewait > 4194304:
                        onewait = float(input("Less than 0 or more than 4194304 seconds is invalid. Please enter a valid number of seconds."))
        onewords = int(input("How many passwords do you wish to use?\nUsing more than 1 will enable a swap passwords function.\nThis, upon each startup, will use your next password."))
        if onewords == 0:
                onewordtotal = 0
        else:
                onewordtotal = 1
        done = 1
        while onewordtotal < onewords + 1 and onewords != 0 and done != 0:
                oneword = input("Please set your password.")
                confirm = input("Please confirm your password.")
                while oneword != confirm:
                        oneword = input("Please set your password so it matches.")
                        confirm = input("Please confirm your password.")
                with open ("./LolexToolsOptions.py", "a") as outf:
                        outf.write("\noneword")
                        outf.write(str(onewordtotal))
                        outf.write(" = ")
                        outf.write('"')
                        outf.write(str(oneword))
                        outf.write('"')
                        if onewordtotal != onewords:
                                onewordtotal = onewordtotal + 1
                        else:
                                done = 0
                        c= input("STAGE 3")
        with open ("./LolexToolsOptions.py", "a") as outf:
                outf.write("\nonewordtotal = ")
                outf.write(str(onewordtotal))
                d = input("STAGE 4")
        if onewords == 0:
                onewordwait = False
        if onewords > 0:
                oneuseword = True
        else:
                oneuseword = False
        if onewords > 1:
                oneswapwords = True
        else:
                oneswapwords = False
        if onewords > 0:
                oneuseword = True
                onewordwait = float(input("If someone gets your password wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
                while onewordwait < 0 or onewordwait > 4194304:
                        onewordwait = float(input("Less than 0 or more than 4194304 seconds is invalid. Please enter a valid number of seconds."))
        if howmanyunames > 1:
                print("Setting up user 2...")
                username2 = input("Please set your username.")
                confirm = input("Please confirm your username.")
                while username2 != confirm or username2 == username1:
                        username2 = input("Sorry! Your usernames didn't match or is already in use!\nPlease set your username.")
                        confirm = input("Please confirm your username.")
                twopins = int(input("How many PINs do you wish to use?\nUsing more than 1 will enable a swap PINs function.\nThis, upon each startup, will use your next PIN."))
                if twopins == 0:
                        twopintotal = 0
                else:
                        twopintotal = 1
                done = 1
                while twopintotal < twopins + 1 and twopins != 0 and done != 0:
                        twopin = int(input("Please set your PIN."))
                        confirm = int(input("Please confirm your PIN."))
                        while twopin != confirm:
                                twopin = int(input("Please set your PIN so it matches."))
                                confirm = int(input("Please confirm your PIN."))
                                with open ("./LolexToolsOptions.py","a") as outf:
                                        e = input("STAGE 5")
                                        outf.write("\ntwopin")
                                        outf.write(str(twopintotal))
                                        outf.write(" = ")
                                        outf.write(str(twopin))
                                        if twopintotal != twopins:
                                                twopintotal = twopintotal + 1
                                        else:
                                                done = 0
                with open ("./LolexToolsOptions.py", "a") as outf:
                        outf.write("\ntwopintotal = ")
                        outf.write(str(twopintotal))
                        f = input("STAGE 6")
                if twopins == 0:
                        twowait = False
                        twousepin = False
                if twopins > 0:
                        twousepin = True
                if twopins > 1:
                        twoswappins = True
                else:
                        twoswappins = False
                if twopins > 0:
                        twowait = float(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
                        while twowait < 0 or twowait > 4194304:
                                twowait = float(input("Less than 0 or bigger than 4194304 seconds is invalid. Please enter a valid number of seconds."))
                twowords = int(input("How many passwords do you wish to use?\nUsing more than 1 will enable a swap passwords function.\nThis, upon each startup, will use your next password."))
                if twowords == 0:
                        twowordtotal = 0
                else:
                        twowordtotal = 1
                done = 1
                while twowordtotal < twowords + 1 and twowords != 0 and done != 0:
                        twoword = input("Please set your password.")
                        confirm = input("Please confirm your password.")
                        while twoword != confirm:
                                twoword = input("Please set your password so it matches.")
                                confirm = input("Please confirm your password.")
                                with open ("./LolexToolsOptions.py", "a") as outf:
                                        g = input("STAGE 7")
                                        outf.write("\ntwoword")
                                        outf.write(str(twowordtotal))
                                        outf.write(" = ")
                                        outf.write('"')
                                        outf.write(str(twoword))
                                        outf.write('"')
                                        if twowordtotal != twowords:
                                                twowordtotal = twowordtotal + 1
                                        else:
                                                done = 0
                with open ("./LolexToolsOptions.py","a") as outf:
                        outf.write("\ntwowordtotal = ")
                        outf.write(str(twowordtotal))
                        h = input("STAGE 8")
                if twowords == 0:
                        twouseword = False
                else:
                        twouseword = True
                if twowords > 1:
                        twoswapwords = True
                else:
                        twoswapwords = False
                if twowords == 0:
                        twowordwait = False
                if twowords > 0:
                        twouseword = True
                        twowordwait = float(input("If someone gets your password wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
                        while twowordwait < 0 or twowordwait > 4194304:
                                twowordwait = float(input("Less than 0 or bigger than 4194304 seconds is invalid. Please enter a valid number of seconds."))
        else:
                with open ("./LolexToolsOptions.py", "a") as outf: outf.write("\ntwopintotal = 0\ntwowordtotal = 0")
                i = input("STAGE 9")
        print("Setting up general options...")
        developer = int(input("Please enter 1 if either of the users are planning to be a developer of this project, or 0 if not."))
        if developer == 1:
                print("WELCOME developer!")
        if useros == "Windows":
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
                print("The first colour will set the background colour, the second the text. Please enter your colour code.")
                theme = "color " + input("Please set your theme.")
                os.system(theme)
        else:
                theme = "cd ./"
        pluginconfirm = int(input("Do you wish to use plugins? Please enter 1 to use them, or 0 to not.\nPlease ensure that your plugins are downloaded and ready for use.\nNOTE:This is HIGHLY EXPERIMENTAL!."))
        if pluginconfirm == 1:
                LolexToolsMethods.addplugins(True)
        else:
                a = open("./startplugins.py", "w+")
                a.truncate()
                a.write("import sys\nsys.path.insert(0, './lib')\nfrom LolexToolsMethods import *")
                a.close()
                compileplugins = 0
        if developer == 1:
                developer = True
        else:
                developer = False
        if twowords < 2:
                twoswapwords = False
        b = open("./theme.py", "w+")
        b.truncate()
        print("Writing theme...", theme)
        b.write('theme = ("')
        b.write(str(theme))
        b.write('")')
        b.close()
        print("OK. Reset completed with a 1.")
        print("Applying new options...")
        c = open("./verifonboot.py", "w+")
        c.truncate()
        c.write("\noneswappins = ")
        c.write(str(oneswappins))
        c.write("\noneswapwords = ")
        c.write(str(oneswapwords))
        c.write("\ntwoswappins = ")
        c.write((str(twoswappins)))
        twoswappins = 0
        c.write("\nruntimeone = 0\nruntimetwo = 0")
        c.write("\ntwoswapwords = ")
        c.write((str(twoswapwords)))
        twoswapwords = 0
        c.write("\nwordtimeone = 0\nwordtimetwo = 0")
        c.close()
        d = open("./LolexToolsOptions.py", "a")
        d.write("\ncompiledon = 10.0") # See if I can get rid of this thing at some point
        d.write("\nuseusername = ")
        d.write(str(useusername))
        useusername = 0
        d.write("\nusername1 = ")
        if username1 == False:
                d.write(str(username1))
        else:
                d.write('("')
                d.write(username1)
                d.write('")')
        username1 = 0
        d.write("\nusername2 = ")
        d.write('("')
        d.write(username2)
        d.write('")')
        username2 = 0
        d.write("\noneusepin = ")
        d.write(str(oneusepin))
        oneusepin = 0
        d.write("\ntwousepin = ")
        d.write(str(twousepin))
        twousepin = 0
        d.write("\noneuseword = ")
        d.write(str(oneuseword))
        oneuseword = 0
        d.write("\ntwouseword = ")
        d.write(str(twouseword))
        twouseword = 0
        d.write("\nonewordwait = ")
        d.write(str(onewordwait))
        onewordwait = "None"
        d.write("\ntwowordwait = ")
        d.write(str(twowordwait))
        twowordwait = "None"
        d.write("\ndeveloper = ")
        d.write(str(developer))
        developer = "None"
        compileplugins = "None"
        d.write("\nonewait = ")
        d.write(str(onewait))
        onewait = "None"
        d.write("\ntwowait = ")
        d.write(str(twowait))
        d.close()
        twowait = "None"
        confirm = "None"
        end = input("END")
        with open ("./patches.py", "a") as outf:
                outf.write('applied = ""')
                #outf.write(str(requiredpatches.patches))
        with open ("./runningsys.py", "a") as outf:
                outf.write("system = " + '("' + useros + '")')
        with open ("./menusettings.py", "a") as outf:
                outf.write("layout = 0")
        if useros == "Linux":
                theme = "cd ./"
        with open ("./lang.py", "a") as outf: outf.write("import sys\nsys.path.insert(0, './strings/')\nimport enUK as strings")
        default_settings = ["./restartsettings.py", "./logoffsettings.py", "./hibernatesettings.py", "./shutdownsettings.py", "./exitsettings.py", "./foldercreatesettings.py", "./exfoldersettings.py", "./addfilesettings.py", "./scriptloopsettings.py", "./mathmodesettings.py", "./scriptlocksettings.py"]
        for i in range(0, len(default_settings) - 1):
                with open(default_settings[i], "w+") as outf:
                        outf.truncate()
                        outf.write("hidden = False")
##        with open ("./restartsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./logoffsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./hibernatesettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./shutdownsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./exitsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./pyshellsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./foldercreatesettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./exfoldersettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./addfilesettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./scriptloopsettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./mathmodesettings.py","a") as outf: outf.write("hidden = False")
##        with open ("./scriptlocksettings.py","a") as outf: outf.write("hidden = False")
        with open ("./madeon.py","a") as outf: outf.write("compiledon = 9.00101")
        try:
                start = int(input("Do you wish to start Lolex-Tools now? Please enter 1 if you do, or 0 if you don't."))
                print("Thank you for using Lolex-Tools Installer.")
                if start == 1:
                        print("Starting Lolex-Tools...")
                        os.system(LolexToolsMethods.py + "main" + LolexToolsMethods.s + "LolexTools.py")
                exit(0)
        except(TypeError, SyntaxError, ValueError):
                print("Failed to start.")
except(SyntaxError) as a:
        print("Sorry! A SyntaxError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(a)
        time.sleep(10)
except(TypeError) as b:
        print("Sorry! A TypeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(b)
        time.sleep(10)
except(ValueError) as c:
        print("Sorry! A ValueError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(c)
        time.sleep(10)
except(IOError) as d:
        print("Sorry! A IOError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(d)
        time.sleep(10)
except(NameError) as e:
        print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(e)
        time.sleep(10)
except(EOFError) as f:
        print("Sorry! A EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(f)
        time.sleep(10)
except(AttributeError) as g:
        print("Sorry! A AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(g)
        time.sleep(10)
except(OSError) as h:
        print("Sorry! A OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
        print(h)
        time.sleep(10)
