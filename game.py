import random
import os
import time


def welcome():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("        _         __                                ")
    print("     _               __                             ")
    print("        ..-^~~~^-..                                 ")
    print("      .~           ~.                               ")
    print("     (;:           :;)                              ")
    print("      (:           :)                               ")
    print("        ':._   _.:'                                 ")
    print("            | |                                     ")
    print("          (=====)                                   ")
    print("            | |                                     ")
    print("            | |                                     ")
    print("            | |                                     ")
    print(" _____ _ (((   )))  _____                           ")
    print("|     |_|___ ___   |   __|_ _ _ ___ ___ ___ ___ ___ ")
    print("| | | | |   | -_|  |__   | | | | -_| -_| . | -_|  _|")
    print("|_|_|_|_|_|_|___|  |_____|_____|___|___|  _|___|_|  ")
    print("                                       |_|          ")
    print(f"\t\tHi, {name}!!! Welcome to the jungle...")

os.system('cls' if os.name == 'nt' else 'clear')
name = input(f"\n\n\t\tWhat´s your name: \n\t\t\t:>").title()
num_col = int(input(f"\t\tWhat will be the number of columns?\b\t\t: "))
num_row = int(input(f"\t\tWhat will be the number of lines?\b\t\t: "))
num_mine = int(input(f"\t\tHow many mines will there be?\b\t\t\t: "))

def create_board(rows, cols, mines):
    board = [["  " for _ in range(cols)] for _ in range(rows)]
    for _ in range(mines):
        row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        while board[row][col] == 'o*':  # To avoid placing mine on already mined cell
            row, col = random.randint(0, rows - 1), random.randint(0, cols - 1)
        board[row][col] = 'o*'
    return board


def count_adjacent_mines(row, col, board):
    count = 0
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + 2):
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'o*':
                count += + 1
    return '{:02d}'.format(count)

def col_numbers():
    num_of_col = [" ",]
    for i in range(0, num_col):
        if i <= 9:
            i = f" {i}"
            num_of_col.append(i)
        else:
            num_of_col.append(i)

    for num in num_of_col:
        print(num, end=" ")


def display_board(board):
    col_numbers()
    print()
    row_num = 0
    for row in board:
        print(f"{row_num} {('|'.join(str(cell) for cell in row))} {row_num}")
        row_num += 1
    col_numbers()
    print()


def main():
    welcome()
    time.sleep(5)
    rows, cols, mines = num_row, num_col, num_mine
    board = create_board(rows, cols, mines)
    revealed = [['__' for _ in range(cols)] for _ in range(rows)]

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        display_board(revealed)

        row = int(input('Enter row: '))
        col = int(input('Enter column: '))

        if board[row][col] == 'o*':
            print('Game Over! You hit a mine.')
            os.system('cls' if os.name == 'nt' else 'clear')
            break

        revealed[row][col] = count_adjacent_mines(row, col, board)
        os.system('cls' if os.name == 'nt' else 'clear')
        print("LOOSER MESSAGE...")

    display_board(board)
    print(f"\t\tGame over! Here is the complete board:")
    print(" _____ _            _____                           ")
    print("|     |_|___ ___   |   __|_ _ _ ___ ___ ___ ___ ___ ")
    print("| | | | |   | -_|  |__   | | | | -_| -_| . | -_|  _|")
    print("|_|_|_|_|_|_|___|  |_____|_____|___|___|  _|___|_|  ")
    print("                                       |_|          ")
    print(f"\t\t{name}, you die!!!")

main()