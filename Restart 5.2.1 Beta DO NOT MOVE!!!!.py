print ("This is copyrighted by Jensen Taylor (C). Restart script version 5.3.1.1 Beta")
print ("Importing module os...")
import os,time
print ("Module os has been imported successfully.")
print ("Importing module time...")
print ("Module time has been imported successfully.")
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
print ("Initializing...")
time.sleep (1.2)





print ("Here is a list of modes available:")
print ("1= Restart")
print ("2 = Logoff")
print ("3 = Hibernate")
print ("4 = Shutdown")
print ("5 = Colour Flicker")
print ("6 = Exit")



modewanted = int(input("Please enter the number of the mode that you want."))
if modewanted == 1:
  shutdown = int(input("Please enter 1 or 0 to confirm restart."))
  if shutdown == 1:
   confirmation = int(input("Please enter 1 for yes or 0 for no to confirm shutdown."))
   if confirmation == 1:
     codenpin = int(518082)
     code = int(input("Please enter the current NPIN."))
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
     if code == codenpin:
           waittimetwo = int(input("How long, in minutes, do you want to wait before shutting down?"))
           time.sleep (waittimetwo*60)
           os.system ("shutdown -l -f")
           os.system ("shutdown -r -f")
     if code != codenpin:
           print("Sorry, you inputted the wrong NPIN.")
           code = int(input("You have one attempt left to get the NPIN correct. Please enter the current NPIN."))
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
     if code == codenpin:
       waittimefour = int(input("How long, in minutes, do you want to wait before logoff proceeds?"))
       time.sleep (waittimefour*60)
       os.system ("shutdown -l -f")
     if code != codenpin:
       print ("You got the NPIN wrong. You now have two attempts left to get it right.")
       code = int(input("Please enter the current NPIN."))
       if code == codenpin:
         waittimefive = int(input("How long, in minutes, do you want to wait before logoff proceeds?"))
         time.sleep (waittimefive*60)
         os.system ("shutdown -l -f")
       if code != codenpin:
         print ("You got the NPIN wrong. You now have one attempt remaining to get it right.")
         code = int(input("Please enter the current NPIN."))
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
      codenpin = int(518082)
      code = int(input("Please enter the current NPIN."))
      if code == codenpin:
        waittimeseven = int(input("How long, in minutes, do you want to wait before hibernating proceeds?"))
        time.sleep (waittimeseven*60)
        os.system ("shutdown -h -f")
      if code != codenpin:
        print ("You got the NPIN wrong. You now have two attempts left to get it right.")
        code = int(input("Please enter the current NPIN."))
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
 suretoflash = int(input("Are you sure you wish to continue? 1 or 0. Please be aware that this could cause an epiplectic fit. Do not continue if you do suffer from epilepsy!"))
 if suretoflash == 1:
    howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
    haha = int(0)
                            
    while howlongtoflashfor != haha:
     os.system ("color 4a")
     os.system ("color f9")
     haha = haha +1

if modewanted == 6:
 print ("Closing!!!")


closing = 5
while closing !=6 and closing >0:
    closing = closing -0.01
    print ("Closing in",  round(closing, +3),"seconds.")
    time.sleep (0.01)

        
                     




      
           
            

