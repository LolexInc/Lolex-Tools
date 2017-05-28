#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, platform, shutil, sys, time
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
	IOError = OSError
sys.path.extend(("./lib/"))
a = time.time()
system = platform.system()
if "arm" in platform.platform():
	try:
		import androidinit
		try:
			os.remove("./ver_old.py")
		except(IOError, OSError):
			pass
		os.rename("./ver.py","ver_old.py")
		shutil.copy("/sdcard/Lolex-Tools/ver.py","./")
		import ver, ver_old
		if ver.version>ver_old.version:
			print("Installing updates...")
			os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
	except(ImportError, SyntaxError, TabError, EOLError):
		os.system("python3 /sdcard/Lolex-Tools/Androidfirsttimeinit.py")
try:
        if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
        	IOError = OSError
        fail = False
        try:
                import JTToolsOptions
                try:
                        os.rename("./JTToolsOptions.py","LolexToolsOptions.py")
                except(IOError, OSError):
                        try:
                                os.rename("./JTToolsOptions.pyc","LolexToolsOptions.pyc")
                        except(IOError, OSError):
                                pass
        except(ImportError, SyntaxError, TabError, EOLError, SystemError):
                fail = True
        if fail != False:
                import LolexToolsOptions
                if LolexToolsOptions.compiledon<8.127:
                        if platform.system() == "Windows":
                                if sys.version_info.minor>5:
                                        os.system(" py .\setup\generic\LolexToolsInstaller.py")
                                else:
                                        os.system("python .\setup\generic\LolexToolsInstaller.py")
                        else:
                                if platform.system() == "Linux":
                                        os.system("python3 ./setup/generic/LolexToolsInstaller.py")
                        exit(0)
                try:
                        import ver
                        if ver.version <= 8.129211346:
                                with open ("./exitsettings.py","a") as f: f.write("hidden = False")
                except(IOError, ImportError):
                        pass
except(ImportError, SyntaxError, TabError, EOLError, IOError, OSError, AttributeError):
        if platform.system() == "Windows":
                if sys.version_info.minor>5:
                        os.system("py .\setup\generic\LolexToolsInstaller.py")
                else:
                        os.system("python .\setup\generic\LolexToolsInstaller.py")
        else:
                os.system("python3 ./setup/generic/LolexToolsInstaller.py")
        exit(0)
if system == "Windows":
        os.system("TITLE Lolex-Tools")
        os.system("MODE 1000")
        if sys.version_info.minor>5:
                os.system("py .\sys\\bootanim.py")
                b = time.time()
                local = time.asctime(time.localtime(time.time()))
                with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                        outf.write(local)
                        outf.write("	 Took ")
                        outf.write((str(b-a)))
                        outf.write("seconds to initilaize on Windows Python >3.5\n")
                time.sleep(3)
                os.system("py .\main\\LolexTools.py")
        else:
                os.system("python .\sys\\bootanim.py")
                b = time.time()
                local = time.asctime(time.localtime(time.time()))
                with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                        outf.write(local)
                        outf.write("	 Took ")
                        outf.write((str(b-a)))
                        outf.write("seconds to initilaize on Windows Python < 3.6.\n")
                time.sleep(3)
                os.system("python .\main\\LolexTools.py")
        exit(0)
else:
        sys.stdout.write("\x1b]2;Lolex-Tools\x07")
        if "arm" in platform.platform() == False:
            os.system("python3 ./sys/bootanim.py")
            os.system("sudo apt-get install xdotool")
            os.system("xdotool key ctrl+super+Up")
        b = time.time()
        local = time.asctime(time.localtime(time.time()))
        with open ("./Logs/LolexToolsLogFile.txt","a") as outf:
                outf.write(local)
                outf.write("	 Took ")
                outf.write((str(b-a)))
                outf.write("seconds to initilaize on Linux Python 3.\n")
        time.sleep(3)
        os.system("python3 ./main/LolexTools.py")
        exit(0)
