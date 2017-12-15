#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import time, os, shutil, io, sys, random
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
    IOError = OSError
try:
    try:
        shutil.rmtree("./project/new/TEST")
    except(IOError, OSError) as e:
        print(e)
    os.mkdir("./project/new/TEST")
    users_file = open("./project/new/TEST/users.py", "w+")
    users_file.write("#! python3\n##0\n## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000\n##  0              00     0  0         0           00             00       0      0    0      0   0          0\n##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000\n##    0            00     0  0         0          0  0            00       0      0    0      0   0              0\n##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000\n##\n## authors = Monkeyboy2805")
    users_file.truncate()
    users = []
    done = "0"
    while done != "1":
        valid = True
        user_name = input("Please enter your desired username.")
        if user_name in users:
            print("Username already in use!")
        else:
            users.append(user_name)
            length = len(os.getcwd()) - 1
            c = length - random.randint(0, 20)
            if c < 1:
                print("Not enough path space left!")
                break;
            folder_string = ""
            for i in range(0, c):
                b = random.randint(65, 115)
                if b > 90:
                    b = b + 7
                folder_string = folder_string + ((str(chr(b))))
        if not os.path.exists("./project/new/TEST/" + (str(folder_string))):
            os.mkdir("./project/new/TEST/" + (str(folder_string)))
        done = input("Please enter 1 if you are done adding users.")
    users_file.write("\nusers = " + (str(users)))
    users_file.close()
except(IOError, OSError) as e:
    print(e)
    print("Something went wrong! Look above for details.")
