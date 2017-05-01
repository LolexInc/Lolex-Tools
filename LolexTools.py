#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import sys, time, subprocess, os, shutil, py_compile, platform, io, zipfile
system = platform.system()
if system == "Windows":
	if sys.version_info.major != 3:
		print("Only Python 3 is currently supported. Please install Python 3.")
		time.sleep(3)
try:
	import LolexToolsMethods
except(ImportError):
	print("Missing library. Please redownload this application.")
	exit(0)
try:
        import menusettings, restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings
except(ImportError):
        pass
try:
	import LolexToolsOptions, runningsys, startplugins, theme
except(ImportError):
	system = platform.system()
	if system == "Windows":
		if sys.version_info.minor>5:
			os.system("py .\LolexToolsInstaller.py")
		else:
			os.system("python .\LolexToolsInstaller.py")
	elif system == "Linux":
		os.system("python3 ./LolexToolsInstaller.py")
	exit(0)
try:
        import verifonboot
except(ImportError):
        LolexToolsMethods.bak("verifonboot", 0, 0, 0, 1)
        import verifonboot
try:
	import madeon
	LolexToolsOptions.compiledon = madeon.compiledon
except(ImportError):
	pass
if LolexToolsOptions.compiledon<9.00001:
	if LolexToolsOptions.compiledon<8.3:
		shutil.copy("./update/83/8.3release.py","./")
		if system == "Windows":
			if sys.version_info.minor>5:
				os.system ("py ./8.3release.py")
			else:
				os.system("python ./8.3release.py")
		else:
			os.system ("python3 ./8.3release.py")
		os.remove("./8.3release.py")
	if LolexToolsOptions.compiledon<9.0:
		shutil.copy("./update/90/9.0n1.py","./")
		if system == "Windows":
			if sys.version_info.minor>5:
				os.system ("py ./9.0n1.py")
			else:
				os.system("python ./9.0n1.py")
		else:
			os.system ("python3 ./9.0n1.py")
		try:
			os.remove("./9.0n1.py")
		except(IOError, OSError):
			pass
	if LolexToolsOptions.compiledon<9.00001:
		shutil.copy("./update/90/9.0nann2.py","./")
		if system == "Windows":
			if sys.version_info.minor>5:
				os.system ("py ./9.0nann2.py")
			else:
				os.system("python ./9.0nann2.py")
		else:
			os.system ("python3 ./9.0nann2.py")
		os.remove("./9.0nann2.py")
	if LolexToolsOptions.compiledon<9.0001:
		shutil.copy("./update/90/9.0nann3.py", "./")
		if system == "Windows":
			if sys.version_info>5:
				os.system("py ./9.0nann3.py")
			else:
				os.system("python ./9.0nann3.py")
		else:
			os.system("python3 ./9.0nann3.py")
		os.remove("./9.0nann3.py")
	if LolexToolsOptions.compiledon < 9.00101:
		shutil.copy("./update/90/9.0nann4.py", "./")
		if system == "Windows":
			if sys.version_info.minor > 5:
				os.system("py ./9.0nann4.py")
			else:
				os.system("python ./9.0nann4.py")
		elif system == "Linux":
			os.system("python3 ./9.0nann4.py")
		os.remove("./9.0nann4.py")
	print("Restarting to finish updating...")
	if system == "Windows":
		if sys.version_info.minor>5:
			os.system("py .\start.py")
		else:
		 	os.system("python .\start.py")
	else:
		os.system("python3 ./start.py")
	exit(0)
if system == "Windows":
	os.system(theme.theme)
	os.system("mode 1000")
	os.system("title Lolex-Tools")
print("Welcome to Lolex-Tools version 9.0exp 10:24 GMT+0.0 17/1/17")
try:
	oneswappins = verifonboot.oneswappins
	twoswappins = verifonboot.twoswappins
	runtimeone = verifonboot.runtimeone
	runtimetwo = verifonboot.runtimetwo
	oneswapwords = verifonboot.oneswapwords
	twoswapwords = verifonboot.twoswapwords
	wordtimeone = verifonboot.wordtimeone
	wordtimetwo = verifonboot.wordtimetwo
	oneuseword = LolexToolsOptions.oneuseword
	twouseword = LolexToolsOptions.twouseword
	if LolexToolsOptions.useusername == True:
		usernameenter = input("Please enter your username.")
		while usernameenter != LolexToolsOptions.username1 and usernameenter != LolexToolsOptions.username2:
			usernameenter = input("Please enter a valid username.")
	elif LolexToolsOptions.useusername == False:
		usernameenter = LolexToolsOptions.username1
	if LolexToolsOptions.username1 == usernameenter:
		if runtimeone == LolexToolsOptions.onepintotal:
			runtimeone = 1
		else:
			runtimeone = runtimeone + 1
		if LolexToolsOptions.onepintotal != 0:
			try:
				os.remove("./onepinner.py")
			except(IOError, OSError):
				pass
			with open ("./onepinner.py","a") as outf:
				outf.write("import LolexToolsOptions\npin = LolexToolsOptions.onepin")
				outf.write(str(runtimeone))
			import onepinner
			codeenter = int(input("Please enter your current PIN."))
			tries = 1
			if codeenter != onepinner.pin:
				while codeenter != onepinner.pin:
					if tries == 5:
						print("You got your PIN wrong 5 times.")
						time.sleep(LolexToolsOptions.onewait)
						tries = 0
					codeenter = int(input("Please enter your current PIN."))
					tries = tries + 1
		if verifonboot.oneswapwords == True:
			if LolexToolsOptions.onewordtotal == wordtimeone:
				wordtimeone = 1
			else:
				wordtimeone = wordtimeone + 1
			if LolexToolsOptions.onewordtotal != 0:
				try:
					os.remove("./oneworder.py")
				except(IOError, OSError):
					pass
				with open("./oneworder.py","a") as outf:
					outf.write("import LolexToolsOptions\nword = LolexToolsOptions.oneword")
					outf.write(str(wordtimeone))
				wordenter = input("Please enter your current password.")
				tries = 1
				while wordenter != oneworder.word:
					if tries == 5:
						print("You got your password wrong 5 times.")
						time.sleep(LolexToolsOptions.onewordwait)
						tries = 0
					wordenter = input("Please enter your current password.")
					tries = tries + 1
	elif LolexToolsOptions.username2 == usernameenter:
		if runtimetwo == LolexToolsOptions.twopintotal:
			runtimetwo = 1
		else:
			runtimetwo = runtimetwo + 1
		if LolexToolsOptions.twopintotal != 0:
			try:
				os.remove("./twopinner.py")
			except(IOError, OSError):
				pass
			with open ("./twopinner.py","a") as outf:
				outf.write("import LolexToolsOptions\npin = LolexToolsOptions.twopin")
				outf.write(str(runtimetwo))
			import twopinner
			codeenter = int(input("Please enter your current PIN."))
			tries = 1
			if codeenter != twopinner.pin:
				while codeenter != twopinner.pin:
					if tries == 5:
						print("You got your PIN wrong 5 times.")
						time.sleep(LolexToolsOptions.twowait)
						tries = 0
					codeenter = int(input("Please enter your current PIN."))
					tries = tries + 1
		if verifonboot.twoswapwords == True:
			if LolexToolsOptions.twowordtotal == wordtimetwo:
				wordtimetwo = 1
			else:
				wordtimetwo = wordtimetwo + 1
			if LolexToolsOptions.twowordtotal != 0:
				try:
					os.remove("./twoworder.py")
				except(IOError, OSError):
					pass
				with open ("./twoworder.py","a") as outf:
					outf.write("import LolexToolsOptions\nword = LolexToolsOptions.twoword")
					outf.write(str(wordtimetwo))
				import twoworder
				wordenter = input("Please enter your current password.")
				tries = 1
				while wordenter != twoworder.word:
					if tries == 5:
						print("You got your password wrong 5 times.")
						time.sleep(LolexToolsOptions.twowordwait)
						tries = 0
					wordenter = input("Please enter your current password.")
					tries = tries + 1
	if (verifonboot.runtimeone != runtimeone) or (verifonboot.runtimetwo != runtimetwo) or (verifonboot.oneswappins != oneswappins) or (verifonboot.twoswappins != twoswappins) or (verifonboot.wordtimeone != wordtimeone) or (wordtimetwo != verifonboot.wordtimetwo) or (oneswapwords != verifonboot.oneswapwords) or (twoswapwords != verifonboot.twoswapwords):
		try:
			os.remove("./verifonboot.py")
		except(IOError, OSError):
			pass
		try:
			os.remove("./verifonboot.pyc")
		except(IOError, OSError):
				print("verifonboot.pyc was not found.")
		with open ("./verifonboot.py","a") as outf:
			outf.write("oneswappins = ")
			outf.write(str(oneswappins))
			outf.write("\ntwoswappins = ")
			outf.write(str(twoswappins))
			outf.write("\nruntimeone = ")
			outf.write(str(runtimeone))
			outf.write("\nruntimetwo = ")
			outf.write(str(runtimetwo))
			outf.write("\nwordtimeone = ")
			outf.write(str(wordtimeone))
			outf.write("\nwordtimetwo = ")
			outf.write(str(wordtimetwo))
			outf.write("\noneswapwords = ")
			outf.write(str(oneswapwords))
			outf.write("\ntwoswapwords = ")
			outf.write(str(twoswapwords))
		if LolexToolsOptions.compiler == True:
			LolexToolsMethods.compiler("verifonboot")
	useros = platform.system()
	if "arm" in platform.platform():
		useros = "Android"
	layout = menusettings.layout
	if layout == 0:
		page = -1
	else:
		page = 0
	while True:
		if useros == "Windows":
			LolexToolsMethods.windowspage(page, menusettings.layout)
		elif useros == "Linux":
			LolexToolsMethods.linuxpage(page, menusettings.layout)
		elif useros == "Android":
			LolexToolsMethods.androidpage(page, menusettings.layout)
		modewanted = int(input("Please enter the number of the mode that you want."))
		if useros == "Windows":
			maxmode = 26
		elif useros == "Linux":
			maxmode = 18
		elif useros == "Android":
			maxmode = 14
		while modewanted > maxmode:
			modewanted = modewanted - maxmode
		while modewanted < 1:
			modewanted = modewanted + maxmode
		if modewanted == 1:
			print("1 = Menu Settings")
			print("2 = Hide modes")
			setting = int(input("Please enter the group of settings you wish to modify."))
			if setting == 1:
					print(" Modiy Menu Layout")
					if layout != 0:
						print(" 0 = Default")
					elif layout != 1:
						print(" 1 = Pages")
					layout = int(input("Please input the number of the setting you wish to apply."))
					try:
						os.remove("./menusettings.py")
						os.remove("./menusettings.pyc")
					except(IOError, OSError):
						pass
					with open ("./menusettings.py","a") as outf:
						outf.write("layout = ")
						outf.write(str(layout))
					if layout == 0:
						page = -1
					elif layout == 1:
						page = 0
			elif setting == 2:
				print("2 = Restart hidden = ", restartsettings.hidden)
				print("3 = Logoff hidden = ", logoffsettings.hidden)
				print("4 = Hibernate hidden = ", hibernatesettings.hidden)
				print("5 = Shutdown hidden = ", shutdownsettings.hidden)
				print("6 = Call a Python Shell hidden = ", pyshellsettings.hidden)
				print("7 = Create folders hidden = ", foldercreatesettings.hidden)
				print("8 = Remove folders hidden = ", exfoldersettings.hidden)
				print("9 = Create files hidden = ", addfilesettings.hidden)
				print("10 = Restart this script hidden = ", scriptloopsettings.hidden)
				print("11 = Perform arithmetic operations hidden = ", mathmodesettings.hidden)
				print("12 = Lock this script hidden = ", scriptlocksettings.hidden)
				print("13 = Start Installer hidden = ", installerstartsettings.hidden)
				print("14 = Print SystemInfo hidden = ", sysinfosettings.hidden)
				print("15 = Exit hidden = ", exitsettings.hidden)
				modetochange = int(input("Please select the number of the mode."))
				if modetochange == 2:
					LolexToolsMethods.modehide("restart", restartsettings.hidden)
				elif modetochange == 3:
					LolexToolsMethods.modehide("logoff", logoffsettings.hidden)
				elif modetochange == 4:
					LolexToolsMethods.modehide("hibernate", hibernatesettings.hidden)
				elif modetochange == 5:
					LolexToolsMethods.modehide("shutdown", shutdownsettings.hidden)
				elif modetochange == 6:
					LolexToolsMethods.modehide("pyshell", pyshellsettings.hidden)
				elif modetochange == 7:
					LolexToolsMethods.modehide("foldercreate", foldercreatesettings.hidden)
				elif modetochange == 8:
					LolexToolsMethods.modehide("exfolder", exfoldersettings.hidden)
				elif modetochange == 9:
					LolexToolsMethods.modehide("addfile", addfilesettings.hidden)
				elif modetochange == 10:
					LolexToolsMethods.modehide("scriptloop", scriptloopsettings.hidden)
				elif modetochange == 11:
					LolexToolsMethods.modehide("mathmode", mathmodesettings.hidden)
				elif modetochange == 12:
					LolexToolsMethods.modehide("scriptlock", scriptlocksettings.hidden)
				elif modetochange == 13:
					LolexToolsMethods.modehide("installerstart", installerstartsettings.hidden)
				elif modetochange == 14:
					LolexToolsMethods.modehide("sysinfo", sysinfosettings.hidden)
				elif modetochange == 15:
					LolexToolsMethods.modehide("exit", exitsettings.hidden)
				if useros == "Windows":
					if sys.version_info.minor>5:
						os.system("py .\start.py")
					else:
						os.system("python .\start.py")
				else:
					os.system("python3 ./start.py")
				exit(0)
		elif modewanted == 2:
			LolexToolsMethods.restart()
		elif (modewanted == 3 and useros != "Android") or (modewanted == 4 and useros == "Windows"):
			LolexToolsMethods.logoff(modewanted-3)
		elif (modewanted == 5 and useros == "Windows") or (modewanted == 4 and useros == "Linux"):
			LolexToolsMethods.hibernate()
		elif (modewanted == 6 and useros == "Windows") or (modewanted == 5 and useros == "Linux") or (modewanted == 3 and useros == "Android"):
			LolexToolsMethods.shutdown(0)
		elif modewanted == 7 and useros == "Windows" :
			LolexToolsMethods.shutdown(1)
		elif modewanted == 8 and useros == "Windows" :
			LolexToolsMethods.flicker()
		elif modewanted == 9 and useros == "Windows" :
			subprocess.call("cmd.exe")
		elif modewanted == 10 and useros == "Windows" :
			subprocess.Popen("explorer.exe")
		elif (modewanted == 11 and useros == "Windows") or (modewanted == 6 and useros == "Linux") or (modewanted == 4 and useros == "Android"):
			LolexToolsMethods.pyshell()
		elif modewanted == 12 and useros == "Windows" :
			subprocess.Popen("taskmgr.exe")
		elif (modewanted == 13 and useros == "Windows") or (modewanted == 7 and useros == "Linux") or (modewanted == 5 and useros == "Android"):
			foldername = input("Please input the name of your new folder.")
			try:
				os.makedirs (foldername)
				cont = input("Success! Press any key then enter to continue...")
			except(IOError, OSError):
				print("Failed to create folder: ", foldername)
		elif (modewanted == 14 and useros == "Windows") or (modewanted == 8 and useros == "Linux") or (modewanted == 6 and useros == "Android"):
			foldername = input("Please input the name of the folder you wish to delete.")
			try:
				 os.rmdir (foldername)
				 cont = input("Success! Press any key then enter to continue...")
			except(IOError, OSError):
				print("Folder does not exist!")
		elif (modewanted == 15 and useros == "Windows") or (modewanted == 9 and useros == "Linux") or (modewanted == 7 and useros == "Android"):
			try:
				filename = input("Please enter your file name plus the extension, eg. B.txt.  ")
				with io.FileIO (filename, "w"):
					pass
				cont = input("Success! Press any key then enter to continue...")
			except(IOError, OSError):
				print("Failed to create file: ",filename)
		elif (modewanted == 16 and useros == "Windows") or (modewanted == 10 and useros == "Linux") or (modewanted == 8 and useros == "Android"):
			LolexToolsMethods.scriptrestart()
		elif (modewanted == 17 and useros == "Windows") or (modewanted == 11 and useros == "Linux") or (modewanted == 9 and useros == "Android"):
			print ("Here is a list of operations:")
			print ("1 = Add")
			print ("2 = Take")
			submode = int(input("Please enter the number of the operatino you wish to perform."))
			if submode == 1 or 2:
				startnum = int(input("Please enter your starting number."))
				addortakenum = int(input("Please input the number to be added."))
				endnum = int(input("Please enter your end number."))
				waittime = int(input("How long do you wish to wait before each operation is performed?"))
				if endnum>startnum:
					while endnum>startnum:
						print(startnum)
						if addortakenum<int(0):
							startnum = startnum - addortakenum
						elif addortakenum > int(0):
							startnum = startnum + addortakenum
						time.sleep(waittime)
					if startnum == endnum or startnum>endnum:
						print("The closest number to your target number was:" + (str(startnum)))
						time.sleep (1)
					elif startnum > endnum:
						while startnum > endnum:
							print (startnum)
							if addortakenum < 0:
								startnum = startnum + addortakenum
							if addortakenum>0:
								startnum = startnum = startnum - addortakenum
								time.sleep (waittime)
						if startnum == endnum or startnum<endnum:
							print ("The closest number to your target end number was:" + (str(startnum)))
							time.sleep (1)
		elif modewanted == 18  and useros == "Windows" :
			path = input("Please input the full path of the RDP file.")
			length = len(path) - 1
			if path[length] == "p":
				length = length - 1
				if path[length] == "d":
					length = length - 1
					if path[length] == "r":
						length = length - 1
						if path[length] == ".":
							os.system(path)
			else:
				print("Not a valid rdp file.")
		elif modewanted == 19 and useros == "Windows" :
			subprocess.call("powershell.exe")
		elif (modewanted == 20 and useros == "Windows") or (modewanted == 14 and useros == "Linux") or (modewanted == 12 and useros == "Android"):
			if useros == "Windows":
				os.system("systeminf")
			elif useros == "Linux":
				os.system("sudo lshw")
			else:
				if os.system("su -c dumpsys") != 0:
					print("Cannot load as much information due to lack of root.")
					if os.system("/system/bin/dumpsys") != 0:
						print("Failed to execute dumpsys binary. Please check your root and SELinux statuses.")
		elif (modewanted == 21 and useros == "Windows") or (modewanted == 12 and useros == "Linux") or (modewanted == 10 and useros == "Android"):
			confirm = int(input("Please confirm (with a 1) to enter the installer."))
			if confirm == 1:
				if useros == "Windows":
					if sys.version_info.minor>5:
						os.system("py .\LolexToolsInstaller.py")
					else:
						os.system("python .\LolexToolsInstaller.py")
				else:
					os.system("python3 ./LolexToolsInstaller.py")
				exit(0)
		elif (modewanted == 13 and useros == "Linux") or (modewanted == 11 and useros == "Android"):
			if "arm" in platform.platform():
				if os.system("su -c uptime") != 0:
					if os.system("/system/bin/uptime") != 0:
						print("Failed to run uptime script.")
			else:
				os.system("uptime")
		elif (modewanted == 23 and useros == "Windows"):
			print("Checking for updates...")
			print("Upon prompt for saving the file, please save as Lolex-Tools-master.zip in your Lolex-Tools folder.")
			if os.system("git clone https://github.com/lolexorg/Lolex-Tools.git") != 0:
				continueto = int(input("Git was not found. Please press 1 to initiate webbrowser method or 0 to cancel."))
				if continueto == 1:
					print("Please save your zip to Lolex-Tools newversion folder.")
					os.system("python -m webbrowser -t https://github.com/lolexorg/Lolex-Tools/zipball/master")
					confirm = input("Press enter to continue...")
					try:
						os.remove("./newversion")
					except(IOError, OSError):
						pass
					os.mkdirs("./newversion")
					newver = os.listdirs("./newversion")
								
		# search for zips instead :P
					zip_ref = zipfile.ZipFile("./newversion"+newver[0], "r")
					print("Extracting...")
					zip_ref.extractall("newversion")
					zip_ref.close()	  
		elif (modewanted == 24 and useros == "Windows") or (modewanted == 16 and useros == "Linux") or (modewanted == 14 and useros == "Android") and menusettings.layout == 1:
			if (page < 5 and useros == "Windows") or (page < 2 and (useros == "Linux" or useros == "Android")):
				page = page + 1
			else:
				page = 0
		elif (modewanted == 25 and useros == "Windows") or (modewanted == 17 and useros == "Linux") or (modewanted == 15 and useros == "Android") and menusettings.layout == 1:
			if page > 0:
				page = page - 1
			else:
				if useros == "Windows":
					page = 5
				elif useros == "Linux" or useros == "Android":
					page = 2
		elif (modewanted == 22 and useros == "Windows") or (modewanted == 15 and useros == "Linux") or (modewanted == 13 and useros == "Android"):
			print("Exiting...")
			print("Giving all threads 5 seconds to exit...")
			time.sleep(5)
			os._exit(0)
except(SyntaxError) as a:
	print("Sorry! A SyntaxError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(a)
	time.sleep(10)
except(TypeError) as b:
	print("Sorry! A TypeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(b)
	time.sleep(10)
except(ValueError) as c:
	print("Sorry! A ValueError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(c)
	time.sleep(10)
except(IOError) as d:
	print("Sorry! An IOError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(d)
	time.sleep(10)
except(NameError) as e:
	print("Sorry! A NameError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(e)
	time.sleep(10)
except(EOFError) as f:
	print("Sorry! An EOFError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(f)
	time.sleep(10)
except(AttributeError) as g:
	print("Sorry! An AttributeError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(g)
	time.sleep(10)
except(OSError) as h:
	print("Sorry! An OSError occured. If this continues to occur, please make an issue on the Github, specifying which file it occured with and what part.")
	print(h)
	time.sleep(10)
except(ZeroDivisionError) as j: # not i for for loops
	print("Sorry! A ZeroDivisionError occured. Please do not try to divide by zero.")
	print(j)
	time.sleep(10)
except(KeyboardInterrupt) as k:
	print("User input caused a crash.")
	print(k)
	# shouldn't be as much of a problem with threads
	time.sleep(10)
