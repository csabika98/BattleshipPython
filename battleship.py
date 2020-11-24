import random
import os
import time

board = []
rows = ["a","A","b","B","c","C","e","E"]
columns = ["1","2","3","4","5"]


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def init_board():
    for i in range(5):
        board.append(["o"] * 5)


def ship_placement(board):
    temp_dict = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    while True:
        position = input("Provide a position:")
        if position == "quit":
            print("Goodbye!")
            exit()
        try:
            if position[0].lower() in ["a", "b", "c", "d", "e"] and int(position[1]) in [1, 2, 3, 4, 5]:
                row = temp_dict.get(position[0].lower())
                col = int(position[1]) - 1
                if board[row][col] == "o":
                    board[row][col] = "x"
                else:
                    print("That position isn't empty!")
        except Exception:
            print("bamm meghaltal")
        if position[0].lower() not in ["a", "b", "c", "d", "e"] or int(position[1]) not in [1, 2, 3, 4, 5]:
            print("Not a valid position!")
        else:
            break
    return position


def ship_positions():
    positions = []
    player1 = ship_placement(board)
    print_board()
    time.sleep(1)
    print_board()
    player2 = ship_placement(board)
    list(player1)
    list(player2)
    positions.append(player1)
    positions.append(player2)
    print(positions)


def print_board():
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


init_board()
print_board()
ship_positions()
print_board()
