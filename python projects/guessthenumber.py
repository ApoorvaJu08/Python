import random
secretNumber = random.randint(1,20)
print('I am thinking of a number between 1 and 20')

#ask the player to guess 6 times
for guesstaken in range(1,7):
	guess = int(input('take a guess'))
	if guess < secretNumber:
		print('Your guess is too low.')
	elif guess > secretNumber:
		print('Your number is too high.')
	else:
		break
if guess == secretNumber:
	print('Good job! you have guessed my number in ' + str(guesstaken) + 'guesses!')
else:
	print('Nope. The number I was thinking of was ' + str(secretNumber))
