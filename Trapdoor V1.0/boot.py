
#This is the boot
import time
print ("Boot Menu")
print ("Boot 1.Desktop")
print ("boot 2.Servers")
Booting = input('Enter the name were you would like to boot to: ')
print("Booting to", Booting)
username = input("Enter your username: ")
password = input("Enter your password: ")
if password==("temple121"):
	print("Welcome", username)
else:
	print("Sorry that password is incorrect. Please try again!")
time.sleep(5.5)