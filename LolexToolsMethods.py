##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, time, py_compile, shutil, sys, platform, threading, subprocess
print ("Module LolexToolsMethods is running, using modules os, time, py_compile, shutil, sys, platform, threading.")
print("This module is intended for 9.0nann2/3, please do not mix and match for compatibility purposes.")
try:
	import ver
except(ImportError):
	if "arm" in platform.platform() == False:
		pass
	else:
		print("Please redownload this repository to access all features.")
try:
	import menusettings
except(ImportError):
	system = platform.system()
	if system == "Windows":
		subprocess.Popen(".\LolexToolsInstaller.py", shell = True)
	elif system == "Linux":
		os.system("python3 ./LolexToolsInstaller.py")
	exit(0)
try:
		import restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
		pass
def version():
	print(ver.version)
def flicker():
	suretoflash = int(input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy."))
	if suretoflash == 1:
		howlongtoflashfor = int(input("How many loops do you wish to occur?")) 
	print("Here is a list of colours available:")
	print("a - Neon Green")
	print("b - Light Blue")
	print("c - Neon Red")
	print("d - Light Purple/Pink")
	print("e - Neon Yellow")
	print("f - White")
	print("1 - Dark Blue")
	print("2 - Dark Green")
	print("3 - Light Non-Neon Blue")
	print("4 - Dark Red/Brown")
	print("5 - Dark Purple")
	print("6 - Non Neon Yellow")
	print("7 - White/Light Gray")
	print("8 - Dark Gray")
	print("9 - Dark Neon Blue")
	colour = ("color " + input("Please enter your first colour "), "color " + input("Please enter your second colour "), "color " + input("Please enter your third colour "), "color " + input("Please enter your fourth colour "), "color " + input("Please enter your fifth colour  "))
	flickerthread = threading.Thread(target=flickerp2, args=[colour, howlongtoflashfor])
	flickerthread.start()
def flickerp2(colour, howlongtoflashfor):
	currentflashes= int(0)
	while howlongtoflashfor != currentflashes:
		os.system (colour[0])
		time.sleep(0.2) # these delays are needed otherwise outputs mess up
		os.system (colour[1])
		time.sleep(0.2)
		os.system (colour[2])
		time.sleep(0.2)
		os.system (colour[3])
		time.sleep(0.2)
		os.system (colour[4])
		time.sleep(0.2)
		currentflashes = currentflashes + 1
	import theme
	os.system(theme.theme)
	exit()
def windowspage(page, layout):
	if page == 0:
		print("1  = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if logoffsettings.hidden == False:
			print("3  = Logoff")
			print("4  = Alternative logoff method")
		if hibernatesettings.hidden == False:
			print("5  = Hibernate")
	elif page == 1:
		if shutdownsettings.hidden == False:
			print("6  = Shutdown")
			print("7  = Alternative shutdown method")		 
		print("8  = Colour Flicker")
		print("9  = Call CMD")
		print("10 = Call documents")
	elif page == 2:
			print("11 = Call a Python shell")
			print("12 = Call Task Manager")
			print("13 = Create folders")
			print("14 = Remove folders")
			print("15 = Create files")
	elif page == 3:
			print("16 = Restart this script")
			print("17 = Perform arithmetic operations")
			print("18 = Lock this script")
			print("19 = Call Remote Desktop")
			print("20 = Call Powershell")
	elif page == 4:
			print("21 = Print SystemInfo")
			print("22 = Start Installer")
	elif page == 5:
			if exitsettings.hidden == False:
				print("23 = Exit")
			print("24 = Experimental auto-update")
	if layout == 0:
			print("25 = Next Page")
			print("26 = Back a Page")
	else:
		if page < 5 and page != -1:
			page = page + 1
			windowspage(page, layout)
def linuxpage(page, layout):
	if page == 0:
		print("1  = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if logoffsettings.hidden == False:
			print("3  = Logoff")
		if hibernatesettings.hidden == False:
			print("4  = Hibernate")
		if shutdownsettings.hidden == False:
			print("5  = Shutdown")
	elif page == 1:
		print("6  = Call a Python Shell")
		print("7  = Create folders")
		print("8  = Remove folders")
		print("9  = Create files")
		print("10 = Restart this script")
	elif page == 2:
		print("11 = Perform arithmetic operations")
		print("12 = Lock this script")
		print("13 = Start Installer")
		print("14 = Show Uptime and Average load")
		print("15 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("16 = Exit")
	if layout == 0:
		print("17 = Next Page")
		print("18 = Back a Page")
	else:
		if page < 2 and page != -1:
			page = page + 1
			linuxpage(page, layout)
		else:
			page = 0
			linuxpage (page, layout)
def androidpage(page, layout):
	if page == 0:
		print("1 = Settings")
		if restartsettings.hidden == False:
			print("2  = Restart")
		if shutdownsettings.hidden == False:
			print("3 = Shutdown")
		print("4  = Call a Python Shell")
		print("5  = Create folders")
	elif page == 1:
		print("6  = Remove folders")
		print("7  = Create files")
		print("8 = Restart this script")
		print("9 = Perform arithmetic operations")
		print("10 = Lock this script")
	elif page == 2:
		print("11 = Start Installer")
		print("12 = Show Uptime and Average load")
		print("13 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("14 = Exit")
	if layout == 0:
		print("15 = Next Page")
		print("16 = Back a Page")
	else:
		if page < 2 and page != -1:
			page = page + 1
			androidpage(page, layout)
		else:
			page = 0
			androidpage (page, layout)
def restart():
	restart = int(input("Please enter 1 to confirm restart."))
	if restart == 1:
		waittime = int(input("How long, in minutes do you wish to wait?"))
	restartthread = threading.Thread(target = restart, args = [waittime])
	restartthread.start()
def logoff(type):
	logoff = int(input("Please enter 1 to confirm logoff."))
	if logoff == 1:
		waittime = int(input("How long, in minutes do you wish to wait?"))
	loggeroff = threading.Thread(target = logoffthread, args = [waittime, type])
	loggeroff.start()
def logoffthread(waittime, type):
	time.sleep(waittime*60)
	print("LOGOFF thread: Logging off...")
	useros = platform.system()
	if useros != "Linux":
		if type == 0:
			os.system("shutdown -l -f")
		else:
			subprocess.call("logoff.exe")
	else:
		os.system("gnome-session-quit --force")
def hibernate():
	hibernate = int(input("Please enter 1 to confirm logoff."))
	if hibernate == 1:
		waittime = int(input("How long, in minutes do you wish to wait?"))
	hibernatethread = threading.Thread(target = hibernatethread, args = [waittime])
	hibernatethread.start()
def hibernatethread(waittime):
	time.sleep(waittime*60)
	print("HIBERNATE thread: Hibernating...")
	useros = platform.system()
	if useros != "Linux":
		os.system("shutdown -h -f")
	else:
		os.system("systemctl suspend")
def restart(waittime):
	time.sleep(waittime*60)
	print("RESTART thread: Restarting device...")
	useros = platform.system()
	if useros != "Linux":
		os.system("shutdown -r -f")
	else:
		if "arm" in platform.platform():
			if os.system("su -c reboot") != 0:
				os.system("reboot")
		else:
			os.system("reboot")
def logo():
	print("This function has been deprecated.")
def exitnow():
	print("This function has been deprecated.")
def compiler(name):
	try:
		os.remove("./"+name+".pyc")
	except(IOError):
		pass
	py_compile.compile(name+".py","./"+name+".pyc")
	os.remove("./"+name+".py")
def modehide(name, state):
	if state == False:
		newstate = True
	else:
		newstate = False
	try:
		os.remove("./"+name+".py")
		os.remove("./"+name+".pyc")
	except(IOError):
		pass
	with open ("./"+name+"settings.py","a") as outf: 
		outf.write("hidden = ")
		outf.write(str(newstate))
def bak(name, path, reinstall, attrestore, regenerate):
	try:
		os.remove("./compile.py")
	except(IOError, OSError):
		pass
	if path == 0:
		path = "./"
	content = os.listdir(path)
	arraypos = 0
	found = False
	while arraypos < len(content):
		if name + ".pyc" in content[arraypos] and len(content[arraypos]) < len(name) + 5:
			found = True
			try:
				os.mkdir("./Backup")
			except(IOError, OSError):
				pass
			dir1 = ("./Backup/" + (str(ver.version)) + " " + (str(time.time())) + "/" + name + ".pyc.notpy" + (str(sys.version_info[0])) + (str(sys.version_info[1])))
			os.rename("./" + name + ".pyc", dir1)
			break;
		arraypos = arraypos + 1
	if found == False:
		print((str(name)) + " not found for backing up.")
	else:
		pass
	if regenerate == 1 and name == "LolexToolsOptions":
		attrestore = 1
		regenerate = 0
		reinstall = 0
	elif name == "verifonboot" or name == "theme" or name == "startplugins" or "settings" in name:
		regenerate = 1
		attrestore = 0
		reinstall = 0
	if "settings" in name:
		if name != "menusettings":
			with open ("./" + name + ".py", "a") as outf: outf.write("hidden = False")
		else:
			with open ("./menusettings.py", "a") as outf: outf.write("layout = 0")
		with open ("./compile.py", "a") as outf:
			outf.write("name = '")
			outf.write(str(name))
			outf.write("'")
		subprocess.Popen("./LolexTools.py", shell = True)
		exit(None)
	elif name == "verifonboot":
		import LolexToolsOptions
		if LolexToolsOptions.onepintotal > 1:
			oneswappins = True
		else:
			oneswappins = False
		if LolexToolsOptions.onewordtotal > 1:
			oneswapwords = True
		else:
			oneswapwords = False
		if LolexToolsOptions.twopintotal > 1:
			twoswappins = True
		else:
			twoswappins = False
		if LolexToolsOptions.twowordtotal > 1:
			twoswapwords = True
		else:
			twoswapwords = False
		with open ("./verifonboot.py", "a") as outf:
			outf.write("compiledon = ")
			outf.write(str(ver.version))
			outf.write("\nruntimeone = 0\nruntimetwo = 0\nwordtimeone = 0\nwordtimetwo = 0")
			outf.write("\noneswappins = ")
			outf.write(str(oneswappins))
			outf.write("\noneswapwords = ")
			outf.write(str(oneswapwords))
			outf.write("\ntwoswappins = ")
			outf.write(str(twoswappins))
			outf.write("\ntwoswapwords = ")
			outf.write(str(twoswapwords))
	elif name == "theme":
		# will add theme changing at some point
		with open ("./theme.py", "a") as outf: pass
	elif name == "startplugins":
		# will add ability to add plugins at some point
		with open ("./startplugins.py", "a") as outf: pass
	if name == "verifonboot" or name == "theme" or name == "startplugins":
		with open ("./compile.py", "a") as outf:
			outf.write("name = '")
			outf.write(str(name))
			outf.write("'")
		subprocess.Popen("./LolexTools.py", shell = True)
		exit(None)
	elif attrestore == 1:
		backup = os.listdir("./Backup")
		arraypos = 0
		found = False
		while arraypos < len(backup):
			currsub = os.listdir(backup[arraypos])
			tarraypos = 0
			while tarraypos < len(backup):
				if name + ".pyc" in currsub[tarraypos] and (".pycnotpy" + (str(sys.version_info[0])) + (str(sys.version_info[1])) in currsub[tarraypos]) == False:
					found = True
					os.rename("./Backup" + backup[arraypos] + cursub[tarraypos], "./" + name + ".pyc")
					with open ("./compile.py", "a") as outf:
						outf.write("name = '")
						outf.write(str(name))
						outf.write("'")
					subprocess.Popen("./LolexTools.py", shell = True)
					exit(None)
		if found == False:
			subprocess.Popen("./LolexToolsInstaller.py", shell = True)
			exit(None)
		
		
