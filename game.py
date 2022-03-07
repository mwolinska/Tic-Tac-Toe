from random import randint

import numpy as np
from typing import Tuple, List

from player import play_move, change_player

def create_game() -> Tuple[List[List], int]:
    clean_board = np.array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    # randomly select whether cross or naught will start
    # 1 is cross, 2 is naught
    starting_number = randint(1, 2)
    return clean_board, starting_number

def play_game():
    game_board, player = create_game()
    play_next_move = True
    while play_next_move:
        game_board, play_next_move = play_move(game_board, player)
        player = change_player(player)
        print(game_board)


