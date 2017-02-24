import os, py_compile
class vars:
    path = "./"
    root = os.listdirs("./")
    folders = []
    files = []
    arraypos = 0
    arraylength = len(root)
while vars.arraypos < vars.arraylength:
    try:
        os.listdirs(vars.root[vars.arraypos])
        vars.folders.append("./" + vars.root[vars.arraypos])
    except(IOError, OSError):
        pass
