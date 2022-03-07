from typing import List

import numpy as np


def continue_game(board, player_number) -> bool:

    for i in range(3):
        # is there a win in each row?
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != 0:
            return False
        # is there a win in each column?
        elif board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != 0:
            return False

    return True

def change_player(player_number):
    if player_number == 1:
        new_player_number = 2
    elif player_number == 2:
        new_player_number = 1
    else:
        new_player_number = None
    return new_player_number

def get_move():
    row = int(input("Play position row: "))
    column = int(input("Play position column: "))
    return row, column

def play_move(board: List[List], player_number):
    row, column = get_move()
    if is_position_available(board, row, column):
        board[row][column] = player_number
        continue_to_next_move = continue_game(board, player_number)
        return board, continue_to_next_move
    else:
        return play_move(board, player_number)

def list_available_positions(board: np.ndarray) -> List[bool]:
    avail_positions = []
    current_board = board.flatten()
    for el in current_board:
        if el == 0:
            avail_positions.append(True)
        else:
            avail_positions.append(False)
    return avail_positions

def is_position_available(board: np.ndarray, row: int, column: int) -> bool:
    available_positions = list_available_positions(board)
    position_index = row * 3 + column
    if row > 2 or column > 2:
        print("Position doesn't exist, pick another one")
        return False

    if not available_positions[position_index]:
        print("Position is not available, try another one")
    return available_positions[position_index]