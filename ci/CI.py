#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, py_compile, sys, time
a = time.time()
print("CI version 3.0.0 PRERELEASE")
sys.path.insert(0, "./ci/build/")
import DJANGO_VERSION as env
for i in range(0, len(env.versions)):
    if i == len(env.versions):
        break;
    b = time.time()
    print("Installing DJANGO version " + env.versions[i])
    os.system("pip install -q django==" + env.versions[i])
    c = time.time()
    print("Installed DJANGO version " + env.versions[i] + " after " + (str(round(c - b, 0))) + " seconds")
    print("Testing...")
    folders = []
    files = []
    root = os.listdir("./")
    arraypos = 0
    while arraypos < len(root):
        if (".git" in root[arraypos]) == False:
            readin = True
            try:
                r = open(root[arraypos], "r")
            except(IOError, OSError):
                readin = False
            if readin == True:
                if root[arraypos].endswith(".py"):
                        files.append("./" + root[arraypos])
            if readin == False:
                readin2 = True
                try:
                    os.listdir(root[arraypos])
                except(IOError, OSError):
                    readin2 = False
                if readin2 == True:
                    folders.append("./" + root[arraypos])
        arraypos = arraypos + 1
    arraypos = 0
    while arraypos < len(folders):
        path = folders[arraypos] + "/"
        currsub = os.listdir(path)
        tarraypos = 0
        sublen = len(currsub)
        while tarraypos < sublen:
            if (".git" in currsub[tarraypos]) == False:
                readin3 = True
                try:
                    r = open(path + currsub[tarraypos])
                except(IOError, OSError):
                    readin3 = False
                if readin3 == True:
                    if currsub[tarraypos].endswith(".py"):
                        files.append(path + currsub[tarraypos])
                if readin3 == False:
                    readin4 = True
                    try:
                        os.listdir(path + currsub[tarraypos])
                    except(IOError, OSError):
                        readin4 = False
                    if readin4 == True:
                        folders.append(path + currsub[tarraypos])
            tarraypos = tarraypos + 1
        arraypos = arraypos + 1
    flen = len(files)
    arraypos = 0
    print("Compiling...")
    fail = False
    failers = 0
    while arraypos < flen:
        currfile = files[arraypos]
        if type(py_compile.compile(currfile)) is str:
            print("Successfully compiled " + (str(currfile)))
        else:
            print("Failed to compile " + (str(currfile)))
            fail = True
            failers = failers + 1
        arraypos = arraypos + 1
    print("Tests complete on DJANGO version " + env.versions[i] + " in " + (str(round(time.time() - b - round(c - b, 0), 0))) + " seconds")
    if fail == True:
        print((str(failers)) + " files failed to compile.")
        exit(1)
