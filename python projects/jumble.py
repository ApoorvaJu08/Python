import random
WORDS = ("python", "jumble", "easy", "difficult", "answer", "xylophone")
word = random.choice(WORDS)
correct = word
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]
print(
    """ 
        Welcome to word Jumble!
    Unscrambel the letters to make a word.
    (Press the enter key at the prompt to quit.)
    """ 
)
print("The jumble is", jumble)
guess = input("\n Your guess: ")
while guess != correct and guess != " ":
    print("Sorry, that's not it")
    guess = input("Your guess: ")
if guess == correct:
    print("That's it! You guessed it! \n")
print("Thanks for playing.")
input("\n\n Press the enter key to exit.")