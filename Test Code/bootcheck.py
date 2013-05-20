import time
check = "1"
checkFile = open("check.txt","r")
if check==checkFile.read():
	print("It works")
else:
	print("It didnt")
time.sleep(5.5)	
