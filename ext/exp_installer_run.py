import os, sys
if input("Do you want to enter the experimental installer? Please enter 1 if so.") == "1":
    sys.path.insert(1, "./lib")
    import LolexToolsMethods
    os.system(LolexToolsMethods.pyo + " ./setup/exp/LolexToolsSetup.py")
