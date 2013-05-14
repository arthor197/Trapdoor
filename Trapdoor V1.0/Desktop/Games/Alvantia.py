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
else:
	print("You defend the goblins attack, and the goblin runs away")
print("I need to find the village to upgrade my equipment")
print("3 Days later.....")
print("Yay im at the village now what should i do")
decision1 = input("Should i go to the blacksmith or the armoury?: ")
if decision1==("blacksmith"):
	print("You walk over to the Blacksmith.")
else:
	print("You walk to the Armoury")
print("Hello what would you like to buy?")
if decision1==("blacksmith"):
	print("Iron Sword(5 coins), Iron Shield(7 coins).")
else:
	print("Iron Armour(8 coins), Iron Chaps(5 coins).")
time.sleep(5.5)	