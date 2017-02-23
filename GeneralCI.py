import py_compile
try:
    py_compile.compile("./LolexTools.py")
    py_compile.compile("./LolexToolsMethods.py")
    py_compile.compile("./LolexToolsInstaller.py")
except(SyntaxError):
    print("Build failed! Not all files compiled correctly...")
