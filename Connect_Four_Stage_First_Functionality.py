# Dominic Whelan

import numpy as np
import pygame
import sys


ROW_COUNT = 6
COLUMN_COUNT = 7

def create_board():
    board = np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_peice(board, row, col, peice):
    board[row][col] = peice

def is_valid_location(board, col):
    return board[ROW_COUNT-1][col] == 0

def get_next_open_row(board, col):
    for r in range(ROW_COUNT):
        if board[r][col] == 0:
            return r

def print_board(board):
    print(np.flip(board, 0))

def winning_move(board, peice):
    # check horizontal locations for win
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT):
            if board[r][c] == peice and board[r][c+1] == peice and board[r][c+2] ==peice and board[r][c+3] == peice:
                return True
    # Check for vertical locations for the win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT-3):
            if board[r][c] == peice and board[r+1][c] == peice and board[r+2][c] ==peice and board[r+3][c] == peice:
                return True
    # Check for positive sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(ROW_COUNT-3):
            if board[r][c] == peice and board[r+1][c+1] == peice and board[r+2][c+2] ==peice and board[r+3][c+3] == peice:
                return True

    # Check for negative sloped diagonals
    for c in range(COLUMN_COUNT-3):
        for r in range(3, ROW_COUNT):
            if board[r][c] == peice and board[r-1][c+1] == peice and board[r-2][c+2] ==peice and board[r-3][c+3] == peice:
                return True

def draww_board
    pass

board = create_board()
print_board(board)
game_over = False
turn = 0

pygame.init()

SQUARE_SIZE = 100

width = COLUMN_COUNT * SQUARE_SIZE
height = (ROW_COUNT + 1) * SQUARE_SIZE

size = (width, height)

screen = pygame.display.set_mode(size)

while not game_over:
    # Ask for Player 1 input
    if turn == 0:
        col = int(input("Player 1 make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_peice(board, row, col, 1)
            if winning_move(board, 1):
                print("PLAYER 1 wins!!! Congrats")
                game_over = True
                break
        print_board(board)

    # Ask for Player 2 input
    else:
        col = int(input("Player 2 make your selection (0-6): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_peice(board, row, col, 2)
            if winning_move(board, 2):
                print("PLAYER 2 wins!!! Congrats")
                game_over = True
                break
        print_board(board)

    turn += 1
    turn = turn % 2
