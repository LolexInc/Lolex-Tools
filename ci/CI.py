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
version = (str(sys.version_info[0])) + (str(sys.version_info[1])) + (str(sys.version_info[2])) + (str(sys.version_info[4]))
a = time.time()
print("CI version 3.0.0 PRERELEASE")
sys.path.insert(0, "./ci/build/")
import DJANGO_VERSION as ENV
import PYTHON_VERSION_FOR_AUTO as PY_VER
del sys.path[sys.path.index("./ci/build/")]
sys.path.insert(0, "../")
import PYTHON_VERSION_FOR_AUTO as PY_VER_OLD
if PY_VER.version < int(version) and sys.version_info[3] == "final":
        os.remove("./ci/build/PYTHON_VERSION_FOR_AUTO.py")
        with open("./ci/build/PYTHON_VERSION_FOR_AUTO.py", "a") as outf:
                outf.write("version = " + str(version))
                print("Found version was bigger than expected")
        os.system("git add *")
        os.system("git commit -am '[ci skip] Update python version in ci/build to " + str(version) + "'")
        if os.system("git pull --rebase") != 0:
            exit(127)
        os.system("git push")
failers = []
for i in range(0, len(ENV.versions)):
    if i == len(ENV.versions):
        break;
    failers.append(0)
    b = time.time()
    print("Installing DJANGO version " + ENV.versions[i])
    os.system("pip install django==" + ENV.versions[i])
    c = time.time()
    print("Installed DJANGO version " + ENV.versions[i] + " after " + (str(round(c - b, 0))) + " seconds")
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
    while arraypos < flen:
        currfile = files[arraypos]
        if type(py_compile.compile(currfile)) is str:
            print("Successfully compiled " + (str(currfile)))
            if version == PY_VER_OLD.version:
                print("Updating headers...")
                file_opened = open(currfile, "r+")
                file_opened_lines = file_opened.readlines()
                if file_opened_lines[0] != "#! python3":
                    file_opened_lines.insert(0, "#! python3\n")
                    file_opened.close()
                    try:
                        os.remove(currfile)
                    except(IOError, OSError):
                        pass
                    with open(currfile, "a") as outf:
                        for i in range(0, len(file_opened_lines)):
                            if i == len(file_opened_lines):
                                break;
                            outf.write("\n" + file_opened_lines[i])
                    os.system("git add *")
                    os.system("git commit -am '[ci skip] Update shebang line in " + currfile + "'")
                    os.system("git branch $TRAVIS_BUILD_NUMBER AUTOMATION")
                    if os.system("git pull --rebase") != 0:
                        os.system(127)
                    os.system("git push")
                    file_opened.close()
        else:
            print("Failed to compile " + (str(currfile)))
            fail = True
            failers[i] = failers[i] + 1
        arraypos = arraypos + 1
    d = (str(round(time.time() - b - round(c - b, 0), 0)))
    d.replace("-", "")
    print("Tests complete on DJANGO version " + ENV.versions[i] + " in " + d + " seconds")
if fail == True:
    out = ""
    for i in range(0, len(failers) - 1):
        out = "\n" + out + (str(failers[i])) + " failed on DJANGO version " + ENV.versions[i]
    exit(1)
