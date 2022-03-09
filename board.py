from typing import List

import numpy as np

from game_interface import GameWindow
from player import Player


class GameBoard(object):
    def __init__(self, number_of_rows: int = 3, number_of_columns: int =3):
        self.board = np.zeros((number_of_rows, number_of_columns))

    def list_available_positions(self) -> List[bool]:
        avail_positions = []
        current_board = self.board.flatten()
        for el in current_board:
            if el == 0:
                avail_positions.append(True)
            else:
                avail_positions.append(False)
        return avail_positions

    def is_position_available(self, row: int, column: int) -> bool:
        available_positions = self.list_available_positions()
        position_index = row * 3 + column
        if row > 2 or column > 2:
            print("Position doesn't exist, pick another one")
            return False

        if not available_positions[position_index]:
            print("Position is not available, try another one")
        return available_positions[position_index]

    def play_move(self, game_interface: GameWindow, player: Player):
        is_move_possible = False
        row, column = None, None
        while not is_move_possible:
            x_click, y_click = game_interface.get_user_interaction()
            row, column = game_interface.get_move_location(x_click, y_click)
            is_move_possible = self.is_position_available(row, column)

        game_interface.draw_symbol(player.player_number)
        self.board[row][column] = player.player_number

