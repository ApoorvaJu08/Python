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