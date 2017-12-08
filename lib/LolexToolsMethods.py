#! python3
##0
## 0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
##  0              00     0  0         0           00             00       0      0    0      0   0          0
##   0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
##    0            00     0  0         0          0  0            00       0      0    0      0   0              0
##     0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
##
## authors = Monkeyboy2805
import os, time, py_compile, shutil, sys, platform, threading, subprocess, random
if sys.version_info.minor > 6 and (sys.version_info[1] == 7 and sys.version_info[2] == 0 and sys.version_info[3] == "alpha" and sys.version[4] == 0) == False:
    IOError = OSError
print ("Module LolexToolsMethods is running, using modules os, time, py_compile, shutil, sys, platform, threading.")
s = os.sep
sys.path.insert(0, "./")
if platform.system() == "Windows":
    if sys.version_info.minor > 5:
        py = "py ." + os.sep
        pyo = "py"
    else:
        py = "python ." + os.sep
        pyo = "python"
elif platform.system() == "Linux":
    py = "python3 " + os.sep
    pyo = "python3"
stopping = False
class uos:
    useros = platform.system()
    if os.path.exists("/system/build.prop") == True and not(os.path.isdir("/system/build.prop")) and platform.system() == "Linux":
        useros = "Android"
class threads:
    shutdown = False
    logoff = False
    restart = False
    hibernate = False
try:
    import restartsettings, logoffsettings, hibernatesettings, exitsettings, shutdownsettings, menusettings, LolexToolsOptions, theme
except(ImportError) as e:
    print((str(e)) + " occured.")
    time.sleep(1)
try:
    import ver
except(ImportError) as e:
    print("Please redownload this repository to access all features.")
    print(e)
    time.sleep(5)
class title_updater:
    threads = 2
    notificationsmsg = []
    notificationsdelay = []
    a = round(time.time(), 0)
    units = ["weeks", "days", "hours", "minutes", "seconds"]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_unit = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    start_month_str = time.asctime(time.localtime(time.time())).split(" ")[1]
    start_month = -1
    for i in range(0, len(months) - 1):
        if start_month_str == months[i]:
            start_month = i - 1
            break
    if uos.useros == "Windows":
        title_cmd_start = "TITLE "
        title_cmd_end = ""
    elif uos.useros == "Linux" or uos.useros == "Android":
        title_cmd_start = "\x1b]2;"
        title_cmd_end = "\x07"
def get_current_datetime():
    a = time.asctime(time.localtime(time.time()))
    a = a.split(" ")
    b = a[3] + " "
    del a[3]
    for i in range(0, 4):
        b = b + a[i] + " "
    return b
def titleUpdater():
    start = title_updater.a
    end = title_updater.a
    load = 0
    global stopping
    while stopping != True:
        if stopping == True:
            break
        if len(title_updater.notificationsmsg) == 0:
            start = time.time()
            #os.system("TITLE Lolex-Tools|    " + (str(title_updater.threads)) + " threads|  Uptime: " + (str(round(time.time(), 0) - title_updater.a)) + " seconds" + (str(time.localtime(time.asctime(time.time())))))
            newtitle = title_updater.title_cmd_start + " Lolex-Tools    " + (str(title_updater.threads)) + " threads  Uptime: " #+ (str(round(time.time(), 0) - title_updater.a)) + " seconds    " + (str(time.time()))
            #print(round(time.time(), 0) - title_updater.a)
            timer = convert_time_all(True, seconds = round(time.time(), 0) - title_updater.a)
            #print(timer)
            #t = len(timer) - 1
            #while t != -1:
                #newtitle = newtitle[t] + (str(timer[t]) + "" + (title_updater.units[t]))
                #print(newtitle)
                #t = t - 1
            #for i in range(0, len(timer) - 1):
                    #j = len(timer) - i - 1
                    #if timer[j] != 0:
                            #newtitle = newtitle + str(timer[i]) + "" + (str(title_updater.units[i]))
            newtitle = newtitle + (str(timer))
            #newtitle = newtitle + title_updater.title_cmd_end
            newtitle = newtitle + "    " + (str(get_current_datetime())) + "    Load: " + (str(load)) + "%" + title_updater.title_cmd_end
            # FIX THE LOAD THING ...
            if uos.useros == "Linux" or uos.useros == "Android":
                    sys.stdout.write(newtitle)
            else:
                    os.system((str(newtitle)))
            time.sleep(1)
            end = time.time()
            load = round((float((end - start - 1) * 100)), 2)
            if load > 100:
                send_notification("WARNING: Overloading. Took " + str(round(float(load - 100)/100), 2) + " seconds too long too tick.", 3)
                load = 100
        else:
            if uos.useros == "Linux" or uos.useros == "Android":
                sys.stdout.write(title_updater.title_cmd_start + (str(title_updater.notificationsmsg[0])) + title_updater.title_cmd_end)
            else:
                os.system(title_updater.title_cmd_start + (str(title_updater.notificationsmsg[0])) + title_updater.title_cmd_end)
            time.sleep(title_updater.notificationsdelay[0])
            del title_updater.notificationsdelay[0]
            del title_updater.notificationsmsg[0]
    if uos.useros == "Linux" or uos.useros == "Android":
        sys.stdout.write("\x1b]2;Lolex-Tools: EXITING...\x07")
    else:
        os.system("TITLE Lolex-Tools: EXITING...")
def _init_():
        title_thread = threading.Thread(target = titleUpdater, args = [])
        title_thread.start()
def version():
        print(ver.version)
def convert_time_all(rtstr, seconds = 0, minutes = 0, hours = 0, days = 0, weeks = 0, start_month = title_updater.start_month, months = 0):
    # Have a look into datetime for this
    string_out = ""
    if seconds >= 60:
        minutes = minutes + seconds//60
        seconds = seconds%60
    if minutes >= 60:
        hours = hours + minutes//60
        minutes = minutes%60
    if hours >= 24:
        days = days + hours//24
        hours = hours%24
    if days >= 7:
        weeks = weeks + days//7
        days = days%7
    #while weeks >= 4: #and days >= title_updater.month_unit[(start_month + (months%12))%12]:
        #weeks = weeks - 4
        # Based on a month being 4 weeks
        #days = days - title_updater.month_unit[(start_month + (months%12))%12]
        #months = months + 1
    if rtstr == True:
        #if months != 0:
            #if months != 1:
               #string_out = string_out + (str(months)) + " months "
            #else:
                #string_out = string_out + (str(months)) + " month "
        if weeks != 0:
            if weeks != 1:
                string_out = string_out + (str(weeks)) + " weeks "
            else:
                string_out = string_out + (str(weeks)) + " week "
        if days != 0:
            if days != 1:
                string_out = string_out + (str(days)) + " days "
            else:
                string_out = string_out + (str(days)) + " day "
        if hours != 0:
            if hours != 1:
                string_out = string_out + (str(hours)) + " hours "
            else:
                string_out = string_out + (str(hours)) + " hour "
        if minutes != 0:
            if minutes != 1:
                string_out = string_out + (str(minutes)) + " minutes "
            else:
                string_out = string_out + (str(minutes)) + " minute "
        if seconds != 0:
            if seconds != 1:
                string_out = string_out + (str(seconds)) + " seconds "
            else:
                string_out = string_out + (str(seconds)) + " second "
        string_out = string_out.replace(".0", "")
        return string_out
    #return months,
    return weeks, days, hours, minutes, seconds
def send_notification(msg, delay):
    title_updater.notificationsmsg.append("Lolex-Tools NOTIFICATION: " + (str(msg)))
    title_updater.notificationsdelay.append(delay)
def str_to_int(string):
    try:
        a = int(string)
    except(ValueError):
        return False
    return True
def flicker():
    a = input("Are you sure you wish to continue? 1 (yes) or 0 (no).Please don't continue if you have epilepsy.")
    if str_to_int(a) == True and int(a) == 1:
        howlongtoflashfor = input("How many loops do you wish to occur?")
        if str_to_int(howlongtoflashfor) == True:
            howlongtoflashfor = int(howlongtoflashfor)
        else:
            howlongtoflashfor = random.randint(1, 1000)
            print("TYPE of loops was not a number, selected " + (str(howlongtoflashfor)))
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
    done = "0"
    colour = []
    while done != "1":
        colour.append("color " + input("Please enter your colour "))
        done = input("Please enter 1 if you are finished adding colours.")
    #colour = ("color " + input("Please enter your first colour "), "color " + input("Please enter your second colour "), "color " + input("Please enter your third colour "), "color " + input("Please enter your fourth colour "), "color " + input("Please enter your fifth colour  "))
    flickerthread = threading.Thread(target = flickerp2, args = [colour, howlongtoflashfor])
    flickerthread.start()
def flickerp2(colour, howlongtoflashfor):
    currentflashes = int(0)
    global stopping
    while howlongtoflashfor != currentflashes:
        if stopping == True:
            break
        for i in range(0, len(colour) - 1):
            os.system(colour[i])
            print("STARTED")
            pass
##        os.system (colour[0])
##        pass
##        os.system (colour[1])
##        pass
##        os.system (colour[2])
##        pass
##        os.system (colour[3])
##        pass
##        os.system (colour[4])
##        pass
        currentflashes = currentflashes + 1
    os.system(theme.theme)
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
        #print("23 = Update")
        print("23 = Start File Explorer\n")
    if layout == 1:
        print("24 = Next Page")
        print("25 = Back a Page")
    else:
        if page < 5:
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
        androidpage(page, layout)
def restart():
    restart_confirm = input("Please enter 1 to confirm restart.")
    if restart_confirm == "1":
        waittime = float(input("How long, in minutes do you wish to wait?"))
        while waittime < 0:
            waittime = float(input("Please select a time bigger than 0 minutes.\nHow long, in minutes, do you wish to wait?"))
        restartthreader = threading.Thread(target = restartthread, args = [waittime])
        restartthreader.start()
def logoff(type_of):
    logoff_confirm = input("Please enter 1 to confirm logoff.")
    if logoff_confirm == "1":
        waittime = float(input("How long, in minutes, do you wish to wait?"))
        while waittime < 0:
            waittime = float(input("Please select a time bigger than 0 minutes.\nHow long, in minutes, do you wish to wait?"))
        loggeroff = threading.Thread(target = logoffthread, args = [waittime, type_of])
        loggeroff.start()
def logoffthread(waittime, type_of):
    if threads.logoff == True:
        print("LOGOFF thread: Logoff already scheduled!")
        return;
    threads.logoff = True
    waittime = waittime * 60
    while waittime > 0.1 and stopping == False:
        time.sleep(0.1)
        waittime = waittime - 0.1
    if stopping != True:
        print("LOGOFF thread: Logging off...")
        if uos.useros != "Linux":
            if type_of == 0:
                os.system("shutdown -l -f")
            else:
                subprocess.Popen("logoff.exe")
        else:
            os.system("gnome-session-quit --force")
    else:
        print("LOGOFF thread: Stopping...")
    threads.logoff = False
def hibernate():
    hibernate_confirm = input("Please enter 1 to confirm logoff.")
    if hibernate_confirm == "1":
        waittime = float(input("How long, in minutes, do you wish to wait?"))
        while waittime < 0 and waittime > 65505:
            waittime = float(input("Please select a time between 0 - 65505 minutes.\nHow long, in minutes, do you wish to wait?"))
        hibernatethreader = threading.Thread(target = hibernatethread, args = [waittime])
        hibernatethreader.start()
def hibernatethread(waittime):
    if threads.hibernate == True:
        print("HIBERNATE thread: Hibernate already scheduled!")
        return;
    threads.hibernate = True
    waittime = waittime * 60
    while waittime > 0.1 and stopping == False:
        time.sleep(0.1)
        waittime = waittime - 0.1
    if stopping != True:
        print("HIBERNATE thread: Hibernating...")
        if uos.useros == "Windows":
            os.system("shutdown -h -f")
        elif uos.useros == "Linux":
            os.system("systemctl suspend")
    else:
        print("HIBERNATE thread: Stopping...")
    threads.hibernate = False
def restartthread(waittime):
    if threads.restart == True:
        print("RESTART thread: restart already scheduled!")
        return;
    threads.restart = True
    waittime = waittime * 60
    while waittime > 0.1 and stopping == False:
        time.sleep(0.1)
        waittime = waittime - 0.1
    if stopping != True:
        print("RESTART thread: Restarting device...")
        if uos.useros != "Linux":
            os.system("shutdown -r -f")
        else:
            if uos.useros == "Android":
                if os.system("su -c reboot") != 0:
                    os.system("reboot")
            else:
                    os.system("reboot")
    else:
        print("RESTART thread: Stopping...")
    threads.restart = False
def shutdown(type_of):
    shutdown_confirm = input("Please enter 1 to shutdown.")
    if shutdown_confirm == "1":
        waittime = float(input("How long, in minutes, do you wish to wait?"))
        while waittime < 0 or waittime > 65505:
            waittime = float(input("Please select a time between 0- 65505 minutes.\nHow long, in minutes, do you wish to wait?"))
        shutdownthreader = threading.Thread(target = shutdownthread, args = [waittime, type_of])
        shutdownthreader.start()
def shutdownthread(waittime, type_of):
    if threads.shutdown == True:
        print("SHUTDOWN thread: Shutdown already scheduled!")
        return;
    threads.shutdown = True
    waittime = waittime * 60
    while waittime > 0.1 and stopping == False:
        time.sleep(0.1)
        waittime = waittime - 0.1
    if stopping != True:
        print("SHUTDOWN thread: shutting device down...")
        if uos.useros == "Windows":
            if type_of == 0:
                os.system ("shutdown -s -f")
            elif type_of == 1:
                subprocess.Popen("shutdown.exe")
        elif uos.useros == "Linux":
            os.system("poweroff")
        elif uos.useros == "Android":
            if os.system("su -c reboot -p") != 0:
                if os.system("/system/bin/reboot -p") != 0:
                    print("Failed to execute reboot binary.")
    else:
        print("SHUTDOWN thread: Stopping...")
    threads.shutdown = False
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
    global stopping
    confirmscriptrestart = int(input("Please input 1 to confirm restarting of this script."))
    if confirmscriptrestart == 1:
        stopping = True
        os.system(py + "start.py")
        os._exit(0)
def numops():
    print("Here is a list of operations:")
    print("1 = Add")
    print("2 = Take")
    submode = int(input("Please enter the number of the operation you wish to perform."))
    if submode == 1 or submode == 2:
        addortake()
def addortake():
    startnum = int(input("Please enter your starting number."))
    addortakenum = int(input("Please input the number to be added."))
    endnum = int(input("Please enter your end number."))
    waittime = float(input("How many seconds do you wish to wait before each operation is performed?"))
    while waittime > 4194304 or waittime < 0:
        waittime = float(input("Please select a time in between 0 and 4194304 seconds.\nHow long, in minutes do you wish to wait?"))
    if endnum > startnum:
        while endnum > startnum:
            print(startnum)
            if addortakenum < int(0):
                startnum = startnum - addortakenum
            elif addortakenum > int(0):
                startnum = startnum + addortakenum
            time.sleep(waittime)
    if startnum > endnum:
        while startnum > endnum:
            print (startnum)
            if addortakenum < 0:
                startnum = startnum + addortakenum
            if addortakenum > 0:
                startnum = startnum = startnum - addortakenum
            time.sleep(waittime)
    print ("The closest number to your target end number was:" + (str(startnum)))
    time.sleep(1)
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
        global stopping
        stopping = True
        os.system(py + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
        exit(0)
def uptime():
    if uos.useros == "Android":
        if os.system("su -c uptime") != 0:
            if os.system("/system/bin/uptime") != 0:
                print("Failed to run uptime script.")
    else:
        os.system("uptime")
def compiler(name):
    try:
        os.remove("./" + name + ".pyc")
    except(IOError):
        pass
    py_compile.compile(name + ".py","./" + name + ".pyc")
    os.remove("./" + name + ".py")
def modehide(name, state):
    if state == False:
        newstate = True
    else:
        newstate = False
    try:
        os.remove("./" + name + ".py")
        os.remove("./" + name + ".pyc")
    except(IOError):
        pass
    with open ("./" + name + "settings.py","a") as outf: 
        outf.write("hidden = ")
        outf.write(str(newstate))
def bak(name, path, reinstall, attrestore, regenerate):
    import LolexToolsOptions
    try:
        os.remove(path + name + ".py")
    except(IOError, OSError):
        pass
    try:
        os.remove(path + name + ".pyc")
    except(IOError, OSError):
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
            with open (path + name + ".py", "a") as outf: outf.write("hidden = False")
        else:
            with open (path + "menusettings.py", "a") as outf: outf.write("layout = 0")
        if LolexToolsOptions.compiler == True:
            compiler(path + name + ".py")
        #os.system(py + s + "main" + s + "LolexTools.py")
        #exit(None)
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
        # os.system(py + "main" + s + "LolexTools.py")
        #exit(None)
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
                    #os.system(py + "main" + s + "LolexTools.py")
                    #exit(None)
        if found == False:
            os.system(py + "setup" + s + "generic" + s + "LolexToolsInstaller.py")
            exit(0)
def dirdisc(rtfiles, rtfolders, stpath, validator):
    stpath = correctpath(stpath)
    folders = [stpath]
    files = []
    arraypos = 0
    while arraypos < len(folders):
        path = correctpath(folders[arraypos])
        if validate(path) == True:
            cont = os.listdir(path)
        else:
            cont = []
        tarraypos = 0
        while tarraypos < len(cont):
            if validator == True:
                filev = validatefile(path + cont[tarraypos])
                folderv = validate(path + cont[arraypos])
            else:
                filev = os.path.isfile(path + cont[tarraypos])
                folderv = os.path.isdir(path + cont[tarraypos])
            if filev == True:
                files.append(path + cont[tarraypos])
            if folderv == True:
                folders.append(path + cont[tarraypos] + "/")
            if folderv == True and filev == True:
                for i in range(0, len(cont) - 1):
                    if cont[i] == cont[tarraypos] and i != tarraypos:
                        del cont[i]
                        break;
            tarraypos = tarraypos + 1
        arraypos = arraypos + 1
    if rtfiles == 1 and rtfolders == 1:
        folders.append("END_OF_ARRAY<>")
        return folders + files;
    elif rtfiles == 1:
        return files;
    elif rtfolders == 1:
        return folders;                                                                                                           
def correctfile(path):
    print(path)
    slash = "\\"
    if path[0] == "." and path[1] == "/":
        tlen = 2
        path = correctpath(os.getcwd()) + path[:midlen] + path[midlen + 2:]
    if len(path) > 2:
        path = path.replace(slash[0], "/")
        path = path.replace("//", "/")
        print(2, path)
    if path[len(path) - 1] == "/":
        path = path[:len(path) - 1]
        print(3, path)
    return path;
def validatefile(path):
    if validate(path) == True:
        return "WrongFunction";
    path = correctfile(path)
    class a:
        a = path
    valid = True
    try:
        open(a.a, "a")
    except(IOError, OSError) as e:
        print(e)
        valid = False
    return valid;
def correctpath(path):
    slash = "\\"
    class zz:
        p = path
    if len(zz.p) > 2:
        zz.p = zz.p.replace(slash[0], "/")
        if zz.p[0] == "." and zz.p[1] == "/":
            tlen = 2
            zz.p = correctpath(os.getcwd()) + zz.p[:midlen] + zz.p[midlen + 2:]
    if len(zz.p) != 0:
        if zz.p[len(zz.p) - 1] != "/":
            zz.p = zz.p.replace(zz.p, zz.p + "/")
        if len(zz.p) > 2:
            for i in range(0, len(zz.p) - 1):
                            zz.p = zz.p.replace("//", "/")
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
    loaded = False
    if (platform.system() != "Windows" and platform.system() != "Linux"):
        clear = "<>"
    elif uos.useros == "Windows":
        clear = "cls"
    elif platform.system() == "Linux":
        clear = "clear"
def loading(text1):
    start = int(0)
    while expl.loaded == False:
        print("\n\n\n\n\n\n                      " + (str(text1)) + "\n          (" + (str(start)) + ") seconds elapsed.")
        time.sleep(1)
        os.system(expl.clear)
        start = int(start) + int(1)
        if expl.loaded == True:
            return;
        time.sleep(5)
def explorer(tofinishop, rtnofiles, rtnofolders, otext, path, allowexit):
    expl.path = path
    file = 0
    auto = 0
    if expl.clear == "<>":
            return 1;
    while True:
        expl.loaded = False
        o = False
        op = False
        expl.path = correctpath(expl.path)
        y = validate(expl.path)
        if y == False:
            auto = 1
        if auto == 0:
            os.system(expl.clear)
        print("\n " + expl.path + "\n")
        if otext == 0:
            otext = "Start/finish operations on this folder"
        if allowexit == 0:
            exittext = "You cannot exit until the current operation is complete"
        else:
            exittext = "Exit file explorer"
        loadingthread = threading.Thread(target=loading, args=["Loading: Large directories may take a while..."])
        loadingthread.start()
        array = os.listdir(expl.path)
        expl.loaded = True
        time.sleep(1.5)
        print("\n\n///o - " + otext + "\n./ - Go to the CWD\n/// - Reload\n///? - Help\n.. - Up a level\n///exit - " + exittext + "\n///s - Search for files/folders in this directory")
        for i in range(0, len(array)):
            if i == len(array):
                break
            if len(array[i]) > 2:
                if array[i][0] != "~" and array[i][1] != "$":
                    print(array[i])
        expl.file = input("\nSelect/Open (Name): ")
        expl.file = expl.file.lower()
        if expl.file == "///":
            pass
        elif expl.file == ".." or auto == 1:
            ## SORT OUT SO IT LOOKS LIKE A REAL PATH AT SOME POINT
            if len(expl.path) > 1 and "/" in expl.path and not (len(expl.path) == 3 and expl.path[2] == "/" and expl.path.count("/") == 1):
                new = expl.path.split("/")
                del new[len(new) -1]
                actual = new[0]
                if len(new) > 1:
                    for i in range(0 , len(new) - 1):
                        actual = "/" + new[i]
                    expl.path = actual
                elif expl.path == "/" or (len(expl.path) == 3 and expl.path[2] == "/" and expl.path.count("/") == 1):
                    os.system(expl.clear)
                    real = False
                    op = False
                    o = False
                    while real != True:
                        ## FIX THIS FOR EXITING
                        currentdrives = []
                        for i in range(ord("A"), ord("Z")):
                            success = True
                            try:
                                    os.listdir(chr(i) + ":/")
                            except(IOError):
                                    success = False
                            if success == True:
                                    currentdrives.append(chr(i) + ":/")
                        for j in range(0, len(currentdrives) - 1):
                            print(currentdrives[j])
                        expl.path = input("Please input your drive letter.")
                        for k in range(0, len(currentdrives) - 1):
                            if expl.path == currentdrives[k]:
                                    real = True
                                    break;
                else:
                    actual = "/"
                    expl.path = actual
                if expl.path == "/" or len(expl.path) < 3:
                    actual = "/"
                    expl.path = actual
                if auto != 0:
                    auto = 0
        if expl.file == "///?":
            print("Type names from here to enter/select files and folders.")
            time.sleep(5)
        elif expl.file == "///exit":
            if allowexit == 1:
                return 1;
            else:
                print("Operation not completed!")
                time.sleep(5)
        elif expl.file != "///s" and expl.file != "///o" and expl.file != ".." and expl.file != "./":
            o = False
            found = 0
            arraypos = 0
            possibles = []
            if validate(expl.path) == False:
                auto = 1
            else:
                array = os.listdir(expl.path)
                arraylen = len(array)
                while arraypos < arraylen:
                    if array[arraypos].lower() == expl.file:
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
                if found == 1:
                    expl.newpath = expl.path + possibles[0]
                    if validate(expl.path) == False:
                        auto = 1
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
                        elif file == 3:
                            print("Could not access folder!")
                            time.sleep(3)
                        elif file == 1:
                            if rtnofiles != 1:
                                if rtnofiles == -1:
                                    return [expl.path, possibles[0]]
                                return expl.newpath;
                            o = True
                        elif file == 0:
                            expl.newpath = correctpath(expl.newpath)
                            expl.path = expl.newpath
                            if tofinishop == True or rtnofolders == 0:
                                    return expl.path;
                if found == 0 or "~$" in expl.file:
                    print("No such file or directory found!")
                    file = 5
        elif expl.file == "///s" or expl.file == "///o":
            o = True
        expl.newpath = expl.path
        if file == 1:
            expl.newpath = correctfile(expl.newpath)
        if o == True:
            op = 0
        while op != 7:
            if expl.file == "///s":
                pass
            else:
                print("\n" + expl.newpath + "\n")
                print("Here is a list of operations available: \n1 = Delete\n2 = Create file/folder\n3 = Copy file/folder\n4 = Rename file/folder\n7 = Back")
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
                            break;
                    print("Folders:")
                    for k in range(j, len(search) - 1):
                            print(k + " = " + search[k])
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
                        ### EXITS FOR SOME REASON ON DIR RELOAD
                        op = 7
                        auto = 1
                    else:
                        print("Deleting...")
                        try:
                            os.remove(expl.newpath)
                        except(IOError, OSError) as f:
                            print(f)
                            print("Couldn't delete folder.")
                            time.sleep(3)
                    break;
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
                        else:
                            typ = "folder"
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
            elif op == 3:
                class copy:
                    a = explorer(0, 1, 0, "Select a path to paste", 0)
                if copy.a != 3:
                    if os.path.isdir(expl.newpath):
                        try:
                            shutil.copytree(expl.newpath, a)
                        except(IOError, OSError):
                            print("Could not copy folder!!!")
                            time.sleep(3)
                    elif os.path.isfile(expl.newpath):
                        try:
                            shutil.copy(expl.newpath, a)
                        except(IOError, OSError):
                            print("Could not copy file!!!")
                            time.sleep(3)
            elif op == 4:
                class rename:
                    c = ""
                if len(expl.newpath) > 0:
                    b = expl.newpath.split("/")
                    del b[len(b) -1]
                    for i in range(0, len(b) - 1):
                        rename.c = b[i] + "/"
                try:
                    os.rename(expl.newpath, "/" + rename.c + input("What do you wish the new name to be?"))
                except(IOError, OSError) as e:
                    print(e)
                    print("Could not rename file/folder!")
                    op = 7                    
            if op == 7:
                if tofinishop == 1:
                    return expl.path;
                break;
        if expl.file == "./":
            expl.path = expl.path.replace(expl.path, os.getcwd() + "/")
            expl.newpath = expl.path
            auto = 1
def addplugins(rewrite):
    if rewrite == True:
        try:
            os.remove("./startplugins.py")
        except(IOError, OSError):
            pass
        try:
            os.remove("./startplugins.pyc")
        except(IOError, OSError):
            pass
        w = open("./startplugins.py", "a")
        w.write("import sys\nsys.path.insert(0, './lib')\nfrom LolexToolsMethods import *")
    done = "0"
    while done != "1":
        success = True
        print("You will now enter the explorer to choose your plugin.")
        time.sleep(1.5)
        namepath = explorer(0, -1, 1, 0, "/", 0)
        if namepath[1].endswith(".py") != True and namepath[1].endswith(".pyc") != True:
            success = False
        if success == True:
            path = namepath[0]
            name = namepath[1]
            name = name.replace(".py", "")
            name = name.replace(".pyc", "")
            if " " in name or "	" in name or name.count(".") > 1 or "#" in name or "@" in name or "LolexTools" in name or "{" in name or "}" in name or "/" in name or "&" in name or "|" in name:
                print("Plugin name contains an/several characters that are invalid. Could not load plugin.")
            else:
                w.write('\ntry:\n    sys.path.insert("0, ' + path + '")\n    from ' + (str(name)) + ' import *\nexcept(ImportError) as e:\n    print("Could not load plugin ' + name + ' due to the error below.")\n    print(e)')
        done = input("Please enter 1 if you are done, 0 if not.")
