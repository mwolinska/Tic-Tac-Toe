import random
import time
from itertools import permutations
from typing import List, Tuple

import numpy as np

from TicTacToe.game_interface import GameWindow
from TicTacToe.player import Player


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

    def select_random_position(self):

        available_position_selected = False
        available_positions_list = self.list_available_positions()

        while not available_position_selected:
            random_position = random.randint(0, 8)

            if available_positions_list[random_position]:
                row = random_position // 3
                column = random_position % 3
                return row, column
            else:
                available_position_selected = False

    def select_best_position(self):
        current_game_board = self.board.copy()
        game_outcome_simulation = BoardSimulation(current_game_board)
        win_probability_matrix = game_outcome_simulation.simulate_possible_games()
        flat_win_probability_matrix = win_probability_matrix.flatten()
        possible_move_indexes = np.where(flat_win_probability_matrix == max(flat_win_probability_matrix))
        random.shuffle(possible_move_indexes)
        row = possible_move_indexes[0][0] // 3
        column = possible_move_indexes[0][0] % 3
        return row, column

    def play_move(self, game_interface: GameWindow, player: Player):
        is_move_possible = False
        row, column = None, None

        if not player.is_random:
            while not is_move_possible:
                x_click, y_click = game_interface.get_user_interaction()
                row, column = game_interface.get_move_location(x_click, y_click)

                is_move_possible = self.is_position_available(row, column)
        else:
            row, column = self.select_best_position()
            print(row, column)

        game_interface.get_symbol_coordinates(row, column)
        game_interface.draw_symbol(player.player_number)
        self.board[row][column] = player.player_number



if __name__ == '__main__':
    a = np.array(
         [[1, 2, 1],
         [2, 2, 1],
         [0, 1, 0],])

    tic = time.perf_counter()
    game_sim = BoardSimulation(a)
    test = game_sim.simulate_possible_games()
    toc = time.perf_counter()
    print(test)
    print(toc - tic)
