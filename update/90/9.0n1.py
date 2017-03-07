##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
import os, LolexToolsOptions, LolexToolsMethods
onepintotal = LolexToolsOptions.onepintotal
twopintotal = LolexToolsOptions.twopintotal
onewordtotal = LolexToolsOptions.onewordtotal
twowordtotal = LolexToolsOptions.twowordtotal
try:
    os.remove("LolexToolsOptions.py")
except(IOError, OSError):
    pass
try:
    os.remove("LolexToolsOptions.pyc")
except(IOError, OSError):
    pass
onemorepins = int(input("Please enter how many more PINs you wish to add for user 1?"))
with open("./LolexToolsOptions.py","a") as outf:
    if onepintotal>0:
        outf.write("\nonepin1 = ")
        outf.write(str(LolexToolsOptions.onepinone))
        if onepintotal>1:
            outf.write("\nonepin2 = ")
            outf.write(str(LolexToolsOptions.onepintwo))
            if onepintotal>2:
                outf.write("\nonepin3 = ")
                outf.write(str(LolexToolsOptions.onepinthree))
                if onepintotal>3:
                    outf.write("\nonepin4 = ")
                    outf.write(str(LolexToolsOptions.onepinfour))
                    if onepintotal>4:
                        outf.write("\nonepin5 = ")
                        outf.write(str(LolexToolsOptions.onepinfive))
    howmanypins = onepintotal + onemorepins
    while onepintotal<howmanypins:
        onepin = int(input("Please set your PIN."))
        confirm = int(input("Please confirm your PIN."))
        while onepin != confirm:
            onepin = int(input("Please set your PIN so that it matches."))
            confirm = int(input("Please confirm your PIN."))
        onepintotal = onepintotal + 1
        outf.write("\nonepin")
        outf.write(str(onepintotal))
        outf.write(" = ")
        outf.write(str(onepin))
twomorepins = int(input("Please enter how many more PINs you wish to add for user 2?"))
with open("./LolexToolsOptions.py","a") as outf:
    if twopintotal>0:
        outf.write("\ntwopin1 = ")
        outf.write(str(LolexToolsOptions.twopinone))
        if twopintotal>1:
            outf.write("\ntwopin2 = ")
            outf.write(str(LolexToolsOptions.twopintwo))
            if twopintotal>2:
                outf.write("\ntwopin3 = ")
                outf.write(str(LolexToolsOptions.twopinthree))
                if twopintotal>3:
                    outf.write("\ntwopin4 = ")
                    outf.write(str(LolexToolsOptions.twopinfour))
                    if twopintotal>4:
                        outf.write("\ntwopin5 = ")
                        outf.write(str(LolexToolsOptions.twopinfive))
    howmanypins = twopintotal + twomorepins
    while twopintotal<howmanypins:
        twopin = int(input("Please set your PIN."))
        confirm = int(input("Please confirm your PIN."))
        while twopin != confirm:
            twopin = int(input("Please set your PIN so that it matches."))
            confirm = int(input("Please confirm your PIN."))
        twopintotal = twopintotal + 1
        outf.write("\ntwopin")
        outf.write(str(twopintotal))
        outf.write(" = ")
        outf.write(str(twopin))
onemorewords = int(input("Please enter how many more passwords you wish to add for user 1?"))
with open("./LolexToolsOptions.py","a") as outf:
    if onewordtotal>0:
        outf.write("\noneword1 = ")
        outf.write(str(LolexToolsOptions.onewordone))
        if onewordtotal>1:
            outf.write("\noneword2 = ")
            outf.write(str(LolexToolsOptions.onewordtwo))
            if onewordtotal>2:
                outf.write("\noneword3 = ")
                outf.write(str(LolexToolsOptions.onewordthree))
                if onewordtotal>3:
                    outf.write("\noneword4 = ")
                    outf.write(str(LolexToolsOptions.onewordfour))
                    if onewordtotal>4:
                        outf.write("\noneword5 = ")
                        outf.write(str(LolexToolsOptions.onewordfive))
    howmanywords = onewordtotal + onemorewords
    while onewordtotal<howmanywords:
        oneword = int(input("Please set your PIN."))
        confirm = int(input("Please confirm your PIN."))
        while oneword != confirm:
            oneword = int(input("Please set your PIN so that it matches."))
            confirm = int(input("Please confirm your PIN."))
        onewordtotal = onewordtotal + 1
        outf.write("\noneword")
        outf.write(str(onewordtotal))
        outf.write(" = ")
        outf.write(str(oneword))
twomorewords = int(input("Please enter how many more passwords you wish to add for user 2?"))
with open("./LolexToolsOptions.py","a") as outf:
    if twowordtotal>0:
        outf.write("\ntwoword1 = ")
        outf.write(str(LolexToolsOptions.twowordone))
        if twowordtotal>1:
            outf.write("\ntwoword2 = ")
            outf.write(str(LolexToolsOptions.twowordtwo))
            if twowordtotal>2:
                outf.write("\ntwoword3 = ")
                outf.write(str(LolexToolsOptions.twowordthree))
                if twowordtotal>3:
                    outf.write("\ntwoword4 = ")
                    outf.write(str(LolexToolsOptions.twowordfour))
                    if twowordtotal>4:
                        outf.write("\ntwoword5 = ")
                        outf.write(str(LolexToolsOptions.twowordfive))
    howmanywords = twowordtotal + twomorewords
    while twowordtotal<howmanywords:
        twoword = int(input("Please set your PIN."))
        confirm = int(input("Please confirm your PIN."))
        while twoword != confirm:
            twoword = int(input("Please set your PIN so that it matches."))
            confirm = int(input("Please confirm your PIN."))
        twowordtotal = twowordtotal + 1
        outf.write("\ntwoword")
        outf.write(str(twowordtotal))
        outf.write(" = ")
        outf.write(str(twoword))
with open ("./LolexToolsOptions.py","a") as outf:
    outf.write("compiledon = 9.0")
    outf.write("\nonepintotal = ")
    outf.write(str(onepintotal))
    outf.write("\ntwopintotal = ")
    outf.write(str(twopintotal))
    outf.write("\nonewordtotal = ")
    outf.write(str(onewordtotal))
    outf.write("\ntwowordtotal = ")
    outf.write(str(twowordtotal))
    outf.write("\nuseusername = ")
    outf.write(str(LolexToolsOptions.useusername))
    useusername = 0
    outf.write("\nusername1 = ")
    if LolexToolsOptions.username1 == False:
        outf.write(str(LolexToolsOptions.username1))
    else:
        outf.write('("')
        outf.write(LolexToolsOptions.username1)
        outf.write('")')
    username1 = 0
    outf.write("\nusername2 = ")
    outf.write('("')
    outf.write(LolexToolsOptions.username2)
    outf.write('")')
    username2 = 0
    outf.write("\noneusepin = ")
    outf.write(str(LolexToolsOptions.oneusepin))
    oneusepin = 0
    outf.write("\ntwousepin = ")
    outf.write(str(LolexToolsOptions.twousepin))
    twousepin = 0
    outf.write("\noneuseword = ")
    outf.write(str(LolexToolsOptions.oneuseword))
    oneuseword = 0
    outf.write("\ntwouseword = ")
    outf.write(str(LolexToolsOptions.twouseword))
    twouseword = 0
    outf.write("\nonewordwait = ")
    outf.write(str(LolexToolsOptions.onewordwait))
    onewordwait = "None"
    outf.write("\ntwowordwait = ")
    outf.write(str(LolexToolsOptions.twowordwait))
    twowordwait = "None"
    outf.write("\ndeveloper = ")
    outf.write(str(LolexToolsOptions.developer))
    developer = "None"
    outf.write("\nvanishprint = ")
    outf.write(str(LolexToolsOptions.vanishprint))
    vanishprint = "None"
    outf.write("\ncompiler = ")
    outf.write(str(LolexToolsOptions.compiler))
    compiler = "None"
    outf.write("\ncompileplugins = ")
    outf.write(str(LolexToolsOptions.compileplugins))
    compileplugins = "None"
    outf.write("\nonewait = ")
    outf.write(str(LolexToolsOptions.onewait))
    onewait = "None"
    outf.write("\ntwowait = ")
    outf.write(str(LolexToolsOptions.twowait))
    twowait = "None"
    confirm = "None"
if LolexToolsOptions.compiler == True:
    LolexToolsMethods.compiler("LolexToolsOptions")
print("Finished updating to 9.0n1...")
