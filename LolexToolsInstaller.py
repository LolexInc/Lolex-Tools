#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
## 
## authors = Monkeyboy2805
import sys, time, os, shutil, platform, LolexToolsMethods
print("This installer uses the following modules:sys, time, os, shutil, platform, LolexToolsMethods")
if sys.version_info.major !=3:
     print("Only Python 3 is currently supported. Please install Python 3.")
     os.system("python3 LolexToolsInstaller.py")
     exit(None)
try:
     continueon = int(input("Please enter 1 to continue, or 0 to exit."))
     if continueon != 1:
              exit(None)
except(ValueError, TypeError, SyntaxError):
     exit(None)
print("Welcome to Lolex-Tools Installer version 3.2.1.\nWhen FINAL CONFIRM appears, enter 3.\nNOTICE: all instructions must be followed carefully.\nAny crashes due to ignorance is not our fault.\nInstallation commencing...")
try:
     print("Resetting...This process could take a couple of minutes.")
     try:
            os.remove("./LolexToolsOptions.pyc")
     except(IOError, OSError):
              pass
     try:
            os.remove("./LolexToolsOptions.py")
     except(IOError, OSError):
              pass
     try:
            os.remove("./verifonboot.pyc")
     except(IOError, OSError):
              pass
     try:
            os.remove("./verifonboot.py")
     except(IOError, OSError):
              pass
     try:
            os.remove("./startplugins.pyc")
     except(IOError, OSError):
              pass
     try:
            os.remove("./startplugins.py")
     except(IOError, OSError):
              pass
     try:
              os.remove("./theme.pyc")
     except(IOError, OSError):
              pass
     try:
              os.remove("./theme.py")
     except(IOError, OSError):
              pass
     try:
              os.remove("./runningsys.pyc")
     except(IOError, OSError):
              pass
     try:
              os.remove("./runningsys.py")
     except(IOError, OSError):
              pass
     class settings:
      	dir = os.listdir("./")
      	file = ""
     for settings.file in settings.dir:
     	if settings.file.endswith("settings.py") or settings.file.endswith("settings.pyc"):
     		try:
     			os.remove(os.path.join(settings.dir, settings.file))
     		except(IOError, OSError):
     			pass
     try:
          os.remove("./madeon.py")
     except(IOError, OSError):
          pass
     useros = platform.system()
     if useros == "Linux":
              print("This project requires Git for updating. Installing git...")
              os.system("apt install git")
     if useros != "Windows":
              plat = int(input("Please enter 1 if you are using Android, or 0 for other."))
              if plat == 1:
                      useros = "Android"
     howmanyunames = int(input("Please enter the number of usernames you wish to use."))
     while howmanyunames<0 or howmanyunames>2:
              print("Sorry! We only support 0 - 2 usernames currently.")
              howmanyunames = int(input("Please enter the number of usernames you wish to use."))
     if howmanyunames == 0:
              useusername = False
              username1 = False
     else:
              useusername = True
     if howmanyunames == 0 or 1:
              username2 = "aFalse"
              twoswappins = False
              twousepin = False
              twouseword = False
              twowait = 0
              twowords = 0
              twowordwait = 0
     if useusername == True:
              print("If your script instance crashes in this bit, enclose your username in speech marks\nThis crash is known to happen on the Python 3.4.1 shell.")
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
              with open ("./LolexToolsOptions.py","a") as outf:
                       outf.write("\nonepin")
                       outf.write(str(onepintotal))
                       outf.write(" = ")
                       outf.write(str(onepin))
                       if onepintotal != onepins:
                                    onepintotal = onepintotal + 1
                       else:
                                    done = 0
     with open ("./LolexToolsOptions.py","a") as outf:
              outf.write("\nonepintotal = ")
              outf.write(str(onepintotal))
     if onepins == 0:
              onewait = False
     if onepins>0:
              oneusepin = True
     else:
              oneusepin = False
     if onepins>1:
              oneswappins = True
     else:
              oneswappins = False
     if onepins>0:
              onewait = int(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
              while onewait<0:
                       onewait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
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
              with open ("./LolexToolsOptions.py","a") as outf:
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
     with open ("./LolexToolsOptions.py","a") as outf:
              outf.write("\nonewordtotal = ")
              outf.write(str(onewordtotal))
     if onewords == 0:
              onewordwait = False
     if onewords>0:
              oneuseword = True
     else:
              oneuseword = False
     if onewords>1:
              oneswapwords = True
     else:
              oneswapwords = False
     if onewords == 0:
              onewordwait = False
     if onewords>0:
              oneuseword = True
     if onewords>0:
              onewordwait = int(input("If someone gets your password wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
              while onewordwait<0:
                       onewordwait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
     if howmanyunames>1:
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
                                    outf.write("\ntwopin")
                                    outf.write(str(twopintotal))
                                    outf.write(" = ")
                                    outf.write(str(twopin))
                                    if twopintotal != twopins:
                                             twopintotal = twopintotal + 1
                                    else:
                                             done = 0
              with open ("./LolexToolsOptions.py","a") as outf:
                       outf.write("\ntwopintotal = ")
                       outf.write(str(twopintotal))
              if twopins == 0:
                       twowait = False
              if onepins>0:
                       twousepin = True
              else:
                       twousepin = False
              if twopins>1:
                       twoswappins = True
              else:
                       twoswappins = False
              twowait = int(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
              while twowait<0:
                       twowait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
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
                       with open ("./LolexToolsOptions.py","a") as outf:
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
              if twowords == 0:
                       twowordwait = False
              if twowords>0:
                       twouseword = True
              else:
                       twouseword = False
              if twowords>1:
                       twoswapwords = True
              else:
                       twoswapwords = False
              if twowords == 0:
                       twowordwait = False
              if twowords>0:
                       twouseword = True
              if twowords>0:
                       twowordwait = int(input("If someone gets your password wrong 5 times, how long should the delay be before retries are allowed, in seconds?"))
                       while twowordwait<0:
                                    twowordwait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
     else:
          with open ("./LolexToolsOptions.py", "a") as outf: outf.write("\ntwopintotal = 0\ntwowordtotal = 0")
     print("Setting up general options...")
     developer = int(input("Please enter 1 if either of the users are planning to be a developer of this project, or 0 if not."))
     if (oneusepin == True or 1) or (twousepin == True or 1):
              if developer !=1:
                       vanishprint = int(input("How many lines do you wish to be printed to hide your PIN (as a number)?"))
                       confirm = 0
                       while vanishprint<500 and confirm!=1:
                                    confirm = int(input("SECURITY WARNING: this number may not be secure. Please enter 0 to change it, or 1 to confirm it.\nPlease be aware that less than 0 lines is invalid."))
                                    if confirm != 1 or vanishprint<0:
                                             vanishprint = int(input("Please enter a valid number of lines."))
                       compiler = True
              elif developer == 1:
                       compiler = int(input("Please enter 1 if you want your options compiling, or 0 if you don't."))
                       vanishprint = 0 #Feature for devs :)
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
                       print("The first colour will set the background colour, the second the text. Please enter color then your colour code.")
                       print("If any crashes occur try enclosing your colour code in speech marks.")
                       theme = input("Please set your theme.")
                       os.system(theme)
     pluginconfirm = int(input("Do you wish to use plugins? Please enter 1 to use them, or 0 to not.\nPlease ensure that your plugins are downloaded and ready for use.\nNOTE:This is HIGHLY EXPERIMENTAL!."))
     if pluginconfirm == 1:
                       currentplugin = (str(input("Please enter the name of your first plugin. Do not include file extensions! Plugin names also have to be case- sensitive, cannot be any types of numbers, cannot have spaces or special characters like commas.")))
                       with open ("./startplugins.py","a") as outf:outf.write(str("\nimport "+(str(currentplugin))))
                       done = int(input("Please enter 1 if you are done, 0 if you aren't."))
                       while done != 1:
                                    currentplugin = input("Please enter the name of your next plugin.")
                                    with open ("./startplugins.py","a") as outf: outf.write(str("\nimport "+(str(currentplugin))))
                                    done = int(input("Please enter 1 if you are done, 0 if you aren't."))
                       if developer == 1:
                                    compileplugins = int(input("Please enter 1 if you want your plugins compiling, or 0 if you don't."))
                       else:
                                    compileplugins = 1
     elif pluginconfirm != 1:
              compileplugins = 0
              with open ("./startplugins.py", "a") as outf: pass
     if developer == 1:
              developer = True
     else:
              developer = False
     if compiler == 1:
              compiler = True
     else:
              compiler = False
     if twowords<2:
              twoswapwords = False
     with open("./theme.py","a") as outf:
              print("Writing theme...", theme)
              outf.write('theme = ("')
              outf.write(str(theme))
              outf.write('")')
     print("OK. Reset completed with a 1.")
     print("Applying new options...")
     with open ("verifonboot.py","a") as outf:
              outf.write("\noneswappins = ")
              outf.write(str(oneswappins))
              outf.write("\noneswapwords = ")
              outf.write(str(oneswapwords))
              outf.write("\ntwoswappins = ")
              outf.write((str(twoswappins)))
              twoswappins = 0
              outf.write("\nruntimeone = 0\nruntimetwo = 0")
              outf.write("\ntwoswapwords = ")
              outf.write((str(twoswapwords)))
              twoswapwords = 0
              outf.write("\nwordtimeone = 0\nwordtimetwo = 0")
     with open ("LolexToolsOptions.py","a") as outf:
              outf.write("\ncompiledon = 9.001")
              outf.write("\nuseusername = ")
              outf.write(str(useusername))
              useusername = 0
              outf.write("\nusername1 = ")
              if username1 == False:
                       outf.write(str(username1))
              else:
                       outf.write('("')
                       outf.write(username1)
                       outf.write('")')
              username1 = 0
              outf.write("\nusername2 = ")
              outf.write('("')
              outf.write(username2)
              outf.write('")')
              username2 = 0
              outf.write("\noneusepin = ")
              outf.write(str(oneusepin))
              oneusepin = 0
              outf.write("\ntwousepin = ")
              outf.write(str(twousepin))
              twousepin = 0
              outf.write("\noneuseword = ")
              outf.write(str(oneuseword))
              oneuseword = 0
              outf.write("\ntwouseword = ")
              outf.write(str(twouseword))
              twouseword = 0
              outf.write("\nonewordwait = ")
              outf.write(str(onewordwait))
              onewordwait = "None"
              outf.write("\ntwowordwait = ")
              outf.write(str(twowordwait))
              twowordwait = "None"
              outf.write("\ndeveloper = ")
              outf.write(str(developer))
              developer = "None"
              outf.write("\nvanishprint = ")
              outf.write(str(vanishprint))
              vanishprint = "None"
              outf.write("\ncompiler = ")
              outf.write(str(compiler))
              compiler = "None"
              outf.write("\ncompileplugins = ")
              outf.write(str(compileplugins))
              compileplugins = "None"
              outf.write("\nonewait = ")
              outf.write(str(onewait))
              onewait = "None"
              outf.write("\ntwowait = ")
              outf.write(str(twowait))
              twowait = "None"
              confirm = "None"
     with open ("./patches.py", "a") as outf: outf.write('applied = "9.0nann4"')
     with open ("./runningsys.py","a") as outf:
              outf.write("system = " + '("' + useros + '")')
     with open ("./menusettings.py","a") as outf:
              outf.write("layout = 0")
     if useros == "Linux":
              theme = "cd ./"
     if compiler == 0 or False:
              pass
     elif compiler == 1 or compiler == True:
             LolexToolsMethods.compiler("verifonboot")
             LolexToolsMethods.compiler("LolexToolsOptions")
             LolexToolsMethods.compiler("runningsys")
             LolexToolsMethods.compiler("theme")
     if compileplugins == 1 or compileplugins == True:
              LolexToolsMethods.compiler("startplugins")
     LolexToolsMethods = False
     with open ("./restartsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./logoffsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./hibernatesettings.py","a") as outf: outf.write("hidden = False")
     with open ("./shutdownsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./exitsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./pyshellsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./foldercreatesettings.py","a") as outf: outf.write("hidden = False")
     with open ("./exfoldersettings.py","a") as outf: outf.write("hidden = False")
     with open ("./addfilesettings.py","a") as outf: outf.write("hidden = False")
     with open ("./scriptloopsettings.py","a") as outf: outf.write("hidden = False")
     with open ("./mathmodesettings.py","a") as outf: outf.write("hidden = False")
     with open ("./scriptlocksettings.py","a") as outf: outf.write("hidden = False")
     with open ("./madeon.py","a") as outf: outf.write("compiledon = 9.00001")
     try:
              start = int(input("Do you wish to start Lolex-Tools now? Please enter 1 if you do, or 0 if you don't."))
              print("Thank you for using Lolex-Tools Installer.")
              if start == 1:
                       print("Starting Lolex-Tools...")
                       if useros == "Linux" or useros == "Android":
                               os.system("python3 ./LolexTools.py")
                       else:
                               if sys.version_info.minor>5:
                                       os.system("py .\LolexTools.py")
                               else:
                                       os.system("python .\LolexTools.py")
              exit(None)
     except(TypeError, SyntaxError, ValueError):
              print("Failed to start.")
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
     print("Sorry! A IOError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(NameError):
     print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(EOFError):
     print("Sorry! A EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(AttributeError):
     print("Sorry! A AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
except(OSError):
     print("Sorry! A OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
     time.sleep(10)
