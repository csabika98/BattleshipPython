import os
import time
# A board is a list of rows, and each row is a list of cells with either an 'X' (a battleship)
# or a blank ' ' (water)
board = []
for i in range(5):
    board.append(["o"] * 5)
# We want to refer to columns by letter, but Python accesses lists by number. So we define
# a dictionary to translate letters to the corresponding number. Note that Python lists start in
# zero, not in one!
letters_to_numbers = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
}


# By writing this as a function, we don't have to repeat it later. It's less code, it makes
# the rest easier to read, and if we improve this, we have to do it only once!
def ask_player_1_user_for_board_position():
    column = input("column (A to E):").lower()
    while column not in "abcde":
        print("That column is wrong! It should be A, B, C, D or E")
        column = input("column (A to E):").lower()

    row = input("row (1 to 5):")
    while row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")
        row = input("row (1 to 5):")

    # The code calling this function will receive the values listed in the return statement below
    # and it can assign it to variables
    return int(row) - 1, letters_to_numbers[column]

def ask_player_2_user_for_board_position():
    column = input("column (A to E):").lower()
    while column not in "abcde":
        print("That column is wrong! It should be A, B, C, D or E")
        column = input("column (A to E):").lower()

    row = input("row (1 to 5):")
    while row not in "12345":
        print("That row is wrong! it should be 1, 2, 3, 4 or 5")
        row = input("row (1 to 5):")

    # The code calling this function will receive the values listed in the return statement below
    # and it can assign it to variables
    return int(row) - 1, letters_to_numbers[column]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board(board):
    # Show the board, one row at a time
    print(" ", " ".join("ABCDE"))
    for letter, row in zip('12345', board):
        print(letter, " ".join(row))


# We want 5 battleships, so we use a for loop to ask for a ship 5 times!
for n in range(3):
    print("Player 1 turn, he choose 3 ship")
    print("Where do you want ship ", n + 1, "?")
    row_number, column_number = ask_player_1_user_for_board_position()
   

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")

    board[row_number][column_number] = 'X'
    print_board(board)

time.sleep(1)
# Now clear the screen, and the other player starts guessing
clear_terminal()

guesses_board = []
for i in range(5):
    guesses_board.append(["o"] * 5)



for n in range(3):
    print("Player 2 turn, he choose 3 ship")
    print("Where do you want ship ", n + 1, "?")
    row_number, column_number = ask_player_2_user_for_board_position()
   

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("That spot already has a battleship in it!")

    board[row_number][column_number] = 'X'
    # print_board(board)

time.sleep(1)
# Now clear the screen, and the other player starts guessing
clear_terminal()

guesses_board = []
for i in range(5):
    guesses_board.append(["o"] * 5)

# Keep playing until we have 5 right guesses
guesses = 0
while guesses < 5:
    print("Guess a battleship location")
    row_number, column_number = ask_player_1_user_for_board_position()
    

    if guesses_board[row_number][column_number] != 'o':
        print("You have already guessed that place!")
        continue

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("HIT!")
        guesses_board[row_number][column_number] = 's'
        guesses = guesses + 1
    else:
        guesses_board[row_number][column_number] = 'm'
        print("MISS!")

    print_board(guesses_board)
print("GAME OVER!")

guesses = 0
while guesses < 5:
    print("Guess a battleship location")
    row_number, column_number = ask_player_2_user_for_board_position()
    

    if guesses_board[row_number][column_number] != 'o':
        print("You have already guessed that place!")
        continue

    # Check that there are no repeats
    if board[row_number][column_number] == 'X':
        print("HIT!")
        guesses_board[row_number][column_number] = 's'
        guesses = guesses + 1
    else:
        guesses_board[row_number][column_number] = 'm'
        print("MISS!")

    print_board(guesses_board)
print("GAME OVER!")
