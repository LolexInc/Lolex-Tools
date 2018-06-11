import time, os
a = time.asctime(time.localtime(time.time())).split()
if a[1] == "Jun" and a[2] == "11":
	os.remove("./README.md")
	os.rename("./README.md.new", "./README.md")
	os.remove("./.travis.yml")
	os.rename("./travis.yml.old", "./travis.yml")
	os.remove("./ci/LolexUK.py")
	os.system("git add *")
	os.system("git commit -am 'Official update to the LolexUK name'")
	os.system("git push")
