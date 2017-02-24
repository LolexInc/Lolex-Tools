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
    if LolexToolsOptions.onepintotal>1:
        outf.write("oneswappins = True\nruntimeone = ")
        outf.write(str(verifonboot.runtimeone))
    if LolexToolsOptions.onewordtotal>1:
        outf.write("oneswapwords = True\nwordtimeone = ")
        outf.write(str(verifonboot.wordtimeone))
    if LolexToolsOptions.twopintotal>1:
        outf.write("twoswappins = True\nruntimetwo = ")
        outf.write(str(verifonboot.runtimetwo))
    if LolexToolsOptions.twowordtotal>1:
        outf.write("twoswappins = True\nwordtimetwo = ")
        outf.write(str(verifonboot.wordtimetwo))
if LolexToolsOptions.compiler == True:
    LolexToolsMethods.compiler("verifonboot")
print("Finished updating to 9.0nann2...")
with open("./madeon.py", "a") as outf: outf.write("compiledon = 9.00001")
        
