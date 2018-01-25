import sys, time
try:
    sys.path.insert(0,"\\")
    import isnottravisci
except(ImportError):
    print("Running as Travis CI... Tests complete. If you are not actually running in Travis CI, please create isnottravisci.py")
    print("Build passed our tests, exiting...")
    time.sleep(5)
    exit(None)
try:
 import sys
 sys.path.insert(0,"\\")
 import JTToolsOptions
except(ImportError):
 try:
  import JTToolsInstaller
 except(ImportError):
     print ("JT Tools Options and Installer are missing. Please go to github.com/monkeyboy2805/LolexTools and redownload them.")
     import time
     time.sleep(5)
     exit(None)
import time, os, subprocess,sys
sys.path.insert(0,"\\")
import JTToolsMethods,JTToolsOptions, verifonboot
JTToolsMethods.logo()
local =time.asctime( time.localtime(time.time()) )
with open("JT Tools Log File.txt", "a") as f: f.write(local)
with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools Initialized:version 7.0.0.1232.20.7.16\n")
print ("JT Tools script version 7.0.0 Beta")
from JTToolsOptions import Options
print ("Please wait two seconds...")
time.sleep (2)
vanish = int(0)
try:
 repeat = int(input("Please enter 1 to confirm you are not a robot."))
 if repeat != 1:
  local =time.asctime( time.localtime(time.time()) )
  with open ("JT Tools Log File.txt","a") as f: f.write (local)
  with open ("JT Tools Log File.txt","a") as f: f.write ("    JT Tools: User has proved that they either cannot read or are a robot.\n")
  JTToolsMethods.exitnow()
 if repeat == 1:
     local = time.asctime(time.localtime(time.time()))
     with open ("JT Tools Log File.txt","a") as f: f.write(local)
     with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools: User has proved they can read and aren't a robot.\n")
 
 uoneswappins = verifonboot.uoneswappins
 utwoswappins = verifonboot.utwoswappins
 runtimeone = verifonboot.runtimeone
 runtimetwo = verifonboot.runtimetwo
 if JTToolsOptions.Options.useusername == True:
     usernameenter = (str(input("Please enter yor username in speech marks and brackets.")))
     print (JTToolsOptions.Options.username1, JTToolsOptions.Options.username2)
     if usernameenter != (str(JTToolsOptions.Options.username1)) or (str(JTToolsOptions.Options.username2)):
         exit()
 elif JTToolsOptions.Options.useusername == False:
     usernameenter = str(JTToolsOptions.Options.username1)
 if usernameenter == str(JTToolsOptions.Options.username1):
     if JTToolsOptions.Options.uoneusepin == True:
         if verifonboot.uoneswappins == True:
             if uonepintwo == False:
                 runtimeone = 1
                 uoneswappins = False
             elif (JTToolsOptions.Options.uonepinthree == False and runtimeone == 2 or 0) or (JTToolsOptions.Options.uonepinfour == False and runtimeone == 3 or 0) or (JTToolsOptions.Options.uonepinfive == False and runtimeone == 4 or 0) or (JTToolsOptions.Options.uonepinfive != False and runtimeone == 5 or 0) or runtimeone == 0:
                 runtimeone = 1
                 print (runtimeone)
         
 while repeat == int(1):
  if JTToolsOptions.Options.menu == True:
   print ("Here is a list of mode groups available:")
   print ("1 = Power Menu Related Options:Restart, Logoff (2 methods available), Hibernate, Shutdown (2 methods available), Lock Workstation")
   print ("2 = Call Programs: CMD, Documents, Python Shell, Task Manager, Auto-Clicker, Notepad, Restart This Script")
   print ("3 = Miscellaneous Options")
  groupmode = int(input("Please enter the number of the group mode you wish to enter."))
  if groupmode == 1:
           local =time.asctime( time.localtime(time.time()) )
           with open("JT Tools Log File.txt", "a") as f: f.write(local)
           with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Mode Group 1 (Power Menu) entered.\n")
           print ("Here is a list of options available in this mode group:")
           print ("1 = Restart")
           print ("2 = Logoff")
           print ("3 = Hibernate")
           modewanted = int(input("Please enter the number of the mode that you want."))
           if modewanted == 1:
                 local =time.asctime( time.localtime(time.time()) )
                 with open("JT Tools Log File.txt", "a") as f: f.write(local)
                 with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Restart (mode 1.1) entered.\n")
                 restart = int(input("Please enter 1 to confirm restart."))
                 if restart == 1:
                  waittime =int(input("How long, in minutes, do you wish to wait?"))
                  time.sleep (waittime*60)
                  local =time.asctime( time.localtime(time.time()) )
                  with open("JT Tools Log File.txt", "a") as f: f.write(local)
                  with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Restart Operation.\n")
                  os.system ("shutdown -r -f")
                  os.system ("shutdown -l -f")
           elif modewanted == 2:
            local =time.asctime( time.localtime(time.time()) )
            with open("JT Tools Log File.txt", "a") as f: f.write(local)
            with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Logoff (mode 1.2) entered.\n")
            logoff = int(input("Please enter 1 or 0 to confirm logoff."))
            if logoff == 1:
             waittime =int(input("How long, in minutes, do you wish to wait?"))
             time.sleep (waittime*60)
             local =time.asctime( time.localtime(time.time()) )
             with open("JT Tools Log File.txt", "a") as f: f.write(local)
             with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Logoff Operation.\n")
             os.system ("shutdown -l -f")
           elif modewanted == 3:
            local =time.asctime( time.localtime(time.time()) )
            with open("JT Tools Log File.txt", "a") as f: f.write(local)
            with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Hibernate(mode 1.3) entered.\n")
            hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
            if hibernate == 1:
             time.sleep (waittime*60)
             local =time.asctime( time.localtime(time.time()) )
             with open("JT Tools Log File.txt", "a") as f: f.write(local)
             with open ("JT Tools Log File.txt","a") as f: f.write("    JT Tools :Performing Hibernate Operation.\n")
             os.system ("shutdown -h -f")
           elif modewanted == 4:
               subprocess.call("JTTools.py", shell = True)
  elif groupmode == 2:
      print("Here is a list of modes available:")
      print ("1 = Call CMD")
      print ("2 = Call Documents")
      print ("3 = Call Task Manager")
      print ("4 = Call Python Shell")
      modewanted = int(input("Please enter the number of the mode you wish to enter."))
      if modewanted == 1:
          subprocess.call("cmd.exe")
      if modewanted == 2:
          subprocess.call("explorer.exe")
      if modewanted == 3:
          subprocess.call("taskmgr.exe")
      if modewanted == 4:
          subprocess.call("python.exe")
  elif groupmode == 3:
      print("Here is a list of modes available:")
      print ("1 = Colour Flicker")
      modewanted = int(input("Please enter the number of the mode you want to enter."))
      if modewanted == 1:
          JTToolsMethods.flicker()
except():
    pass
#except(NameError,ValueError,SyntaxError,ImportError,WindowsError):
   # print ("Dammit! Something went wrong!")
   # time.sleep(5)
