import os, py_compile
folders = []
files = []
root = os.listdir("./")
arraypos = 0
while arraypos < len(root):
    if (".git" in root[arraypos]) == False:
        if "." in root[arraypos] or "LICENSE" in root[arraypos]:
            length = len(root[arraypos])
            p = root[arraypos][length - 3]
            y = root[arraypos][length - 2]
            dot = root[arraypos][length - 4]
            if p == "p" and y == "y" and dot == ".":
                files.append("./" + root[arraypos])
            else:
                folders.append("
            
