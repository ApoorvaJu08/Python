for i in range(1,3):
	guess = int(input("Guess: "))
	answer = 42
	if answer < guess:
		print("Too Low")
	elif answer == guess:
		print("Correct")
		break
	else:
		print("Too High")
