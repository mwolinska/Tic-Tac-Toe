from random import randint

import numpy as np
from typing import Tuple

from board import GameBoard
from game_interface import GameWindow
from player import Player

class TicTacToe(object):
    def __init__(self, number_of_players: int = 2):
        self.number_of_players = number_of_players
        pass

    def change_player(self, current_player_index: int) -> int:
        next_player_index = current_player_index + 1

        if next_player_index == self.number_of_players:
            next_player_index = 0

        return next_player_index

    def create_list_of_players(self):
        list_of_players = []

        for i in range(self.number_of_players):
            list_of_players.append(Player(i+1))

        return list_of_players

    def has_player_won(self, board: GameBoard, player: Player) -> bool:
        is_win_mask = board.board == player.player_number

        for i in range(3):
            # is there a win in each row?
            if np.all(is_win_mask[:, i]):
                print("Player " + str(player.player_number) + " has won the game")
                return True
            # is there a win in each column?
            elif np.all(is_win_mask[i, :]):
                print("Player " + str(player.player_number) + " has won the game")
                return True
        # Check if there is a win across the diagonals
        if is_win_mask[0][0] == is_win_mask[1][1] == is_win_mask[2][2] == True:
            return True
        elif is_win_mask[2][0] == is_win_mask[1][1] == is_win_mask[0][2] == True:
            return True

        return False

    def is_game_draw(self, board: GameBoard) -> bool:
        if sum(board.list_available_positions()) == 0:
            print("The game is over, this is a draw")
            return True
        else:
            return False

    def is_game_over(self, board: GameBoard, player: Player) -> Tuple[bool, str]:

        if self.has_player_won(board, player):
            outcome_string = "Player " + str(player.player_number) + " won the game"
            return True, outcome_string
        else:
            if self.is_game_draw(board):
                outcome_string = "This game is a draw"
                return True, outcome_string
            else:
                outcome_string = "The game continues"
                return False, outcome_string

    def play_game(self):
        game_visual = GameWindow()
        player_list = self.create_list_of_players()
        continue_playing = True

        while continue_playing:
            board = GameBoard()
            starting_player_index = randint(0, len(player_list) - 1)
            game_visual.prepare_board()
            game_visual.print_starting_player(player_list[starting_player_index].player_number)

            is_over = False
            outcome = None

            player_making_move_index = starting_player_index
            player_making_move = player_list[player_making_move_index]

            while not is_over:
                board.play_move(game_visual, player_making_move)
                is_over, outcome = self.is_game_over(board, player_making_move)

                player_making_move_index = self.change_player(player_making_move_index)
                player_making_move = player_list[player_making_move_index]

            game_visual.game_outcome(outcome)
            continue_playing = game_visual.play_again()


if __name__ == '__main__':
    my_game = TicTacToe()
    my_game.play_game()
