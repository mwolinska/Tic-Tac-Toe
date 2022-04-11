import logging
import random
from typing import Tuple, Optional, List

import numpy as np

from TicTacToe.board import GameBoard
from TicTacToe.player import AbstractPlayer
from TicTacToe.player_human import Player
from TicTacToe.player_smart import SmartPlayer
from TicTacToe.utils import Color, Move, Position


class TicTacToe(object):
    def __init__(self,
                 number_of_players: int = 2,
                 with_bots: bool = False,
                 generate_visual: bool = True,
                 player_list: Optional[List[AbstractPlayer]] = None,
                 ):
        self.number_of_players = number_of_players
        self.with_bots = with_bots
        self.game_board = GameBoard(generate_visual=generate_visual)

        if player_list is None:
            self.player_list = self.create_list_of_players()
        else:
            self.player_list = player_list

        self.player_index = 0

    @classmethod
    def from_existing_board(cls,
                            current_game_state_board: np.ndarray,
                            with_bots=False,
                            generate_visual=False,
                            player_list: Optional[List[AbstractPlayer]] = None,
                            ):
        game = cls(with_bots=with_bots, generate_visual=False, player_list=player_list)
        game.game_board = GameBoard.from_array(current_game_state_board, generate_visual=generate_visual)
        if generate_visual:
            game.game_board.game_visual.from_existing_board(current_game_state_board)
        return game

    def create_list_of_players(self) -> List[AbstractPlayer]:
        list_of_players = []
        list_of_colors = [Color(132, 165, 157), Color(242, 132, 130)]
        player_number_counter = 1
        range_for_list = self.number_of_players
        if self.with_bots:
            range_for_list = self.number_of_players // 2

        for i in range(range_for_list):
            list_of_players.append(Player(player_number_counter, list_of_colors[i]))
            player_number_counter += 1
            if self.with_bots:
                list_of_players.append(SmartPlayer(player_number_counter, list_of_colors[i + 1]))
                player_number_counter += 1

        random.shuffle(list_of_players)

        return list_of_players

    def has_player_won(self, last_move: Move) -> bool:

        is_win_mask = self.game_board.board == last_move.player_number

        for i in range(self.game_board.board.shape[0]):
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

    def is_game_over(self, last_move: Move) -> Tuple[bool, str]:

        if self.has_player_won(last_move):
            outcome_string = "Player " + str(last_move.player_number) + " won the game"
            return True, outcome_string
        else:
            if sum(self.game_board.available_positions_list) == 0:
                outcome_string = "This game is a draw"
                return True, outcome_string
            else:
                outcome_string = "The game continues"
                return False, outcome_string

    def get_next_player(self) -> AbstractPlayer:
        player = self.player_list[self.player_index % self.number_of_players]
        return player

    def play_game(self):

        is_over = False
        outcome = None
        play_again = True

        self.game_board.game_visual.print_starting_player(self.player_list[0].player_number)

        while not is_over:
            player = self.get_next_player()
            logging.debug(self.number_of_players)

            player_move = player.make_move(self.game_board)

            if player_move is None:
                is_over = True
                outcome = "Game ended early"
            elif self.game_board.is_position_available(player_move.position):
                self.game_board.game_visual.draw_symbol(player_move, color=player.color)
                self.game_board.update_board(player_move)
                logging.debug(self.game_board.board)
                logging.debug(self.game_board.available_positions_list)

                is_over, outcome = self.is_game_over(player_move)
                self.player_index += 1

            else:
                logging.info("Position is taken, try again")

        logging.info(outcome)
        self.game_board.game_visual.game_outcome(outcome)
        play_again = self.game_board.game_visual.play_again()

        return play_again

def single_player_game_main():
    logging.getLogger().setLevel(logging.INFO)
    play = True
    while play:
        play = TicTacToe(with_bots=True).play_game()

def two_player_game_main():
    logging.getLogger().setLevel(logging.INFO)
    play = True
    while play:
        play = TicTacToe().play_game()
