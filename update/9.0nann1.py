import os, LolexToolsOptions, LolexToolsMethods, verifonboot
try:
    os.remove("./verifonboot.py")
except(IOError, OSError):
    pass
try:
    os.remove("./verifonboot.pyc")
except(IOError, OSError):
    pass
with open ("./verifonboot.py","a") as outf:
    if LolexToolsOptions.onepintotal>0:
        outf.write("oneswappins = True\nruntimeone = ")
        outf.write(str(verifonboot.runtimeone))
    if LolexToolsOptions.onewordtotal>0:
        outf.write("oneswapwords = True\nwordtimeone = ")
        outf.write(str(verifonboot.wordtimeone))
    if LolexToolsOptions.twopintotal>0:
        outf.write("twoswappins = True\nruntimetwo = ")
        outf.write(str(verifonboot.runtimetwo))
    if LolexToolsOptions.twowordtotal>0:
        outf.write("twoswappins = True\nwordtimetwo = ")
        outf.write(str(verifonboot.wordtimetwo))
        
