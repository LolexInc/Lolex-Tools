@echo off
set /P proxy=Press enter to continue if you are NOT using a proxy. Otherwise refer to README.txt 
.\curl\curl --url "https://www.python.org/ftp/python/3.7.0/python-3.7.0-embed-win32.zip" --location --output "./python.zip" --insecure
.\curl\curl --url "https://github.com/LolexUK/Lolex-Tools/releases/download/vcruntime140.dll_download/vcruntime140.dll" --location --output "./vcruntime140.dll" --insecure
