import os, py_compile
class vars:
    path = "./"
    root = os.listdir("./")
    folders = []
    files = []
    arraypos = 0
    arraylength = len(root)
while vars.arraypos < vars.arraylength:
    try:
        os.listdir(vars.root[vars.arraypos])
        vars.folders.append("./" + vars.root[vars.arraypos])
        #print(vars.folders)
    except(IOError, OSError):
        vars.files.append("./" + vars.root[vars.arraypos])
    #print(vars.files)
    vars.arraypos = vars.arraypos + 1
vars.arraypos = 0
vars.arraylength = len(vars.folders)
while vars.arraypos<vars.arraylength:
    vars.path = "./" + vars.folders[vars.arraypos]
    class number2:
        currsub = os.listdir(vars.path)
        arraypos = 0
        arraylength = len(currsub)
    while number2.arraypos<number2.arraylength:
        try:
            os.listdir(number2.currsub[number2.arraypos])
            vars.folders.append(vars.path + number2.currsub[number2.arraypos])
            #print(vars.folders)
            number2.arraypos = number2.arraypos + 1
        except(IOError, OSError):
            vars.files.append(vars.path + number2.currsub[number2.arraypos])
        #print(vars.files)
        number2.arraypos = number2.arraypos + 1
filearraylen = len(vars.files)
vars.arraypos = 0
while vars.arraypos<filearraylen:
    indivlen = len(vars.files[vars.arraypos])
    if vars.files[vars.arraypos[indiveln - 2]] == "y" and vars.files[vars.arraypos[indiveln - 3]] == "p" and vars.files[vars.arraypos[indiveln - 4]] == ".":
        py_compile.compile(vars.files[vars.arraypos])
        print("Successfully compiled " + vars.files[vars.arraypos])
        vars.arraypos = vars.arraypos + 1
