import os, time
check = int (0)

print ("Module JTToolsMethods is running, using modules os and time.")
def flicker():
 suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
 if suretoflash == 1:
    howlongtoflashfor = int(input("How many flashes do you wish to occur?"))
    currentflashes= int(0)                       
    while howlongtoflashfor != currentflashes:
     os.system ("color 4a")
     os.system ("color f9")
     currentflashes = currentflashes+1

def logo():
    os.system ("color f9")
    print ("00000000000000000000000000000000000000000   00000000000000000000000")
    print ("00000000000000000000000000000000000000000   00000000000000000000000")
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
def exitnow():
    if check != 1:
        closing = 5
    while closing> 0.015:
        print("Closing in", round (closing, +3),"seconds.")
        time.sleep(0.017)
        closing = closing -0.015
