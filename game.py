from random import randint

import numpy as np
from typing import Tuple, List

from game_interface import GameWindow
from player import play_move, change_player
from utils import list_available_positions


def create_game() -> Tuple[List[List], int]:
    clean_board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # randomly select whether cross or naught will start
    # 1 is cross, 2 is naught
    starting_number = randint(1, 2)
    return clean_board, starting_number

def has_player_won(board: np.ndarray, player_number: int) -> bool:
    is_win_mask = board == player_number

    for i in range(3):
        # is there a win in each row?
        if np.all(is_win_mask[:, i]):
            print("Player " + str(player_number) + " has won the game")
            return True
        # is there a win in each column?
        elif np.all(is_win_mask[i, :]):
            print("Player " + str(player_number) + " has won the game")
            return True
    # Check if there is a win across the diagonals
    if is_win_mask[0][0] == is_win_mask[1][1] == is_win_mask[2][2] == True:
        return True
    elif is_win_mask[2][0] == is_win_mask[1][1] == is_win_mask[0][2] == True:
        return True

    return False

def is_game_draw(board):
    if sum(list_available_positions(board)) == 0:
        print("The game is over, this is a draw")
        return True
    else:
        return False


def is_game_over(board, player_number) -> Tuple[bool, str]:
    outcome_string = None

    if has_player_won(board, player_number):
        outcome_string = "Player " + str(player_number) + " won the game"
        return True, outcome_string
    else:
        if is_game_draw(board):
            outcome_string = "This game is a draw"
            return True, outcome_string
        else:
            outcome_string = "The game continues"
            return False, outcome_string

def play_game():
    game_board, player = create_game()
    game_visual = GameWindow()
    game_visual.prepare_board()

    is_over = False
    outcome = None
    while not is_over:

        game_board = play_move(game_visual, game_board, player)
        is_over, outcome = is_game_over(game_board, player)

        player = change_player(player)
        print(game_board)
        print(outcome)

    game_visual.game_outcome(outcome)


