from typing import List, Tuple
import numpy as np

from utils import is_position_available

def change_player(player_number):
    if player_number == 1:
        new_player_number = 2
    elif player_number == 2:
        new_player_number = 1
    else:
        new_player_number = None
    return new_player_number

def play_move(game_interface, board: np.ndarray, player_number):
    is_move_possible = False
    row, column = None, None
    while not is_move_possible:
        x_click, y_click = game_interface.get_user_interaction()
        row, column = game_interface.get_move_location(x_click, y_click)
        is_move_possible = is_position_available(board, row, column)

    game_interface.draw_symbol(player_number)
    board[row][column] = player_number
    return board
