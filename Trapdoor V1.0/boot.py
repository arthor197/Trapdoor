#This is the boot
import time
check = "1"
checkFile = open("check.txt","r")
if check==checkFile.read():
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
else:
	print("Hello and welcome to Trapdoor V1.0")
	print ("Let's begin what do you want your username to be?")
	username = input("Enter your desired username: ")
	print("Thats a nice username", username)
	print ("Now how old are you?")
	age = input('Enter your age: ')
	print ("Ok so you're", age)
	password = input("What would you like your password to be?: ")
	print("Ok lets setup your wifi")
	wifi = input("Whats your wifi name?: ")
	wifipass = input("Ok and whats the password?: ")
	print("Attempting to join", wifi)
	time.sleep(2.2)
	print("Joined", wifi,"!")
	while 1:
		print("So your username is", username)
		print("And your age is", age)
		print("The wifi you connected to is", wifi)
		print("Your password will be", password)
		user = input("So all this information correct?: ")
		if user=="No" or user=="no" or user=="n" or user=="N":
			print("Okay then quit and try again") 
		elif user=="Yes" or user=="yes" or user=="y" or user=="Y": break	
		usernameFile = open("username.txt","w")
		usernameFile.write(username)
		usernameFile.close()
		passwordFile = open("password.txt","w")
		passwordFile.write(password)
		passwordFile.close()
		usernameFile = open("check.txt","w")
		usernameFile.write("1")
		usernameFile.close()
	print("Setting up Files")
	time.sleep(2.2)	
	print("Ok close this window and re-run boot.py to log in!")
time.sleep(7.7)