##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, LolexToolsOptions, LolexToolsMethods
onepintotal = 0
if LolexToolsOptions.oneusepin != False:
    if LolexToolsOptions.onepinone != False:
        onepintotal = onepintotal + 1
        if LolexToolsOptions.onepintwo != False:
            onepintotal = onepintotal + 1
            if LolexToolsOptions.onepinthree != False:
                onepintotal = onepintotal + 1
                if LolexToolsOptions.onepinfour != False:
                    onepintotal = onepintotal + 1
                    if LolexToolsOptions.onepinfive != False:
                        onepintotal = onepintotal + 1
onewordtotal = 0
if LolexToolsOptions.oneuseword != False:
    if LolexToolsOptions.onewordone != False:
        onewordtotal = onewordtotal + 1
        if LolexToolsOptions.onewordtwo != False:
            onewordtotal = onewordtotal + 1
            if LolexToolsOptions.onewordthree != False:
                onewordtotal = onewordtotal + 1
                if LolexToolsOptions.onewordfour != False:
                    onewordtotal = onewordtotal + 1
                    if LolexToolsOptions.onewordfive != False:
                        onewordtotal = onewordtotal + 1
twopintotal = 0
if LolexToolsOptions.twousepin != False:
    if LolexToolsOptions.twopinone != False:
        twopintotal = twopintotal + 1
        if LolexToolsOptions.twopintwo != False:
            twopintotal = twopintotal + 1
            if LolexToolsOptions.twopinthree != False:
                twopintotal = twopintotal + 1
                if LolexToolsOptions.twopinfour != False:
                    twopintotal = twopintotal + 1
                    if LolexToolsOptions.twopinfive != False:
                        twopintotal = twopintotal + 1
twowordtotal = 0
if LolexToolsOptions.twouseword != False:
    if LolexToolsOptions.twowordone != False:
        twowordtotal = twowordtotal + 1
        if LolexToolsOptions.twowordtwo != False:
            twowordtotal = twowordtotal + 1
            if LolexToolsOptions.twowordthree != False:
                twowordtotal = twowordtotal + 1
                if LolexToolsOptions.twowordfour != False:
                    twowordtotal = twowordtotal + 1
                    if LolexToolsOptions.twowordfive != False:
                        twowordtotal = twowordtotal + 1
try:
    os.remove("./LolexToolsOptions.py")
    os.remove("./LolexToolsOptions.pyc")
except(IOError, OSError):
    print("Option files inaccessible.")
with open ("./LolexToolsOptions.py","a")as outf:
    outf.write("compiledon = 8.3")
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
    if onewordtotal>0:
        outf.write("\nonewordone = ")
        if LolexToolsOptions.onewordone == False:
            outf.write(str(LolexToolsOptions.onewordone))
        else:
            outf.write('("')
            outf.write(str(LolexToolsOptions.onewordone))
            outf.write('")')
        if onewordtotal>1:
            outf.write("\nonewordtwo = ")
            if LolexToolsOptions.onewordtwo == False:
                outf.write(str(LolexToolsOptions.onewordtwo))
            else:
                outf.write('("')
                outf.write(str(LolexToolsOptions.onewordtwo))
                outf.write('")')
            if onewordtotal>2:
                outf.write("\nonewordthree = ")
                if LolexToolsOptions.onewordthree == False:
                    outf.write(str(LolexToolsOptions.onewordthree))
                else:
                    outf.write('("')
                    outf.write(str(LolexToolsOptions.onewordthree))
                    outf.write('")')
                if onewordtotal>3:
                    outf.write("\nonewordfour = ")
                    if LolexToolsOptions.onewordfour == False:
                        outf.write(str(LolexToolsOptions.onewordfour))
                    else:
                        outf.write('("')
                        outf.write(str(LolexToolsOptions.onewordfour))
                        outf.write('")')
                    if onewordtotal>4:
                        outf.write("\nonewordfive = ")
                        if LolexToolsOptions.onewordfive == False:
                            outf.write(str(LolexToolsOptions.onewordfive))
                        else:
                            outf.write('("')
                            outf.write(str(LolexToolsOptions.onewordfive))
                            outf.write('")')
    if onepintotal>0:
        outf.write("\nonepinone = ")
        outf.write(str(LolexToolsOptions.onepinone))
        if onepintotal>1:
            outf.write("\nonepintwo = ")
            outf.write(str(LolexToolsOptions.onepintwo))
            if onepintotal>2:
                outf.write("\nonepinthree = ")
                outf.write(str(LolexToolsOptions.onepinthree))
                if onepintotal>3:
                    outf.write("\nonepinfour = ")
                    outf.write(str(LolexToolsOptions.onepinfour))
                    if onepintotal>4:
                        outf.write("\nonepinfive = ")
                        outf.write(str(LolexToolsOptions.onepinfive))
    if twopintotal>0:
        outf.write("\ntwopinone = ")
        outf.write(str(LolexToolsOptions.twopinone))
        if twopintotal>1:
            outf.write("\ntwopintwo = ")
            outf.write(str(LolexToolsOptions.twopintwo))
            if twopintotal>2:
                outf.write("\ntwopinthree = ")
                outf.write(str(LolexToolsOptions.twopinthree))
                if twopintotal>3:
                    outf.write("\ntwopinfour = ")
                    outf.write(str(LolexToolsOptions.twopinfour))
                    if twopintotal>4:
                        outf.write("\ntwopinfive = ")
                        outf.write(str(LolexToolsOptions.twopinfive))
    if twowordtotal>0:
        outf.write("\ntwowordone = ")
        if JTToolsOptions.twowordone == False:
            outf.write(str(LolexToolsOptions.twowordone))
        else:
            outf.write('("')
            outf.write(str(LolexToolsOptions.twowordone))
            outf.write('")')
        if twowordtotal>1:
            outf.write("\ntwowordtwo = ")
            if JTToolsOptions.twowordone == False:
                outf.write(str(LolexToolsOptions.twowordone))
            else:
                outf.write('("')
                outf.write(str(LolexToolsOptions.twowordone))
                outf.write('")')
            if twowordtotal>2:
                outf.write("\ntwowordthree = ")
                outf.write(str(LolexToolsOptions.twowordthree))
                if JTToolsOptions.twowordthree == False:
                    outf.write(str(LolexToolsOptions.twowordthree))
                else:
                    outf.write('("')
                    outf.write(str(LolexToolsOptions.twowordthree))
                    outf.write('")')
                if twowordtotal>3:
                    outf.write("\ntwowordfour = ")
                    if JTToolsOptions.twowordfour == False:
                        outf.write(str(LolexToolsOptions.twowordfour))
                    else:
                        outf.write('("')
                        outf.write(str(LolexToolsOptions.twowordfour))
                        outf.write('")')
                    if twowordtotal>4:
                        outf.write("\ntwowordfive = ")
                        if JTToolsOptions.twowordfive == False:
                            outf.write(str(LolexToolsOptions.twowordfive))
                        else:
                            outf.write('("')
                            outf.write(str(LolexToolsOptions.twowordfive))
                            outf.write('")')
if LolexToolsOptions.compiler == True:
    LolexToolsMethods.compiler("LolexToolsOptions")
print("Finished updating to 8.3...")
