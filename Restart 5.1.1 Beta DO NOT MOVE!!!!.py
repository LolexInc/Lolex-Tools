print ("This is copyrighted by Jensen Taylor (C). Restart script version 5.1.1.1 Beta")
print ("The changelog is as follows: you can now see NPIN attempts in two modes and you can see when you started the script and finished the script.")
print ("Importing module os...")
import os
print ("Module os has been imported successfully.")
print ("Importing module time...")
import time
print ("Module time has been imported successfully.")
print ("Importing module sys...")
import sys
print ("Module sys has been successfully imported.")
def enter_code():
  codenpin = int(518082)
  code = int(input("Please enter the current NPIN."))
  if code != codenpin:
    enter_code()
  if code == codenpin:
    print ("Correct!")

localtime = time.asctime( time.localtime(time.time()) )
print ("Script loaded on:",localtime,)
print ("Here is a list of modes available:")
print ("1= Restart")
print ("2 = Logoff")
print ("3 = Hibernate")
print ("4 = Shutdown")
print ("5 = Exit")
modewanted = int(input("Please enter the number of the mode that you want."))
if modewanted == 1:
  shutdown = int(input("Please enter 1 or 0 to confirm restart."))
  if shutdown == 1:
   confirmation = int(input("Please enter 1 for yes or 0 for no to confirm shutdown."))
   if confirmation == 1:
     codenpin = int(518082)
     code = int(input("Please enter the current NPIN."))
     print ("Processing your attempt...")
     localtime = time.asctime( time.localtime(time.sleep(2)) )
     print ("First NPIN code attempt made at:",localtime,)
     if code == codenpin:
        waittime = int(input("How long, in minutes, do you want to wait before shutting down?"))
        time.sleep(waittime*60)
        os.system ("shutdown -r -f")
        os.system ("shutdown -l -f")
   if confirmation != 1:
     print ("Sorry, you inputted the wrong answer.")
   if shutdown ==0:
     print ("Sorry, you inputted the wrong answer.")
   if code != codenpin:
     print ("Sorry, you inputted the wrong NPIN.")
     code = int(input("You have two attempts left to get the NPIN correct. Please enter the current NPIN."))
     print ("Processing your attempt...")
     localtime = time.asctime( time.localtime(time.sleep(2)) )
     print ("Second NPIN code attempt made at:",localtime,)
     
     if code == codenpin:
           waittimetwo = int(input("How long, in minutes, do you want to wait before shutting down?"))
           time.sleep (waittimetwo*60)
           os.system ("shutdown -l -f")
           os.system ("shutdown -r -f")
     if code != codenpin:
           print("Sorry, you inputted the wrong NPIN.")
           code = int(input("You have one attempt left to get the NPIN correct. Please enter the current NPIN."))
           print ("Processing your attempt...")
           localtime = time.asctime( time.localtime(time.sleep(2)) )
           print ("Third NPIN code attempt made at:",localtime,)
           if code == codenpin:
                waittimethree = int(input("How long, in minutes, do you want to wait before shutting down?"))
                time.sleep (waittimethree*60)
                os.system ("shutdown -l -f")
                os.system ("shutdown -r -f")
                
if modewanted == 2:
  confirmation = int(input("Enter 1 for yes or 0 for no to confirm logoff."))
  if confirmation == 1:
   suretologoff = int(input("Are you sure? 1 or 0?"))
   if suretologoff == 1:
     codenpin = int(518082)
     code = int(input("Please enter the current NPIN."))
     print ("Processing your attempt...")
     localtime = time.asctime( time.localtime(time.sleep(2)) )
     print ("First NPIN code attempt made at:",localtime)
     if code == codenpin:
       waittimefour = int(input("How long, in minutes, do you want to wait before logoff proceeds?"))
       time.sleep (waittimefour*60)
       os.system ("shutdown -l -f")
     if code != codenpin:
       print ("You got the NPIN wrong. You now have two attempts left to get it right.")
       code = int(input("Please enter the current NPIN."))
       print ("Processing your attempt...")
       localtime = time.asctime( time.localtime(time.sleep(2)) )
       print ("Second NPIN code attempt made at:",localtime,)
       if code == codenpin:
         waittimefive = int(input("How long, in minutes, do you want to wait before logoff proceeds?"))
         time.sleep (waittimefive*60)
         os.system ("shutdown -l -f")
       if code != codenpin:
         print ("You got the NPIN wrong. You now have one attempt remaining to get it right.")
         code = int(input("Please enter the current NPIN."))
         print ("Processing your attempt...")
         localtime = time.asctime( time.localtime(time.sleep(2)) )
         print ("Third NPIN code attempt made at:",localtime,)
         if code == codenpin:
           waittimesix = int(input("How long, in minutes, do you want to wait before logoff proceeds?"))
           time.sleep (waittimesix*60)
           os.system ("shutdown -l -f")
         if code != codenpin:
           print("You got the NPIN wrong.")
if modewanted == 3:
  confirmation = int(input("Enter 1 for yes or 0 for no to confirm hibernation of this computer."))
  if confirmation == 1:
    suretohibernate = int(input("Are you sure? 1 or 0?"))
    if suretohibernate == 1:
     
     if code == codenpin:
        waittimeseven = int(input("How long, in minutes, do you want to wait before hibernating proceeds?"))
        time.sleep (waittimeseven*60)
        os.system ("shutdown -h -f")
        if code != codenpin:
         
         if code == codenpin:
          waittimeeight = int(input("How long, in minutes, do you wish to wait before hibernating proceeds?"))
          time.sleep (waittimeeight*60)
          os.system ("shutdown -h -f")
         if code != codenpin:
          print ("You got the NPIN wrong. You now have one attempt left to get it right.")
          code = int(input("Please enter the current NPIN."))
          if code == codenpin:
            waittimenine = int(input("How long, in minutes, do you wish to wait before hibernating proceeds?"))
            os.system ("shutdown -h -f")
          if code != codenpin:
            print ("Sorry, you entered the wrong NPIN three times.")
if modewanted == 4:
  confirmation = int(input("Enter 1 for yes or 0 for no to confirm shutdown of this computer."))
  if confirmation == 1:
    suretoshutdown = int(input("Are you sure? 1 or 0?"))
    if suretoshutdown == 1:
      codenpin = int(518082)
      code = int(input("Please enter the current NPIN."))
      if code == codenpin:
        waittimeten = int(input("How long, in minutes, do you wish to wait before shutting down proceeds?"))
        time.sleep (waittimeten*60)
        os.system ("shutdown -s -f")
      if code != codenpin:
        print ("You got the NPIN wrong. You now have two attempts remaining to get it correct.")
        code = int(input("Please enter the current NPIN."))
        if code == codenpin:
          waittimeeleven = int(input("How long, in minutes, do you want to wait before shutting down proceeds?"))
          time.sleep (waittimeeleven*60)
          os.system ("shutdown -s -f")
        if code != codenpin:
          print("You got the NPIN wrong. You now have one attempt remaining to get it right.")
          code = int(input("Please enter the current NPIN."))
          if code == codenpin:
            waittimetwelve = int(input("How long, in minutes, do you wish to wait before shutting down proceeds?"))
            time.sleep (waittimetwelve*60)
            os.system ("shutdown -s -f")
          if code != codenpin:
            print ("You got the NPIN wrong.")
if modewanted == 5:
 exit = int(input("Confirm closing of the script?1 or 0?"))
 if exit == 1:
   print("Closing...")



             

 
                    



