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
    done = input("Please enter 1 if you are done adding users.")
users_file.write("\nusers = " + (str(users)))
users_file.close()
