#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import sys, os
class add_user:
    def setup_folder():
        pass
    def add_user_to_file():
        pass
class authenticate:
    def login():
        try:
            sys.path.insert(0, "./project/new/setup/exp/TEST")
            import users
            usernameenter = input("Please enter your username.")
            if usernameenter in users.users:
                path = users.paths[user.users.index(usernameenter)]
                print("Welcome " + (str(usernameenter)))
            else:
                return 1
        except(ImportError):
            return 2
