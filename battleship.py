import random
import os
import time

board = []


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_input(): # easy get_input
    coordinates = input("Please enter a column and row: ")
    return coordinates

def init_board():
    board = []
    for i in range(5):
        board.append(["o"] * 5)
    return board 

def switch_player(current_player): # switching player 1 to player 2
    if current_player == 1:
        current_player = 2
    else:
        current_player = 1
    return current_player


def choosing_scene():
    ship = 1
    shoot_board1 = init_board()
    shoot_board2 = init_board()
    previous_move = []
    is_it_shooting_phase = True
    board_player_1 = init_board() # board of each player
    board_player_2 = init_board()
    mark = "" # need mark your choices , literraly saving your choices 
    current_player = 1 # variables to be able to switch players (player1 or player2 ) NOT FINISHED UNDER DEVELOPMENT
    app_only_run_once = True # with this variable i am able to PRINT Board  , OR Stop the screen/print board and with this i am making sure the program runs only Once
    while app_only_run_once: # i made a while loop using my variables if TRUE the program STARTS , if FALSE It not starts anymore
        mark = "X"  
        if current_player == 1: # you can decide if player1 start his choosing or player2 
            print_board(board_player_1)
            board = board_player_1
        else:
            print_board(board_player_2)
            board = board_player_2
        coordinates = get_input() # getting the coordinates
        os.system('cls||clear')
        if not valid_input(coordinates):  # sorting out if you have typed a valid input or not
            continue
        translated_coordinates = converter(coordinates)
        if ship == 2:
            if place_is_available_next_part(board, previous_move, translated_coordinates):
             continue
        if ship == 3:
            if not place_is_available_next_part(board, previous_move, translated_coordinates):
                print("Vertical or horizontal only!")
                continue 
        mark_player_coordinates(board,translated_coordinates, mark)
        previous_move = translated_coordinates
        ship +=1

        if sum(x.count('X') for x in board) == 3:    # adding your choices to the BOARD with using the converter
            print_board(board)
            if current_player == 2:      # its making sure that the next player come after the player 1 chosed his X-s
                app_only_run_once = False
            current_player = switch_player(current_player)
            os.system("""bash -c 'read -s -n 1 -p "Press any key to continue..."'""")
            os.system('cls||clear')
            print("Current player for shooting round is player: ", current_player)

    while is_it_shooting_phase:
        if current_player == 1:
            print_board(shoot_board1)
            board = shoot_board1
        else:
            print_board(shoot_board2)
            board = shoot_board2
        coordinates = get_input()
        if not valid_input(coordinates):
            continue
        translated_cooridinates = converter(coordinates)
        if current_player == 1:
            board = board_player_2
        else:
            board = board_player_1
        
        if not place_is_okay(board, translated_cooridinates):
            mark = "M"
            if current_player == 1:
                board = shoot_board1
            else:
                board = shoot_board2
            mark_player_coordinates(board, translated_cooridinates, mark)
            win_check(current_player, board) 
        
        else:
            mark = "S"
            if current_player == 1:
                board = shoot_board1
            else:
                board = shoot_board2
                print("current player", current_player)
            mark_player_coordinates(board, translated_cooridinates, mark)
            print("current player", current_player)
            current_player = switch_player(current_player)
            print("current player", current_player)


def marking_your_shoots(coordinates, board):
    if board[coordinates[0]][coordinates[1]] == 'X':
        board[coordinates[0]][coordinates[1]] = 'S'
    if board[coordinates[0]][coordinates[1]] != 'X':
        board[coordinates[0]][coordinates[1]] = 'M'      
    return board


def checking_if_you_win(current_player, board):
    if sum(x.count('H') for x in board) == 3:
        print("Congrats player", current_player, "has won the game")
        exit()



def win_check(current_player, board):
    if sum(x.count('H') for x in board) == 3:
        print("Congratulations player", current_player, "has won the game")
        exit()



def place_is_okay(board, coordinates):
    if board[coordinates[0]][coordinates[1]] == '0':
        return True
    else:
        return False


def converter(coordinates):
    coordinates_list = list(coordinates)
    try:
        if coordinates_list[0] == 'A' or coordinates_list[0] == 'a':
            coordinates_list[0] = 0
        if coordinates_list[0] == 'B' or coordinates_list[0] == 'b':
            coordinates_list[0] = 1
        if coordinates_list[0] == 'C' or coordinates_list[0] == 'c':
            coordinates_list[0] = 2
        if coordinates_list[0] == 'D' or coordinates_list[0] == 'd':
            coordinates_list[0] = 3
        if coordinates_list[0] == 'E' or coordinates_list[0] == 'e':
            coordinates_list[0] = 4
        
        coordinates_list[1] = int(coordinates_list[1]) - 1
        
    except:
        print('ERROR: Invalid input')
    return coordinates_list


def valid_input(coordinates):  # cheking if the input is valid or not
    coordinates_list = list(coordinates)
    if len(coordinates_list) !=2: # if the coordinates less than 2 charachters the program gave you invalid input
        print("That's not gonna working, please use valid input")
        return False
    possible_coordinates = ['a', 'b', 'c', 'd', 'e', 'A', 'B', 'C', 'D', 'E', '1', '2', '3', '4', '5'] # your possibly choices
    if coordinates_list[0] not in possible_coordinates or coordinates_list[1] not in possible_coordinates:
        print("Invalid Input try agian")
        return False
    return True

def print_board(board):
    print(" ", " ".join("12345"))
    for letter, row in zip('ABCDE', board):
        print(letter, " ".join(row))


def mark_player_coordinates(board, coordinates, mark):  # marking your choices on the board
    board[coordinates[0]][coordinates[1]] = mark
    return board

def place_is_available_next_part(board, previous_move, coordinates):
    if board[coordinates[0]] == board[previous_move[0]]:
        if coordinates[1] == previous_move[1] - 1 or coordinates[1] == previous_move[1] + 1:
            print("Invalid position, you musn't pick side by side !")
            return True
    if board[coordinates[1]] == board[previous_move[1]]:
        if coordinates[0] == previous_move[0] - 1 or coordinates[0] == previous_move[0] + 1:
            print("Invalid position, you musn't pick side by side !")
            return True


if __name__ == "__main__":
    choosing_scene()

