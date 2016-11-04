import shutil
try:
	shutil.rmtree("./Lolex-Tools")
except(IOError):
	pass
try:
	shutil.copytree("/sdcard/Lolex-Tools/","./Lolex-Tools")
except():
	print("Please extract this program to /sdcard/")