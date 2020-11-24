import random
import os

board = []
rows = ["a","A","b","B","c","C","e","E"]
columns = ["1","2","3","4","5"]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board():
    for i in range(5):
        board.append(["o"] * 5)


def ship_placement(board):
    ship_row = input("Enter the ship's position (row): ")
    ship_col = input("Enter the ship's position (col): ")
    ship_position = [ship_row, ship_col]
    for i in board:
        if i == ship_position[0]:
            for e in i:
                if e == ship_position[1]:
                    e = "x"


def print_board():
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


print_board()
ship_placement(board)
print_board()


'''while True:
    row = input("Provide a row: ")
    if row not in rows:
        print("That's not quite right , please use valid inputs")
        continue
    col = input("Provide a column: ")
    if col not in columns:
        print("That's not quite right, please use valid inputs")
        continue
   
    break'''