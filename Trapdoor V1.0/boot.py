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
	username = input("Enter your username: ")
	if username==("ksmit799"): break
	else:
		print("There is no user called", username)	
while 1:
	password = input("Enter your password: ")
	if password==("temple121"): break
	else:
		print("Sorry that password is incorrect please try again!")		
print("Welcome", username)	
time.sleep(5.5)