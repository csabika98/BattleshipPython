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
    rows = ["a","A","b","B","c","C","e","E"]
    while True:
        row = input("type a row:")
        if row not in rows:
            print("That's not quite right , please use valid inputs")
            retry = input("Do you wanna try again? y/n : ")
        elif retry == "y":
            first_input() 
        elif retry == "n":
            exit()
        break


def second_input():
    columns = ["1","2","3","4","5"]
    while True:
        col = input("Provide a column: ")
        if col not in columns:
            print("That's not quite right, please use valid inputs")
        

if __name__ == "__main__":
    print_board()
    first_input()
    second_input()