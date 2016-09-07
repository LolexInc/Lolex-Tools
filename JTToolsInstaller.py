import sys,time,subprocess,os,shutil,py_compile
sys.path.insert(0,"\\")
try:
 import isnottravisci
except(ImportError):
    print("Running as Travis CI...\nIf you aren't actually then create isnottravisci.py  to verify you aren't actually a bot.\nInstallation will commence upon the script restart and the file being present.")
    exit()
try:
    continueon = int(input("Please enter 1 to continue, or 0 to exit."))
    if continueon != 1:
        exit()
except(ValueError, TypeError, SyntaxError):
    exit()
print("Welcome to Lolex Tools Installer version 3.2.1.\nWhen FINAL CONFIRM appears, enter 3.\nNOTICE: all instructions must be followed carefully.\nAny crashes due to ignorance is not our fault.\nInstallation commencing...")
try:
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
        username2 = False
    if useusername == True:
        print("IF your script instance crashes in this bit, enclose your username in speech marks\nThis crash is known to happen on the Python 3.4.1 shell.")
        username1 = (str(input("Please set your username.")))
        repr(str(username1))
        confirm = (str(input("Please confirm your username.")))
        while username1 != confirm:
            username1 = (str(input("Your usernames didn't match. Please set your username.")))
            confirm = (str(input("Please confirm your username.")))
    onepins = int(input("How many PINs do you wish to use?\nUsing more than 1 will enable a swap PINs function.\nThis, upon each startup, will use your next PIN."))
    while onepins<0 or onepins>5:
        onepins = int(input("We only support between 0-5 PINs currently.\nHow many PINs do you wish to use?"))
    if onepins>1:
        oneswappins = True
    else:
        oneswappins = False
    if onepins == 0:
        oneusepin = False
    else:
        oneusepin = True
    if onepins>0:
        onepinone = int(input("Please set your first PIN."))
        confirm = int(input("Please confirm your first PIN."))
        while onepinone != confirm:
            onepinone = int(input("Sorry! Your PINs didn't match! Please set your first PIN."))
            confirm = int(input("Please confirm your first PIN."))
    if onepins>1:
        onepintwo = int(input("Please set your second PIN."))
        confirm = int(input("Please confirm your second PIN."))
        while onepintwo != confirm or onepintwo == onepinone:
            onepintwo = int(input("Sorry! Your PINs didn't match or they matched an earlier PIN! Please set your second PIN."))
            confirm = int(input("Please confirm your second PIN."))
    if onepins>2:
        onepinthree = int(input("Please set your third PIN."))
        confirm = int(input("Please confirm your third PIN."))
        while onepinthree != confirm or(onepinthree ==(onepintwo or onepinone)):
            onepinthree = int(input("Sorry! Your PINs didn't match or they matched an earlier PIN! Please set your third PIN."))
            confirm = int(input("Please confirm your third PIN."))
    if onepins>3:
        onepinfour = int(input("Please set your fourth PIN."))
        confirm = int(input("Please confirm your fourth PIN."))
        while onepinfour != confirm or (onepinfour == (onepinthree or onepintwo or onepinone)):
            onepinfour = int(input("Sorry! Your PINs didn't match or they matched an earlier PIN! Please set your fourth PIN."))
            confirm = int(input("Please confirm your fourth PIN."))
    if onepins>4:
        onepinfive = int(input("Please set your fifth PIN."))
        confirm = int(input("Please confirm your fifth PIN."))
        while onepinfive != confirm or (onepinfive == (onepinfour or onepinthree or onepintwo or onepinone)):
            onepinfive = int(input("Sorry! Your PINs didn't match or they matched an earlier PIN! Please set your fifth PIN."))
            confirm = int(input("Please confirm your fifth PIN."))
    if onepins == 0:
        onepinone = False
    if onepins == 0 or 1:
        onepintwo = False
    if onepins == 0 or 1 or 2:
        onepinthree = False
    if onepins == 0 or 1 or 2 or 3:
        onepinfour = False
    if onepins == 0 or 1 or 2 or 3 or 4:
        onepinfive = False
    if onepins>0:
        oneusepin = True
    if onepins>0:
     onewait = int(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed?"))
     while onewait<0:
        onewait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
    if howmanyunames>1:
        print("Setting up user 2...")
        username2 = (str(input("Please set your username.")))
    
        confirm = (str(input("Please confirm your username.")))
        while username2 != confirm or username2 == username1:
            username2 = (str(input("Sorry! Your usernames didn't match or is already in use!\nPlease set your username.")))
            confirm = (str(input("Please confirm your username.")))
        twopins = int(input("How many PINs do you wish to use?\nUsing more than 1 will enable a swap PINs function.\nThis, upon each startup, will use your next PIN."))
        while twopins<0 or twopins>5:
            twopins = int(input("We only support between 0-5 PINs currently.\nHow many PINs do you wish to use?"))
        if twopins>1:
            twoswappins = True
        else:
            twoswappins = False
        if twopins == 0:
            twousepin = False
        else:
            twousepin = True
        if twopins>0:
            twopinone = int(input("Please set your first PIN."))
            confirm = int(input("Please confirm your first PIN."))
            while twopinone != confirm:
                twopinone = int(input("Sorry! Your PINs didn't match! Please set your first PIN."))
                confirm = int(input("Please confirm your first PIN."))
        if twopins>1:
            twopintwo = int(input("Please set your second PIN."))
            confirm = int(input("Please confirm your second PIN."))
            while twopintwo != confirm or twopintwo == twopinone:
                twopintwo = int(input("Sorry! Your PINs didn't match! Please set your second PIN."))
                confirm = int(input("Please confirm your second PIN."))
        if twopins>2:
            twopinthree = int(input("Please set your third PIN."))
            confirm = int(input("Please confirm your third PIN."))
            while twopinthree != confirm or (twopinthree ==(twopintwo or twopinone)):
                twopinthree = int(input("Sorry! Your PINs didn't match! Please set your third PIN."))
                confirm = int(input("Please confirm your third PIN."))
        if twopins>3:
            twopinfour = int(input("Please set your fourth PIN."))
            confirm = int(input("Please confirm your fourth PIN."))
            while twopinfour != confirm or (twopinfour == (twopinthree or twopintwo or twopinone)):
                twopinfour = int(input("Sorry! Your PINs didn't match! Please set your fourth PIN."))
                confirm = int(input("Please confirm your fourth PIN."))
        if twopins>4:
            twopinfive = int(input("Please set your fifth PIN."))
            confirm = int(input("Please confirm your fifth PIN."))
            while twopinfive != confirm or (twopinfive == (twopinfour or twopinthree or twopintwo or twopinone)):
                twopinfive = int(input("Sorry! Your PINs didn't match! Please set your fifth PIN."))
                confirm = int(input("Please confirm your fifth PIN."))
        if twopins == 0:
            twopinone = False
        if twopins == 0 or 1:
            twopintwo = False
        if twopins == 0 or 1 or 2:
            twopinthree = False
        if twopins == 0 or 1 or 2 or 3:
            twopinfour = False
        if twopins == 0 or 1 or 2 or 3 or 4:
            twopinfive = False
        if twopins>0:
            twowait = int(input("If someone gets your PIN wrong 5 times, how long should the delay be before retries are allowed?"))
            while twowait<0:
                twowait = int(input("Less than 0 seconds is invalid. Please enter a valid number of seconds."))
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
        elif developer == 1:
             compiler = int(input("Please enter 1 if you want your options compiling, or 0 if you don't."))
             vanishprint = 0 #Feature for devs :)
        theme = (str(input("Here is a list of colours available: a - Neon Green, b - Light Blue, c - Neon Red, d - Light Purple/Pink, e - Neon Yellow, f - White, 1 - Dark Blue, 2 - Dark Green, 3 - Light Non-Neon Blue, 4 - Dark Red/Brown, 5 - Dark Purple, 6 - Non Neon Yellow, 7 - White/Light Gray, 8 - Dark Gray, 9 - Dark Neon Blue.The first colour will set the background colour, the second the text. Please enter color then your colour code.If any crashes occur try enclosing your colour code in speech marks.")))
        os.system(theme)             
             
    
                
except():
    pass
