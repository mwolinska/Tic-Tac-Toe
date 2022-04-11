import abc

from enum import Enum
from typing import List

import numpy as np

from TicTacToe.utils import Move
from TicTacToe.player import AbstractPlayer


class GameStatus(str, Enum):
    win = "win"
    loss = "loss"
    draw = "draw"
    ongoing = "ongoing"


class AbstractGame(abc.ABC):

    @classmethod
    @abc.abstractmethod
    def from_existing_board(cls, current_game_board: np.ndarray, player_list: List[AbstractPlayer]) -> "AbstractGame":
        pass

    @abc.abstractmethod
    def play_game(self):
        pass

    @abc.abstractmethod
    def get_game_status(self, move: Move) -> GameStatus:
        pass

    def has_player_won(self, move: Move):
        pass
