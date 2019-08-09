#! python3
# 0
#  0                000000   0         000000     0  0         000000000   00000000    00000000   0          000000
#   0              00     0  0         0           00             00       0      0    0      0   0          0
#    0             00     0  0         00000       00   000000    00       0      0    0      0   0          00000
#     0            00     0  0         0          0  0            00       0      0    0      0   0              0
#      0000000      000000   0000000   000000    0    0           00       00000000    00000000   0000000   000000
#
# authors = Monkeyboy2805
import sys


class AddUser:
	def setup_folder(self):
		pass

	def add_user_to_file(self):
		pass


class Authenticate:
	@staticmethod
	def login():
		try:
			sys.path.insert(0, "./project/new/setup/exp/TEST")
			import users
			usernameenter = input("Please enter your username.")
			if usernameenter in users.users:
				path = users.paths[users.users.index(usernameenter)] # NOTE: the local variable path will be used at some point, but there isn't enough functionality for it to be used as of yet
				print("Welcome " + (str(usernameenter)))
			else:
				return 1
		except ImportError:
			return 2
