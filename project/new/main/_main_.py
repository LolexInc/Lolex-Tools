#! python3
# 0
#  0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
#   0              00     0  0         0           00             00       0      0    0      0   0          0
#    0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
#     0            00     0  0         0          0  0            00       0      0    0      0   0              0
#      0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
#
# authors = Monkeyboy2805
import os
import sys
import time
sys.path.insert(0, "./project/old/lib")
try:
    import LolexToolsMethods  # As this is a custom library that the project needs to run, it's better to try except the import then the user has actually helpful information as to why the program isn't working. This could possibly be removed if logging were to ever work properly
except ImportError:
    print("Something went wrong here!")
    time.sleep(5)
    exit(1)
try:
    del sys.path[sys.path.index("./project/old/lib")]
except ValueError:
    pass
print("Nothing available here yet... Entering experimental setup...")
os.system(LolexToolsMethods.pyo + " ./project/new/setup/exp/LolexToolsSetup.py")
LolexToolsMethods.authenticate.login()
