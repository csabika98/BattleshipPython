import random
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_board():
    board = []
    for i in range(0,5):
        board.append(["O"] * 5)
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


def first_input():
    board = []
    for i in range(0,5):
        c_board = board.append(["O"] * 5)
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))
    temp_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    while True:
        position = input("type a row and column:")
        row_for_retry = position
        try:
            if position[0].lower() in ["a", "b", "c", "d", "e"] and int(position[1]) in [1, 2, 3, 4, 5]:
                row = temp_dict.get(position[0].lower())
                col = int(position[1]) - 1
            if c_board[row][col] == "X":
                c_board[row][col] = "X"
            else:
                print("That position isn't empty!")
        except Exception:
            print("bamm")  
            break
            if position not in temp_dict:
                print("That's not quite right , please use valid inputs")
                try_ag = input("Do you wanna try again? y/n : ")
            if position not in temp_dict and try_ag == "y":
                print("The game now restarting!")
                row_for_retry  
            if position not in temp_dict and try_ag == "n":
                exit()

first_input()

def second_input():
    columns = ["1","2","3","4","5"]
    while True:
        col = input("Provide a column: ")
        if col not in columns:
            print("That's not quite right, please use valid inputs")
        
