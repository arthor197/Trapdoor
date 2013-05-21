#Imports
import time
import math
#Dictonaries
#Programs
def calculator():
    print("Choose your calculation type")
    print("    1)Addition")
    print("    2)Subtraction")
    print("    3)Multiplication")
    print("    4)Division")
    calc1 = input("Which one: ")
    if calc1=="1":
        print("You Chose Addition!")
        x = input("First number: ")
        y = input("Plus: ")
        num1 = int(x)
        num2 = int(y)
        ans = num1+num2
        time.sleep(0.5)
        print("Answer: ", ans)
        time.sleep(3.0)
    elif calc1=="2":
        print("You Chose Subtration")
        x = input("First Number: ")
        y = input("Minus: ")
        num1 = int(x)
        num2 = int(y)
        ans = num1-num2
        time.sleep(0.5)
        print("Answer: ", ans)
        time.sleep(3.0)
    elif calc1=="3":
        print("You Choise Multiplication")
        x = input("First Number: ")
        y = input("Times: ")
        num1 = int(x)
        num2 = int(y)
        ans = num1*num2
        time.sleep(0.5)
        print("Answer: ", ans)
        time.sleep(3.0)
    elif calc1=="4":
        print("You Chose Division")
        x = input("First Number: ")
        y = input("Devided by: ")
        num1 = int(x)
        num2 = int(y)
        ans = num1/num2
        time.sleep(0.5)
        print("Answer: ", ans)
        timesleep(3.0)
    else:
        print("You didn't Pick a type... ")
        time.sleep(0.5)
        calculator()
def traptalk():
    print("Tip: Start of by saying Hello or List for a list of chat options")    
    while 1:
        traptalk1 = input("TrapTalk: ")
        if traptalk1=="Hello" or traptalk1=="hello":
            print("TrapTalk Says: Hello")
        elif traptalk1=="quit" or traptalk1=="quit":
            break
        elif traptalk1=="list" or traptalk1=="List":
            print("You could say:")
            print(" Hello")
            print("Or")
            print("quit (To quit TrapTalk)")
        else:
            print("I don't know what you mean by", traptalk1)
#Dictonary Startup
def boot():
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
                print("Welcome",username)           
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
        print("So your username is", username)
        print("And your age is", age)
        print("The wifi you connected to is", wifi)
        print("Your password will be", password)
        while 1:
            user = input("So all this information correct?: ")
            if user=="No" or user=="no" or user=="n" or user=="N":
                print("Okay then quit and try again")
            elif user=="Yes" or user=="yes" or user=="y" or user=="Y": 
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
                print("Welcome",username)
                break
time.sleep(1.0)
def logout():
    print("Logging out")
    time.sleep(3.0)
    boot()
#Main User Input
boot()
print("Tip: Type list for a list of commands!")
while 1:
    input1 = input("Trapdoor: ")
    if input1=="calculator" or input1=="1":
        calculator()
    elif input1=="list" or input1=="List":
        print("Programs:")
        print(" 1.Calculator")
        print(" 2.TrapTalk")
        print("Options:")
        print(" 3.Logout")
    elif input1=="TrapTalk" or input1=="traptalk" or input1=="2":
        traptalk()
    elif input1=="Logout" or input1=="logout" or input1=="3":
        logout()
    #elif input1==
    else:
        print("I don't know what you mean by", input1)