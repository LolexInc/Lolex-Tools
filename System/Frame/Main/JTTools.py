import sys, time, subprocess, os
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
        print("WHOO! It worked!!!")
            
    
    
    
    
    
except():
    pass
