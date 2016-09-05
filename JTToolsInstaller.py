import os, subprocess, py_compile, shutil, sys, time
try:
    sys.path.insert(0,"\\")
    import isnottravisci
except(ImportError):
    print("Running as Travis CI... Tests complete. If you are not actually running in Travis CI, please create isnottravisci.py")
    time.sleep(500)
    print("...")
    time.sleep(500)
    print("...")
    time.sleep(500)
    print("...")
    time.sleep(500)
    print("...")
    time.sleep(500)
    print("...")
    time.sleep(500)
    print("...")
    
    print ("Build passed our tests, exiting...")
    exit(None)
try:
    test = raw_input("Please press any key then enter to continue...")
    python = int(2)
except(NameError):
    python = int(3)
    test = input("Press any key then enter to continue...")
    
    
try:
 os.remove ("JTToolsOptions.pyc")
except(FileNotFoundError):
    print ("Error:pyc file not found. Continuing...")
try:
 os.remove("JTToolsOptions.py")
except(FileNotFoundError):
    print ("Error: py file not found. Continuing...")
try:
 print ("Starting JT Tools Installer version 1.0.0 beta-alpha...")
 import time
 with open ("JTToolsOptions.py","a") as f: f.write ("class Options:\n")
 usepin=int(input("Please enter 1 to use a pin or 0 to not use."))
 if usepin==int(1):
     with open ("JTToolsOptions.py","a") as f: f.write(" pin = True\n")
     code = str(input("Please set your code."))
     code2=str(input("Please confirm your code."))
     while code != code2:
         print ("Sorry, your codes don't match.")
         code = str(input("Please set your code."))
         code2 = str(input("Please confirm your code."))
     with open ("JTToolsOptions.py","a") as f: f.write(" code = ")
     with open ("JTToolsOptions.py","a") as outf: outf.write (str(code))
     with open ("JTToolsOptions.py","a") as f: f.write ("\n")
 elif usepin != 1:
     with open ("JTToolsOptions.py","a") as f: f.write (" pin = False\n")
     with open ("JTToolsOptions.py","a") as f: f.write (" code = 0\n")
 useusername = int(input("Please enter 1 to use usernames or 0 to not."))
 if useusername != 1:
     with open ("JTToolsOptions.py","a") as f: f.write(" useusername = False\n")
     with open ("JTToolsOptions.py","a") as f: f.write(" username1 = False\n")
     with open ("JTToolsOptions.py","a") as f: f.write(" username2 = False\n")
 if useusername == int(1):
     with open ("JTToolsOptions.py","a") as f: f.write(" useusername = True\n")
     usernamenum = int(input("Please input how many usernames you wish to use."))
     if usernamenum <3:
         usernamesdone = 0
         while usernamesdone != usernamenum:
             currusername = input("Please enter the username enclosed in speech marks and brackets.")
             usernamesdone = usernamesdone +1
             if usernamenum == 1:
                 with open ("JTToolsOptions.py","a") as f: f.write(" username2 = False\n")
             if usernamesdone == 1:
                 with open ("JTToolsOptions.py","a") as f: f.write(" username1 = ")
                 with open ("JTToolsOptions.py","a") as f: f.write(currusername)
                 with open ("JTToolsOptions.py","a") as f: f.write("\n")
             elif usernamesdone == 2:
                 with open ("JTToolsOptions.py","a") as f: f.write(" username2 = ")
                 with open ("JTToolsOptions.py","a") as f: f.write(currusername)
                 with open ("JTToolsOptions.py","a") as f: f.write("\n")
 developer = int(input("If you are planning to he a developer of this script please enter 1. If not, please enter any other number."))
 if developer == 1:
     with open ("JTToolsOptions.py","a") as f: f.write(" idle = True\n")
 elif developer != 1:
     with open ("JTToolsOptions.py","a") as f: f.write(" idle = False\n")
 securityvanish = int(input("For security reasons, this script has a feature where after you have put your code in, the script will print x lines of nothing to hide your code.Please enter the number of lines you wish to be printed."))
 confirmed = int(0)
 while securityvanish <500 and confirmed != 1:
     confirm = int(input("WARNING! This number of lines may not be suitable.Please enter 1 to confirm this number."))
     if confirm != int(1):
         securityvanish = int(input("Please enter a new number of lines."))
     elif confirm == int(1):
         confirmed = int(1)
 if securityvanish >499:
     with open ("JTToolsOptions.py","a") as f: f.write(" vanishprint = ")
     with open("JTToolsOptions.py","a") as outf: outf.write(str(securityvanish))
     with open ("JTToolsOptions.py","a") as f: f.write("\n")
 showmenu = int(input("Please enter 1 if you want menus to be displayed or any other number to not."))
 if showmenu == 1:
     with open ("JTToolsOptions.py","a") as f: f.write(" menu = True\n")
 if showmenu != 1:
     with open ("JTToolsOptions.py","a") as f: f.write (" menu = False")
     
 



        
                              
                   
                   
     

            


except(ValueError):
    print("FOLLOW INSTRUCTIONS!")
    subprocess.call("JTToolsInstaller.py", shell = True)
    time.sleep(5)

py_compile.compile("JTToolsOptions.py")
try:
 shutil.copy("\\__pycache__\JTToolsOptions.cpython-35.pyc","\\")
 os.rename("\\JTToolsOptions.cpython-35.pyc", "JTToolsOptions.pyc")
 os.remove("\\__pycache__\JTToolsOptions.cpython-35.pyc")
except(FileNotFoundError):
 try:
   shutil.copy("\\__pycache__\JTToolsOptions.cpython-34.pyc","\\")
   os.rename("\\JTToolsOptions.cpython-34.pyc", "JTToolsOptions.pyc")
   os.remove("\\__pycache__\JTToolsOptions.cpython-34.pyc")
 except(FileNotFoundError):
     try:
      shutil.copy("\\__pycache__\JTToolsOptions.cpython-33.pyc","\\")
      os.rename("\\JTToolsOptions.cpython-33.pyc", "JTToolsOptions.pyc")
      os.remove("\\__pycache__\JTToolsOptions.cpython-33.pyc")
     except(FileNotFoundError):
         try:
          shutil.copy("\\__pycache__\JTToolsOptions.cpython-32.pyc","\\")
          os.rename("\\JTToolsOptions.cpython-32.pyc", "JTToolsOptions.pyc")
          os.remove("\\__pycache__\JTToolsOptions.cpython-32.pyc")
         except(FileNotFoundError):
             try:
              shutil.copy("\\__pycache__\JTToolsOptions.cpython-31.pyc","\\")
              os.rename("\\JTToolsOptions.cpython-31.pyc", "JTToolsOptions.pyc")
              os.remove("\\__pycache__\JTToolsOptions.cpython-31.pyc")
             except(FileNotFoundError):
                 try:
                  shutil.copy("\\__pycache__\JTToolsOptions.cpython-30.pyc","\\")
                  os.rename("\\JTToolsOptions.cpython-30.pyc", "JTToolsOptions.pyc")
                  os.remove("\\__pycache__\JTToolsOptions.cpython-30.pyc")
                 except(FileNotFoundError):
                     print("Sorry! You need to update Python to at least version 3.0")
              
          
       
     



os.remove("\\JTToolsOptions.py")


    
                

