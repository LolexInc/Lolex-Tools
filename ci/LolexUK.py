import time, os
a = time.asctime(time.localtime(time.time())).split()
if a[1] == "Aug" and a[2] == "1" and a[4] == "2018":
	os.remove("./README.md")
	os.rename("./README.md.new", "./README.md")
	os.remove("./.travis.yml")
	os.rename("./travis.yml.old", "./.travis.yml")
	os.remove("./ci/LolexUK.py")
	os.system("git add *")
	os.system("git commit -am 'Official update to the LolexUK name'")
	os.system("git push")
else:
	print("Not August 1st + yet")
