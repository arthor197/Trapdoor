import time
print('Hello and welcome to Alvantia')
print("Let's begin what is your name?")
name = input("Name: ")
print("your name is", name)
print("...... One day,", name, "is walking through a forest when all of a sudden")
print("A goblin leaps out of the bush!")
print("would you like to defend or attack?")
attack1 = input("Attack or defend?: ")
if attack1==("attack"):
	print("You attack the goblin and slay it collecting 5 coins!")
	fob = open('C:/Users/Kyle/Documents/GitHub/Trapdoor/Trapdoor V1.0/Alvantia Game info.txt', 'w')
	fob.write("You have 5 coins!")
	fob.close()
else:
	print("You defend the goblins attack, and the goblin runs away")
time.sleep(5.5)
