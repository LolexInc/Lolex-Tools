@echo off
set /P proxy=Enter a capital Y if you are using a proxy or anything else if you aren't using a proxy or you don't know what this means: 
IF "%proxy%"=="Y" (
	set /P proxy_address="Enter your proxy's address in the format proxy_address:port : "
	.\curl\curl -x %proxy_address% --url "https://www.python.org/ftp/python/3.7.0/python-3.7.0-embed-win32.zip" --location --output "./python.zip" --insecure
	.\curl\curl -x %proxy_address% --url "https://github.com/LolexUK/Lolex-Tools/releases/download/vcruntime140.dll_download/vcruntime140.dll" --location --output "./vcruntime140.dll" --insecure
)

IF /I not "%proxy%"=="Y" (
	.\curl\curl --url "https://www.python.org/ftp/python/3.7.0/python-3.7.0-embed-win32.zip" --location --output "./python.zip" --insecure
	.\curl\curl --url "https://github.com/LolexUK/Lolex-Tools/releases/download/vcruntime140.dll_download/vcruntime140.dll" --location --output "./vcruntime140.dll" --insecure
)