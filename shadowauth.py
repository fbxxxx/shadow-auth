#!/usr/bin/python3
import spwd
from crypt import crypt
from getpass import getpass

while True:
	username = input("Username: ")
	password = getpass("Password: ")

	try:
		shadow_username = spwd.getspnam(username)
		shadow_password = shadow_username.sp_pwd

		clean_salt = shadow_password.split("$")[2]
		hashtype = shadow_password.split("$")[1]
		salt_for_crypt = "${}${}".format(hashtype, clean_salt)

		encrypted_password = crypt(password, salt=salt_for_crypt)

		if encrypted_password == shadow_password:
			print('\033[1;32m'+"[+] Login successful!\n"+'\033[0m')
			break
		else:
			print('\033[1;31m'+"[-] Invalid login credentials!\n"+'\033[0m')
			pass
	except:
		print('\033[1;31m'+"[!!] Invalid login credentials\n"+'\033[0m')
