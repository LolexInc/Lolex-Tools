#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, time, py_compile, shutil, sys, platform, threading, subprocess
from glob import glob
syslen = len(sys.path)
print ("Module LolexToolsMethods is running, using modules os, time, py_compile, shutil, sys, platform, threading.")
if platform.system() == "Windows":
	if sys.version_info.minor > 5:
		py = "py .\\"
		pyo = "py"
	else:
		py = "python .\\"
		pyo = "python"
	s = "\\"
elif platform.system() == "Linux":
	py = "python3 ./"
	pyo = "python3"
	s = "/"
try:
	sys.path.append("./")
	import ver
except(ImportError) as e:
	if "arm" in platform.platform() == False:
		pass
	else:
		print("Please redownload this repository to access all features.")
		print(e)
		exit(0)
class uos:
	useros = platform.system()
	if "arm" in platform.platform():
		useros = "Android"
try:
		import restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings, menusettings
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
		time.sleep()
		os.system (colour[1])
		time.sleep()
		os.system (colour[2])
		time.sleep()
		os.system (colour[3])
		time.sleep()
		os.system (colour[4])
		time.sleep()
		currentflashes = currentflashes + 1
	import theme
	os.system(theme.theme)
	exit(0)
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
			print("18 = Call Remote Desktop")
			print("19 = Call Powershell")
			print("20 = Print SystemInfo")
	elif page == 4:
			print("21 = Start Installer")
			if exitsettings.hidden == False:
				print("22 = Exit")
	elif page == 5:
		print("EXPERIMENTAL FEATURES:")
		print("23 = Update")
		print("24 = Start File Explorer\n")
	if layout == 1:
			print("25 = Next Page")
			print("26 = Back a Page")
	else:
		if page < 5 and page != -1:
			page = page + 1
		else:
			return;
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
		print("12 = Start Installer")
		print("13 = Show Uptime and Average load")
		print("14 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("15 = Exit")
	elif page == 3:
		print("EXPERIMENTAL FEATURES:")
		print("16 = Start File Explorer\n")
	if layout == 1:
		print("17 = Next Page")
		print("18 = Back a Page")
	else:
		if page < 3:
			page = page + 1
		else:
			return;
		linuxpage (page, layout)
def androidpage(page, layout):
	if page == 0:
		print("1 = Settings")
		if restartsettings.hidden == False:
			print("2 = Restart")
		if shutdownsettings.hidden == False:
			print("3 = Shutdown")
		print("4 = Call a Python Shell")
		print("5 = Create folders")
	elif page == 1:
		print("6 = Remove folders")
		print("7 = Create files")
		print("8 = Restart this script")
		print("9 = Perform arithmetic operations")
		print("10 = Start Installer")
	elif page == 2:
		print("11 = Show Uptime and Average load")
		print("12 = Print SystemInfo")
		if exitsettings.hidden == False:
			print("13 = Exit")
		print("EXPERIMENTAL FEATURES:")
		print("14 = Start File Explorer\n")
	if layout == 1:
		print("15 = Next Page")
		print("16 = Back a Page")
	else:
		if page < 2:
			page = page + 1
		else:
			return;
		androidpage (page, layout)
def restart():
	restart = int(input("Please enter 1 to confirm restart."))
	if restart == 1:
		waittime = int(input("How long, in minutes do you wish to wait?"))
		restartthreader = threading.Thread(target = restartthread, args = [waittime])
		restartthreader.start()
def logoff(type):
	logoff = input("Please enter 1 to confirm logoff.")
	if logoff == "1":
		waittime = int(input("How long, in minutes do you wish to wait?"))
		loggeroff = threading.Thread(target = logoffthread, args = [waittime, type])
		loggeroff.start()
def logoffthread(waittime, type):
	time.sleep(waittime*60)
	print("LOGOFF thread: Logging off...")
	uos.useros = platform.system()
	if uos.useros != "Linux":
		if type == 0:
			os.system("shutdown -l -f")
		else:
			subprocess.Popen("logoff.exe")
	else:
		os.system("gnome-session-quit --force")
def hibernate():
	hibernate = input("Please enter 1 to confirm logoff.")
	if hibernate == "1":
		waittime = input("How long, in minutes do you wish to wait?")
		hibernatethreader = threading.Thread(target = hibernatethread, args = [waittime])
		hibernatethreader.start()
def hibernatethread(waittime):
	time.sleep(waittime*60)
	print("HIBERNATE thread: Hibernating...")
	uos.useros = platform.system()
	if uos.useros == "Windows":
		os.system("shutdown -h -f")
	elif uos.useros == "Linux":
		os.system("systemctl suspend")
def restartthread(waittime):
	time.sleep(waittime*60)
	print("RESTART thread: Restarting device...")
	uos.useros = platform.system()
	if uos.useros != "Linux":
		os.system("shutdown -r -f")
	else:
		if "arm" in platform.platform():
			if os.system("su -c reboot") != 0:
				os.system("reboot")
		else:
			os.system("reboot")
def shutdown(type):
	shutdown = input("Please enter 1 to shutdown.")
	if shutdown == "1":
		waittime = int(input("How long, in minutes, do you wish to wait?"))
		shutdownthreader = threading.Thread(target = shutdownthread, args = [waittime,type])
		shutdownthreader.start()
def shutdownthread(waittime, type):
	time.sleep(waittime*60)
	print("SHUTDOWN thread: shutting device down...")
	if uos.useros == "Windows":
		if type == 0:
			os.system ("shutdown -s -f")
		elif type == 1:
			subprocess.Popen("shutdown.exe")
	elif uos.useros == "Android":
		if os.system("su -c reboot -p") != 0:
			if os.system("/system/bin/reboot -p") != 0:
				print("Failed to execute reboot binary.")
	elif uos.useros == "Linux":
		os.system("poweroff")
def pyshell():
	if uos.useros == "Android" or uos.useros == "Linux":
		os.system("python3")
	elif uos.useros == "Windows":
		option = input("Please enter 1 for the Python Shell or 0 for the IDLE shell.")
		if option == "0":
			subprocess.call(pyo + ".exe")
		elif option == "1":
			subprocess.Popen(pyo + "w.exe")
def scriptrestart():
	confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
	if confirmscriptrestart == 1:
		os.system(py + "start.py")
		exit(0)
def numops():
	print ("Here is a list of operations:")
	print ("1 = Add")
	print ("2 = Take")
	submode = int(input("Please enter the number of the operatino you wish to perform."))
	if submode == 1 or submode == 2:
		addortake()
def addortake():
	startnum = int(input("Please enter your starting number."))
	addortakenum = int(input("Please input the number to be added."))
	endnum = int(input("Please enter your end number."))
	waittime = float(input("How long do you wish to wait before each operation is performed?"))
	if endnum > startnum:
		while endnum > startnum:
			print(startnum)
			if addortakenum < int(0):
				startnum = startnum - addortakenum
			elif addortakenum > int(0):
				startnum = startnum + addortakenum
			time.sleep(waittime)
		if startnum == endnum or startnum > endnum:
			print("The closest number to your target number was:" + (str(startnum)))
			time.sleep (1)
	elif startnum > endnum:
		while startnum > endnum:
			print (startnum)
			if addortakenum < 0:
				startnum = startnum + addortakenum
			if addortakenum > 0:
				startnum = startnum = startnum - addortakenum
			time.sleep (waittime)
		if startnum == endnum or startnum < endnum:
			print ("The closest number to your target end number was:" + (str(startnum)))
			time.sleep (1)
def dumpme():
	if uos.useros == "Windows":
		os.system(".\resources\systeminf")
	elif uos.useros == "Linux":
		os.system("sudo lshw")
	else:
		if os.system("su -c dumpsys") != 0:
			print("Cannot load as much information due to lack of root.")
			if os.system("/system/bin/dumpsys") != 0:
				print("Failed to execute dumpsys binary. Please check your root and SELinux statuses.")
def enterinstall():
	confirm = int(input("Please confirm (with a 1) to enter the installer."))
	if confirm == 1:
		os.system(py + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
		exit(0)
def uptime():
	if "arm" in platform.platform():
		if os.system("su -c uptime") != 0:
			if os.system("/system/bin/uptime") != 0:
				print("Failed to run uptime script.")
	else:
		os.system("uptime")
def logo():
	print("This function has been deprecated.")
def exitnow():
	print("This function has been deprecated.")
def compiler(name):
	try:
		os.remove("./" + name+".pyc")
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
		if LolexToolsOptions.compiler == True:
			compiler(name + ".py")
		os.system(py + ".." + s + "main" + s + "LolexTools.py")
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
		if LolexToolsOptions.compiler == True:
			compiler(name + ".py")
		os.system(py + "main" + s + "LolexTools.py")
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
					if LolexToolsOptions.compiler == True:
						compiler(name + ".py")
					os.system(py + "main" + s + "LolexTools.py")
					exit(None)
		if found == False:
			os.system(py + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
			exit(0)
def dirdisc(rtfiles, rtfolders, path):
	path = correctpath(path)
	class a:
		files = []
		folders = [path]
		fullfolders = []
	if sys.version_info.minor < 5:
		if validate(path) == True:
			while len(a.folders) != 0:
				a.folders[0] = correctpath(a.folders[0])
				class b:
					cont = os.listdir(a.folders[0])
				while len(b.cont) != 0:
					if validate(a.folders[0] + b.cont[0]) == True:
						patha = correctpath(a.folders[0] + b.cont[0])
						a.folders.append(patha)
						a.fullfolders.append(patha)
					elif validatefile(a.folders[0] + b.cont[0]) == True:
						patha = correctfile(a.folders[0] + b.cont[0])
						a.files.append(patha)
					del b.cont[0]
				del a.folders[0]
		else:
			return "INVALID<>";
	else:
		fullfolders = glob("./**/", recursive = True)
		files = glob("./**/*", recursive = True)
		print(fullfolders)
		print(files)
			
		arraypos = 0
		while arraypos < len(a.fullfolders):
			if validate(a.fullfolders[arraypos]) == False:
				del a.fullfolders[arraypos]
				arraypos = arraypos - 1
			arraypos = arraypos + 1
		arraypos = 0
		while arraypos < len(a.files):
			if validatefile(a.files[arraypos]) == False:
				del a.files[arraypos]
				arraypos = arraypos - 1
			arraypos = arraypos + 1
	if rtfiles == 1 and rtfolders == 1:
		files.append("END_OF_ARRAY<>")
		returns = a.files + a.fullfolders
		return returns;
	elif rtfiles == 1:
		return a.files;
	elif rtfolders == 1:
		return a.fullfolders;
	else:
		return "None";
def correctfile(path):
	slash = "\\"
	if len(path) > 2:
		path = path.replace(slash[0], "/")
		path = path.replace("//", "/")
		if path[0] == "." and path[1] == "/":
			path = path[:0]
			path = path[:1]
			path = os.getcwd() + path
	return path;
def validatefile(path):
	path = correctfile(path)
	class a:
		a = path
	valid = True
	try:
		open(a.a, "a")
	except(IOError, OSError):
		valid = False
	return valid;
def correctpath(path):
	slash = "\\"
	class zz:
		p = path
	if len(zz.p) > 2:
		if zz.p[len(zz.p) - 1] != "/" and (zz.p[len(zz.p) - 1] + zz.p[len(zz.p) - 1] != slash[0]):
			zz.p = zz.p + "/"
		zz.p = zz.p.replace(slash[0], "/")
		if zz.p[0] == "." and zz.p[1] == "/":
			zz.p = zz.p[:0]
			zz.p = zz.p[:1]
			zz.p = os.getcwd() + zz.p
		j = 0
	if len(zz.p) > 2:
		zz.p.replace("//", "/")
	return zz.p;
def validate(path):
	path = correctpath(path)
	class v:
		p = path
	readin = True
	try:
		os.path.isdir(v.p)
	except(IOError, OSError):
		readin = False
	if readin == True and not os.path.isdir(v.p):
		readin = False
	elif readin == True:
		try:
			os.listdir(v.p)
		except(IOError, OSError):
			readin = False
	return readin;
class expl:
	path = "/"
	newpath = "/"
	file = ""
def explorer(tofinishop, rtnofiles, rtnofolders, otext, path, allowexit):
	expl.path = path
	file = 0
	auto = 0
	if (platform.system() != "Windows" and platform.system() != "Linux"):
		clear = "<>"
	elif uos.useros == "Windows":
		clear = "cls"
	elif platform.system() == "Linux":
		clear = "clear"
	else: pass
	if clear == "<>":
		return 1;
	if clear != "<>":
		while True:
			print(expl.path)
			expl.path = correctpath(expl.path)
			y = validate(expl.path)
			if y == False:
				expl.file == ".."
				auto = 1
			if auto == 0:
				os.system(clear)
				print("\n " + expl.path + "\n")
				if otext == 0:
					otext = "Start/finish operations on this folder"
				if allowexit == 0:
					exittext = "You cannot exit until the current operation is complete"
				else:
					exittext = "Exit file explorer"
				print("\n\n///o - " + otext + "\n./ - Go to your current working directory\n/// - Reload\n///? - Help\n.. - Up a level\n///exit - " + exittext + "\n///s - Search for files/folders in this directory")
				array = os.listdir(expl.path)
				for i in range(0, len(array) - 1):
					print(array[i])
				expl.file = input("\nSelect/Open (Name): ")
			if expl.file == "///":
				pass
			elif expl.file == "./":
				expl.path = "./"
			elif expl.file == "..":
				if expl.path != "/":
					safedir = False
					while safedir == False:
						slash = False
						arraypos = len(expl.path) - 2
						if len(expl.path) > 2:
							while slash == False:
								if expl.path[arraypos] == "/":
									slash = True
									endpoint = arraypos
								else:
									arraypos = arraypos - 1
									endpoint = -1
								if arraypos < 1 and slash != True:
									path = "/"
									safedir = True
									slash = True
									break;
							if slash == True and expl.path != "/":
								arraypos = len(expl.path) - 2
								while arraypos > endpoint:
									expl.path = expl.path[:arraypos]
									arraypos = arraypos - 1
						else:
							expl.path = "/"
							slash = True
							safedir = True
							break;
						print("Out of loop...")
						y = validate(expl.path)
						if y == True:
							safedir == True
							break;
				else:
					print("Already at highest directory")
					time.sleep(3)
					break;
			if auto != 0:
				auto = 0
			else: pass
			if expl.file == "///?":
				print("Type names from here to enter/select files and folders.")
				time.sleep(5)
			elif expl.file == "///exit":
				if allowexit == 1:
					return 1;
				else:
					print("Operation not completed!")
					time.sleep(5)
			elif expl.file != "///s" and expl.file != "///o":
				o = False
				found = 0
				arraypos = 0
				possibles = []
				if validate(expl.path) == False:
					auto = 1
					expl.file = ".."
				else:
					array = os.listdir(expl.path)
					arraylen = len(array)
					while arraypos < arraylen:
						if array[arraypos] == expl.file:
							possibles.append(array[arraypos])
							found = found + 1
						arraypos = arraypos + 1
					if found == 2:
						if tofinishop == 1 or rtnofiles == 1:
							which = 1
						elif rtnofolders == 1:
							which = 0
						else:
							which = int(input("Please enter 1 for the folder, 0 for the file."))
							while which != 1 or which != 0:
								which = which - 2
						del possibles[which]
						found = 1
					else: pass
					if found == 1:
						expl.newpath = expl.path + "/" + possibles[0]
						if validate(expl.path) == False:
							auto = 1
							expl.file = ".."
						else:
							file = 0
							if os.path.isdir(expl.newpath) == False:
								file = 1
								try:
									open(expl.newpath, "a")
								except(IOError, OSError):
									file = 2
							else:
								try:
									os.listdir(expl.newpath + "/")
								except(IOError, OSError):
									file = 3
							if file != 0 and tofinishop == 1:
								file = 4
								print("Please select a (valid) folder to complete the operation.")
								time.sleep(3)
							if file == 2:
								print("Could not access file!")
								time.sleep(3)
							elif file == 3:
								print("Could not access folder!")
								time.sleep(3)
							elif file == 1:
								if rtnofiles != 1:
									return expl.newpath;
								o = True
							elif file == 0:
								expl.path = expl.newpath + "/"
								if tofinishop == True or rtnofolders == 0:
									return expl.path;
					elif found == 0:
						print("No such file or directory found!")
			elif expl.file == "///s" or expl.file == "///o":
				o = True
				expl.newpath = expl.path
			else: pass
			if o == True:
				op = 0
				while op != 7:
					if expl.file == "///s":
						pass
					else:
						print("\n" + expl.newpath + "\n")
						print("Here is a list of operations available: \n1 = Delete\n2 = Create file/folder")
						op = int(input("Please enter the number of the operation you wish to execute."))
					if op == 0 and expl.file == "///s":
						search = searchpath(input("Please enter the characters to search for."), expl.path, int(input("Please enter 1 to exlude this name, or 0 to include it.")), int(input("Please enter 1 to only include results with the characters at the end, or 0 to not.")), int(input("Please enter 1 to include folders, or 0 to not.")), int(input("Please enter 1 to include files, or 0 to not,")))
						if search == "INVALID<>":
							print("Folder could not be accessed or no return was selected.")
							time.sleep(3)
							break;
						elif searchpath.rtfiles == 1 and searchpath.rtfolders == searchpath.files:
							if search == "None" or (len(search) == 1 and search[0] == "END_OF_ARRAY<>"):
								print(search)
							else:
								print("Files:")
								for i in range(0, len(search) - 1):
									if search[i] != "END_OF_ARRAY<>":
										print( i + " = " + search[i])
									elif searchpath.rtfolders == 1:
										endfiles = i - 1
										j = i + 1
										print("Folders:")
										for k in range(j, len(search) - 1):
											print(k + " = " + search[k])
										break;
					elif op == 1:
						confirm = int(input("Please enter 1 to confirm delete."))
						if confirm == int(1):
							if os.path.isdir(expl.newpath) == True:
								print("Deleting...")
								try:
									shutil.rmtree(expl.newpath)
								except(IOError, OSError) as e:
									print(e)
									print("Couldn't delete folder.")
									time.sleep(3)
							else:
								print("Deleting...")
								try:
									os.remove(expl.newpath)
								except(IOError, OSError) as f:
									print(f)
									print("Couldn't delete folder.")
									time.sleep(3)
							op = 7
							auto = 1
							expl.file = ".."
					elif op == 2:
						if validatefile(expl.newpath) == True:
							print("Cannot create files/folders inside files!")
						else:
							oq = int(input("1 = Make a folder\n2 = Make a file\nPlease enter the number of the object you would like to create."))
							class create:
								if oq == int(1):
									typ = "folder"
								elif oq == int(2):
									typ = "file"
								newname = input("Please enter the name of your new " + typ + "  ")
							if oq == int(1):
								array.append(create.newname)
								try:
									print("Creating folder...")
									os.mkdir(expl.path + create.newname)
								except(IOError, OSError) as g:
									print(g)
									time.sleep(3)
									del array[len(array) - 1]
							elif oq == int(2):
								array.append(create.newname)
								try:
									print("Creating file...")
									open(expl.path + create.newname, "a")
								except(IOError, OSError) as h:
									print(h)
									time.sleep(3)
									del array[len(array) - 1]
					if op == 7:
						if tofinishop == 1:
							return expl.path;
						break;
							

			
del sys.path[syslen]
	