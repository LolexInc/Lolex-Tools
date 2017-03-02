import os, py_compile
folders = []
files = []
root = os.listdir("./")
arraypos = 0
filesl = 0
while arraypos < len(root):
    if (".git" in root[arraypos]) == False:
        if "." in root[arraypos] or "LICENSE" in root[arraypos]:
            length = len(root[arraypos])
            p = root[arraypos][length - 2]
            y = root[arraypos][length - 1]
            dot = root[arraypos][length - 3]
            if p == "p" and y == "y" and dot == ".":
                files.append("./" + root[arraypos])
        else:
            folders.append("./" + root[arraypos])
    arraypos = arraypos + 1
arraypos = 0
while arraypos<len(folders):
    path = folders[arraypos]
    currsub = os.listdir(path)
    tarraypos = 0
    sublen = len(currsub)
    while tarraypos<sublen:
        if (".git" in root[arraypos]) == False:
            if "." in root[arraypos]:
                clen = len(currsub[tarraypos])
                p = currsub[tarraypos][clen - 2]
                y = currsub[tarraypos][clen - 1]
                dot = currsub[tarraypos][clen - 3]
                if p == "p" and y == "y" and dot == ".":
                    files.append(path + currsub[tarraypos])
            else:
                folders.append(path + currsub[tarraypos])
        tarraypos = tarraypos + 1
    arraypos = arraypos + 1
flen = len(files)
arraypos = 0
print("Compiling...")
while arraypos<flen:
    currfile = file[arraypos]
    py_compile.compile(currfile)
    print("Successfully compiled " + (str(currfile)))
    arraypos = arraypos + 1
