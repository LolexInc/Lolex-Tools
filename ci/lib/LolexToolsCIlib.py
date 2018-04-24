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
def get_py_ver():
    return (str(sys.version_info[0])) + (str(sys.version_info[1])) + (str(sys.version_info[2])) + (str(sys.version_info[4]))
def update_py_ver():
    sys.path.insert(0, "./ci/build/prop")
    import LATEST_PYTHON_VERSION as PY_VER
    del sys.path[sys.path.index("./ci/build/prop")]
    sys.path.insert(0, "../Lolex-Tools-original")
    import LATEST_PYTHON_VERSION as PY_VER_OLD
    del sys.path[sys.path.index("../Lolex-Tools-original")]
    if PY_VER.version < int(get_py_ver()) and sys.version_info[3] == "final":
        os.remove("./ci/build/prop/LATEST_PYTHON_VERSION.py")
        with open("./ci/build/prop/LATEST_PYTHON_VERSION.py", "a") as outf:
            outf.write("version = " + str(get_py_ver()))
            print("Found version was bigger than expected")
        os.system("git add *")
        os.system("git commit -am '[ci skip] Update python version in ci/build to " + str(get_py_ver()) + "'")
        if os.system("git pull --rebase") != 0:
            exit(127)
        os.system("git push")
def update_headers():
    if int(get_py_version()) == int(PY_VER_OLD.version):
        ### Getting RIGHT contents but somehow writing to the wrong files
        print("Updating headers...")
        for j in range(0, len(files) - 1):
            file_opened = open(files[j], "r+")
            file_opened_lines = file_opened.readlines()
            if file_opened_lines[0] != "#! python3\n":
                file_opened_lines.insert(0, "#! python3\n")
                file_opened.close()
                os.remove(files[j])
                with open(files[j], "a") as outf:
                    for i in range(0, len(file_opened_lines)):
                        if i == len(file_opened_lines):
                            break
                        outf.write(file_opened_lines[i])
                os.system("git add *")
                os.system("git commit -am '[ci skip] Update shebang line in " + files[j] + "'")
                # os.system("git branch $TRAVIS_BUILD_NUMBER AUTOMATION")
                if os.system("git pull --rebase") != 0:
                    os.system("127")
                os.system("git push")
                file_opened.close()
