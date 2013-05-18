#This is the boot
import time
print ("Boot Menu")
print ("Boot 1.Desktop")
print ("boot 2.Servers")
while 1:
	Booting = input('Enter the name were you would like to boot to: ')
	if Booting=="desktop" or Booting=="1" or Booting=="Desktop":
		print("Booting to desktop")
		break
	elif Booting=="servers" or Booting=="2" or Booting=="Servers":
		print("Booting to Servers")
		break
	else:
		print("There is no option to boot to", Booting)
while 1:
	print("Enter Your Username")
	username = input("Username: ")
	usernameFile = open("username.txt","r")
	if username==usernameFile.read():
		break
	else:
		print("There is no user called", username)	
while 1:
	print("Enter Your Password")
	password = input("Password: ")
	passwordFile = open("password.txt","r")
	if password==passwordFile.read():
		break
	else:
		print("That Password is incorrect")
print("Welcome", username)
time.sleep(5.5)