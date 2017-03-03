##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
import py_compile
try:
    py_compile.compile("./LolexTools.py")
    py_compile.compile("./LolexToolsMethods.py")
    py_compile.compile("./LolexToolsInstaller.py")
except(SyntaxError):
    print("Build failed! Not all files compiled correctly...")
