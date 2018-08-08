import os, time
proxy = input("Enter Y if you are using a proxy or enter anything else if you aren't or you don't know what this means. ")
if proxy == "Y":
	os.system(".\curl\curl -x " + input("Enter your proxy in the format proxy_address:port") + " --url https://github.com/lolexuk/lolex-tools/zipball/latest --location --insecure --output ./package.zip")
else:
	os.system(".\curl\curl --url https://github.com/lolexuk/lolex-tools/zipball/latest --location --insecure --output D:/package.zip")