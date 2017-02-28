import os, py_compile
class vars:
    path = "./"
    root = os.listdir("./")
    print(root)
    folders = []
    files = []
    arraypos = 0
    arraylength = len(root)
while vars.arraypos < vars.arraylength:
    try:
        if ".git" in vars.root[vars.arraypos] == False:
            os.listdir(vars.root[vars.arraypos])
            print(vars.root[vars.arraypos])
            vars.folders.append("./" + vars.root[vars.arraypos])
        #print(vars.folders)
    except(IOError, OSError):
        vars.files.append("./" + vars.root[vars.arraypos])
    vars.arraypos = vars.arraypos + 1
    print(len(vars.folders), " and ", len(vars.files), "discovered.")
print("Discovering subfolders...")
vars.arraypos = 0
vars.arraylength = len(vars.folders)
while vars.arraypos<vars.arraylength:
    vars.path = "./" + vars.folders[vars.arraypos]
    class number2:
        currsub = os.listdir(vars.path)
        print(currsub)
        arraypos = 0
        arraylength = len(currsub)
    while number2.arraypos<number2.arraylength:
        try:
            if ".git" in number2.currsub[number2.arraypos] == False:
                os.listdir(number2.currsub[number2.arraypos])
                print(number2.currsub[number2.arraypos])
                vars.folders.append(vars.path + number2.currsub[number2.arraypos])
            #print(vars.folders)
            number2.arraypos = number2.arraypos + 1
        except(IOError, OSError):
            vars.files.append(vars.path + number2.currsub[number2.arraypos])
        number2.arraypos = number2.arraypos + 1
        print(len(vars.folders), " and ", len(vars.files), "discovered.")
    vars.arraypos = vars.arraypos + 1
print("Compiling files...")
filearraylen = len(vars.files)
print("Seperating ", filearraylen, "files into .py and non-.py files...")
vars.arraypos = 0
while vars.arraypos<filearraylen:
    indivlen = len(vars.files[vars.arraypos])
    if vars.files[vars.arraypos][indivlen - 2] == "y" and vars.files[vars.arraypos][indivlen - 3] == "p" and vars.files[vars.arraypos][indivlen - 4] == ".":
        py_compile.compile(vars.files[vars.arraypos])
        print("Successfully compiled " + vars.files[vars.arraypos])
        vars.arraypos = vars.arraypos + 1
print("Done!")
