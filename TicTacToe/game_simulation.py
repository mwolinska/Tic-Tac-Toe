import copy
import logging
from typing import Optional

import numpy as np

from TicTacToe.board import GameBoard
from TicTacToe.game import AbstractGame, GameStatus
from TicTacToe.utils import Move, Position


class GameSim(AbstractGame):

    def __init__(self, player_list):
        super().__init__()
        self.player_list = player_list
        self.game_board = GameBoard()
        self.player_index = 0
        self.first_position = None

    @classmethod
    def from_existing_board(cls, current_game_state_board: np.ndarray, player_list) -> "GameSim":
        game = cls(player_list)
        game.game_board = game.game_board.from_array(current_game_state_board)
        return game

    def get_copy(self):
        return copy.deepcopy(self)

    def play_game(self):
        status = GameStatus.ongoing
        n_moves_till_end = 0

        while status == GameStatus.ongoing:
            player = self.player_list[self.player_index % len(self.player_list)]

            if n_moves_till_end == 0 and self.first_position is not None:
                player_move = Move(self.first_position, player.player_number)
            else:
                player_move = player.make_move(self.game_board)

            self.game_board.update_board(player_move)
            status = self.get_game_status(player_move)
            self.player_index += 1
            n_moves_till_end += 1

        return status, n_moves_till_end

    def get_game_status(self, last_move: Move) -> GameStatus:
        if self.has_player_won(last_move) and last_move.player_number == 2:
            outcome = GameStatus.win
        elif self.has_player_won(last_move) and last_move.player_number != 2:
            outcome = GameStatus.loss
        elif sum(self.game_board.available_positions_list) == 0:
            outcome = GameStatus.draw
        else:
            outcome = GameStatus.ongoing
        return outcome

    def run_single_simulation(self) -> float:
        game_copy = self.get_copy()
        outcome, n_moves_till_end = game_copy.play_game()
        outcome_score = self.outcome_to_int(outcome) / n_moves_till_end
        return outcome_score

    def simulate(self, number_of_simulations: int, first_position: Optional[Position]) -> float:
        game_score_tally = 0
        self.first_position = first_position
        for i in range(number_of_simulations):
            outcome_score = self.run_single_simulation()
            game_score_tally += outcome_score

        logging.info("The score is " + str(game_score_tally / number_of_simulations))
        return game_score_tally / number_of_simulations

    @staticmethod
    def outcome_to_int(outcome):
        if outcome == GameStatus.win:
            outcome_int = 1
        elif outcome == GameStatus.draw:
            outcome_int = 0
        elif outcome == GameStatus.loss:
            outcome_int = -1
        else:
            outcome_int = None

        return outcome_int
