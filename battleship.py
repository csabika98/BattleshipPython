import random
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


rows = ["a","A","b","B","c","C","e","E"]
columns = ["1","2","3","4","5"]
def print_board():
    board = []
    for i in range(0,5):
        board.append(["O"] * 5)
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


print_board()

while True:
    row = input("Provide a row: ")
    if row not in rows:
        print("That's not quite right , please use valid inputs")
        continue
    col = input("Provide a column: ")
    if col not in columns:
        print("That's not quite right, please use valid inputs")
        continue
        
    break