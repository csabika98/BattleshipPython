import random
import os

board = []


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board():
    for i in range(5):
        board.append(["o"] * 5)


def ship_placement(board):
    temp_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    while True:
        position = input("Provide position:")
        row = temp_dict.get(position[0].lower())
        col = int(position[1]) - 1
        if position == "quit":
            print("Goodbye!")
            exit()
        try:
            if position[0].lower() in ["a", "b", "c", "d", "e"] and int(position[1]) in [1, 2, 3, 4, 5]:
                board[row][col] = "o"
                board[row][col] = "x"
            else:
                print("That's not quite good! Please use valid input! ")
                try_ag = input("Do you wanna try again? y/n ")
            if not position[0].lower() in ["a", "b", "c", "d", "e"] and int(position[1]) in [1, 2, 3, 4, 5] and try_ag == "y":
                ship_placement
            if not position[0].lower() in ["a", "b", "c", "d", "e"] and int(position[1]) in [1, 2, 3, 4, 5] and try_ag == "n":
                exit()
        except: 
            print("good work")
        break


def print_board():
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


init_board()
print_board()
ship_placement(board)
print_board()


