import time
print('Hello and welcome to Alvantia')
print("Let's begin what is your name?")
name = input("Name: ")
print("Your name is", name)
time.sleep(2.2)
print("...... One day,", name, "is walking through a forest when all of a sudden")
print("A goblin leaps out of the bush!")
print("would you like to 1.Attack or 2.Defend?")
while 1:
	attack1 = input("1.Attack or 2.Defend?: ")
	if attack1=="attack" or attack1=="Attack" or attack1=="1":
		print("You attack the goblin and slay it collecting 5 coins!")
		break
	elif attack1=="Defend" or attack1=="defend" or attack1=="2":
		print("You defend the goblins attack, and the goblin runs away")
		break
print("I need to find the village to upgrade my equipment")
time.sleep(2.2)
print("3 Days later.....")
time.sleep(2.2)
print("Yay im at the village now what should i do")
while 1:
	decision1 = input("Should i go to the 1.Blacksmith or the 2.Armoury: ")
	if decision1=="blacksmith" or decision1=="Blacksmith" or decision1=="1":
		print("You walk over to the Blacksmith.")
		break
	elif decision1=="Armoury" or decision1=="armoury" or decision1=="2":
		print("You walk to the Armoury")
		break
print("Hello what would you like to buy?")
if decision1=="blacksmith" or decision1=="Blacksmith" or decision1=="1":
	print("A.Iron Sword(5 coins), B.Iron Shield(7 coins).")
elif decision1=="armoury" or decision1=="Armoury"or decision1=="2":
	print("1.Iron Armour(8 coins), 2.Iron Chaps(5 coins).")
if attack1=="attack" or attack1=="Attack" or attack1=="1":
	while 1:
		buy1 = input("I would like to buy: ")
		if buy1=="Iron Chaps" or buy1=="2":
			print("You buy 1 Iron Chaps")
			break
		elif buy1=="Iron Sword" or buy1=="a" or buy1=="A":
			print("You buy 1 Iron Sword")
			break
		elif buy1=="Iron Shield" or buy1=="B" or buy1=="b":
			print("You don't have enough money for that!")
		elif buy1=="Iron Armour" or buy1=="1":
			print("You don't have enough money for that!")
elif attack1=="Defend" or attack1=="defend" or attack1=="2":
	time.sleep(2.2)
	print("Crap you mutter suddenly realizing that you have no money")
print("Now what should i do?")
print("Hint: Type List for a list of actions you can do")			
time.sleep(5.5)	