import random
score = 0
while True:
	botact = random.randint(1,3)
	botsym = 0
	if botact == 1:
		botsym = "Rock"
	elif botact == 2:
		botsym = "Papper"
	elif botact == 3:
		botsym = "Scissor"

	useract = input("""
Rock, Papper or Scissor ?
	""")
	print("Your score is " + str(score))
	print("You played "  + useract + ", the bot played " + botsym )
	if useract == botsym:
		print("Match draw")
	elif (useract =="Scissor" and botsym == "Rock") or (useract =="Rock" and botsym == "Papper") or (useract =="Papper" and botsym == "Scissor"):
		print("You loose")
	elif (useract =="Rock" and botsym == "Scissor") or (useract =="Papper" and botsym == "Rock") or (useract =="Scissor" and botsym == "Papper"):
		print("You won")
		score += 1
	elif useract == "quit":
		exit("Goodbye !")
	else:
		print("That's not an option, you cheater !")
