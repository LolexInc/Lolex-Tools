import sys, os
sys.path.insert(0, "./ci/build/")
import stats
stats.inactivity = stats.inactivity + 1
os.remove("./ci/build/stats.py")
with open("./ci/build/stats.py", "a") as outf:
	outf.write("inactivity = " + str(stats.inactivity))
os.system("git add *")
os.system("git commit -am 'Bumped stats inactivity number by + 1'")
os.system("git push")
