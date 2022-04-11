from itertools import permutations
from typing import List, Tuple

import numpy as np


class BoardSimulation(object):
    def __init__(self, board: np.ndarray, player_number: int = 2, opponent_player_number: int = 1):
        self.starting_board = board
        self.board = board
        self.player_number = player_number
        self.opponent_player_number = opponent_player_number

    def simulate_possible_games(self):
        all_available_moves = self.list_available_position_tuples()
        if len(all_available_moves) == 9:
            win_probability_array = np.array([[0.8, 0.72857143, 0.8],
                                              [0.72857143, 0.88571429, 0.72857143],
                                              [0.8, 0.72857143, 0.8]])
            return win_probability_array
        starting_board = self.board.copy()
        win_probability_array = np.full((3, 3), -1, dtype=float)

        for first_move in all_available_moves:
            score_for_move = 0
            row = first_move[0]
            column = first_move[1]
            self.board[row][column] = self.player_number

            interim_board = self.board.copy()

            all_sequences = self.get_all_move_permutations()

            for game_sequence in all_sequences:
                number_moves_till_outcome = self.get_game_end_board(game_sequence)
                if number_moves_till_outcome != 0:
                    score_for_move += (self.get_game_outcome_score() / number_moves_till_outcome)
                else:
                    score_for_move += self.get_game_outcome_score()
                self.board = interim_board.copy()

            else:
                win_probability_array[row][column] = score_for_move / len(all_sequences)
            self.board = starting_board.copy()

        print(win_probability_array)
        return win_probability_array

    def get_all_move_permutations(self):
        all_available_positions = self.list_available_position_tuples()
        all_game_sequences = list(permutations(all_available_positions, len(all_available_positions)))
        return all_game_sequences

    def get_game_end_board(self, move_sequence):
        current_player = self.opponent_player_number
        n_moves_till_end = 0

        for i in range(len(move_sequence)):
            row = move_sequence[i][0]
            column = move_sequence[i][1]
            self.board[row][column] = current_player
            n_moves_till_end = i + 1

            if self.is_simulation_win(current_player):
                return n_moves_till_end

            current_player = self.change_player(current_player)

        return n_moves_till_end

    def get_game_outcome_score(self):
        if self.is_simulation_win(self.player_number):
            return 1
        elif self.is_simulation_win(self.opponent_player_number):
            return -1
        elif self.is_game_draw():
            return 0
        else:
            return None

    def change_player(self, player):
        if player == self.player_number:
            player = self.opponent_player_number
        elif player == self.opponent_player_number:
            player = self.player_number
        return player

    def number_of_moves_remaining(self):
        remaining_moves_mask = self.board == 0
        return sum(remaining_moves_mask)

    def list_available_position_tuples(self) -> List[Tuple[int, int]]:
        flat_board = self.board.flatten()
        avail_position_tuples = []
        for i in range(flat_board.size):
            if flat_board[i] == 0:
                row = i // 3
                column = i % 3
                avail_position_tuples.append((row, column))
        return avail_position_tuples

    def is_simulation_win(self, current_player):
        is_win_mask = self.board == current_player

        for i in range(3):
            # is there a win in each row?
            if np.all(is_win_mask[:, i]):
                return True
            # is there a win in each column?
            elif np.all(is_win_mask[i, :]):
                return True
        # Check if there is a win across the diagonals
        if is_win_mask[0][0] == is_win_mask[1][1] == is_win_mask[2][2] == True:
            return True
        elif is_win_mask[2][0] == is_win_mask[1][1] == is_win_mask[0][2] == True:
            return True

        return False

    def is_game_draw(self) -> bool:
        if self.number_of_moves_remaining().any():
            return False
        else:
            return True
