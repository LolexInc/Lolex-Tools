
#! python3

#! python3

##0

## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000

##  0              00     0  0         0           00             00       0      0    0      0   0          0

##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000

##    0            00     0  0         0          0  0            00       0      0    0      0   0              0

##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000

##

## authors = Monkeyboy2805

import os, sys, time

sys.path.insert(0, "./project/old/lib")

try:

    import LolexToolsMethods

except(ImportError):

    print("Something went wrong here!")

    try:

        del sys.path[sys.path.index("./project/old/lib")]

    except(ValueError):

        pass

    time.sleep(5)

    exit(0)

try:

    del sys.path[sys.path.index("./project/old/lib")]

except(ValueError):

    pass

print("Nothing available here yet... Entering experimental setup...")

os.system(LolexToolsMethods.pyo + " ./project/new/setup/exp/LolexToolsSetup.py")

LolexToolsMethods.authenticate.login()
