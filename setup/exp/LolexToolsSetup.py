#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import time, os, shutil, io
try:
    shutil.rmtree("./TEST")
except(IOError, OSError):
    pass
os.mkdir("./TEST")
users_file = open("./TEST/users.py", "w+")
users = []
done = "0"
while done != "1":
    valid = True
    user_name = input("Please enter your desired username.")
    if len(users) > 0:
        for i in range(0, len(users)):
            if i == len(users):
                break;
            if users[i] == user_name:
                print("Username is already taken!")
            else:
                users.append(user_name)
    done = input("Please enter 1 if you are done adding users.")
users_file.write("users = " + (str(users)))
print("Welcome to the preliminary LolexToolsSetup. It doesn't actually do anything so we'll just exit now...")
time.sleep(5)
exit(0)
