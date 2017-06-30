import os
from lib import LolexToolsMethods
if os.path.exists("./update/90/9.0alpha0patch1.py") and (os.path.isdir("./update/90/9.0alpha0patch1.py")) == False:
	pass
else:
	LolexToolsMethods.addplugins(True)
