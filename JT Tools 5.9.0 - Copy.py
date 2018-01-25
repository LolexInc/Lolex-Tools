print ("This script is copyrighted by Jensen Taylor 2014 - 2016(C). JT Tools script version 6.0.0 Beta Re-Written for Python 2.7 instead of 3.4 due to a bug in python 3.4.1.")
print ("Importing module os...")
import os,subprocess
print ("Module os has been imported successfully.")
print ("Importing module time...")
import time
print ("Module time has been imported successfully.")
print ("Importing module sys...")
import sys
print ("Module sys has been successfully imported.")
os.system ("color f9")
print ("00000000000000000000000000000000000000000    00000000000000000000000")
print ("00000000000000000000000000000000000000000    00000000000000000000000")
print ("                                                    000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("            00000000000000000                       000000000")
print ("            0000000000000000                        000000000")
print ("           00000000000000000                        000000000")
print ("          00000000000000000                         000000000")
print ("         0000000000000000                           000000000")
print ("        000000000000000                             000000000")
print ("      0000000000000                                 000000000")
print ("    000000000000                                    000000000")
print ("Please wait two seconds...")
time.sleep (2)
terminal = int(0)




repeat = int(input("Please enter 1 to confirm you are not a robot."))
while repeat == int(1):
 print ("Here is a list of modes available:")
 print ("1= Restart")
 print ("2 = Logoff")
 print ("3 = Alternative Logoff Method ")
 print ("4 = Hibernate")
 print ("5= Shutdown")
 print ("6 = Alternative Shutdown Method")
 print ("7 = Colour Flickr")
 print ("8 = Call CMD")
 print ("9 = Call Documents")
 print ("10 = Call A Python Shell")
 print ("11 = Create folders in the same directory as this script.")
 print ("12 = Restart This Script (debug purposes)")
 print ("13 = Perform Operations With Numbers")
 print ("14 = Exit")



 modewanted = int(input("Please enter the number of the mode that you want."))
 if modewanted == 1:
  shutdown = int(input("Please enter 1 or 0 to confirm restart."))
  if shutdown == 1:
   code = int(518082)
   codeenter = int(input("Please enter the current NPIN."))
   while codeenter != code:
     print("Sorry you got the code wrong.")
     codeenter = int(input("Please enter the current NPIN."))
   if codeenter == code:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -r -f")
     os.system ("shutdown -l -f")
 if modewanted == 2:
  logoff = int(input("Please enter 1 or 0 to confirm logoff."))
  if logoff == 1:
   code = int(518082)
   codeenter = int(input("Please enter the current NPIN."))
   while codeenter != code:
     print("Sorry you got the code wrong.")
     codeenter = int(input("Please enter the current NPIN."))
   if codeenter == code:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -l -f")
 if modewanted == 4:
  hibernate = int(input("Please enter 1 or 0 to confirm hibernate."))
  if hibernate == 1:
   code = int(518082)
   codeenter = int(input("Please enter the current NPIN."))
   while codeenter != code:
     print("Sorry you got the code wrong.")
     codeenter = int(input("Please enter the current NPIN."))
   if codeenter == code:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -h -f")
  
 if modewanted == 5:
  shutdown = int(input("Please enter 1 or 0 (no) to confirm hibernate."))
  if shutdown == 1:
   code = int(518082)
   codeenter = int(input("Please enter the current NPIN."))
   while codeenter != code:
     print("Sorry you got the code wrong.")
     codeenter = int(input("Please enter the current NPIN."))
   if codeenter == code:
     waittime =int(input("How long, in minutes, do you wish to wait?"))
     time.sleep (waittime*60)
     os.system ("shutdown -s -f")


 if modewanted == 7:
  suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
  if suretoflash == 1:
    howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
    currentflashes= int(0)
                            
    while howlongtoflashfor != currentflashes:
     os.system ("color 4a")
     os.system ("color f9")
     currentflashes = currentflashes+1



 if modewanted == 8:
  code = int(518082)
  codeenter = int(input("Please enter the current NPIN to launch CMD."))
  while codeenter != code:
    print("Sorry, you inputted the wrong code.")
  if codeenter == code:
    subprocess.call("cmd.exe")
 if modewanted == 14:
  print ("Closing!!!")
  closing = 5
  while closing !=6 and closing >0:
    closing = closing -0.017
    print ("Closing in",  round(closing, +3),"seconds.")
    time.sleep (0.017)
  if closing == 0 or closing<0:
    exit()

 if modewanted == 9:
  code = int(518082)
  codeenter = int(input("Please enter the current NPIN to launch your documents."))
  while codeenter != code:
    print("Sorry, you inputted the wrong code.")
  if codeenter == code:
    subprocess.call("explorer.exe")

 if modewanted == 10:
  code= int(518082)
  codeenter =int(input("Please enter the current code to enter a python shell."))
  while codeenter != code:
   print("Sorry, you inputted the wrong code")
  if code == codeenter:
   subprocess.call("python.exe")

 if modewanted ==3:
  altlogoff = int(input("Please enter 1 or 0 to confirm logoff."))
  if altlogoff ==1:
   code = int(518082)
   codeenter =int(input("Please enter the current NPIN."))
   while codeenter != code:
    print ("Sorry, you inputted the wrong code.")
   if codeenter == code:
    waittime =int(input("How long, in minutes, do you wish to wait before logoff proceeds?"))
    time.sleep(waittime*60)
    subprocess.call ("logoff.exe")

 if modewanted == 6:
  altshutdown =int(input("Please enter 1 or 0 to confirm shutdown."))
  if altshutdown ==1:
   codeenter= int(input("Please enter the current code."))
   code =int(518082)
   while codeenter != code:
    print("Sorry, you inputted the wrong code.")
   if code== codeenter:
    waittime = int(input("How long, in minutes, do you wish to wait before shutdown proceeds?"))
    time.sleep (waittime*60)
    subprocess.call ("shutdown.exe")
   time.sleep (5)

 if modewanted == 11:
  
   code = int(518082)
 
   foldername = raw_input("Please input the name of your new folder.")
 
   codeenter= int(input("Please enter the current code to create this folder."))
   while codeenter != code:
    print("Sorry, you inputted the wrong code.")
   if codeenter == code:
    os.makedirs (foldername)
    cont = raw_input("Success! Press any key then enter to continue...")
  
    


 

 if modewanted == 12:



  confirmscriptrestart= int(input("Please input 1 to confirm restarting of this script."))
  if confirmscriptrestart == 1:
   code=int(518082)
   codeenter =int(input("Please enter the current code."))
   while codeenter != code:
    print("Sorry, you inputted the wrong code.")
   if codeenter ==code:
    subprocess.call ( "JT Tools 5.9.0.py", shell =True)
 if modewanted == 13:
  print ("Here is a list of operations:")
  print ("1 =Add")
  print ("2 = Take")
  submode = int(input("Please enter the number of the operatino you wish to perform>"))
  if submode == 1 or 2:
    check = int(0)
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
    if startnum>endnum and check !=int(1):
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


 
  


        
                     




      
           
            
