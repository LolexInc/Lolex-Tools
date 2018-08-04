set /P proxy=Enter Y if you are using a proxy or N if you aren't using a proxy or you don't know what this means
if "%proxy%"=="Y" (
	set /P "proxy_address=Enter your proxy's address in the format proxy_address:port"
)
echo "WTF"
if DEFINED proxy_address (
	.\curl\curl -x %proxy_address% --url "https://www.python.org/ftp/python/3.7.0/python-3.7.0-embed-win32.zip" --location --output "D:/python.zip" --insecure
	.\curl\curl -x %proxy_address% --url "https://github.com/LolexUK/Lolex-Tools/releases/download/vcruntime140.dll_download/vcruntime140.dll" --location --output "D:/vcruntime140.dll" --insecure
)
powershell.exe -nologo -noprofile -command "& { $shell = powershell Expand-Archive D:/python.zip -DestinationPath D:/Python_TEST }