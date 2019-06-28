X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9

def display_instruct():
"""Display game instructions."""
print(
"""
Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
This will be a showdown between your human brain and my silicon processor.
You will make your move known by entering a number, 0 - 8.
will correspond to the board position as illustrated:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Prepare yourself, human. The ultimate battle is about to begin. \n
"""
)

def ask_yes_no(question):
    """Ask a yes or no question."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no("Do you require the first move?(y/n):")
    if go_first == 'y':
        print("\n Then take the first move. You will need it.")
        human = X
        computer = 0
    else:
        print("\n Your bravery will be your undoing....I will go first.")
        computer = X
        human = 0
    return computer, human