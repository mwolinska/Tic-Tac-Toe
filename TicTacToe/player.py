import abc
import dataclasses
from dataclasses import dataclass
from typing import List

from TicTacToe.board import GameBoard
from TicTacToe.utils import Position, Move


@dataclass
class PotentialMove:
    position: Position
    score: float

@dataclass
class PotentialMoves:
    potential_moves: List[PotentialMove] = dataclasses.field(default_factory=list)

    @property
    def best_potential_move(self) -> PotentialMove:
        try:
            best_move_score = self.potential_moves[0].score
            best_move = self.potential_moves[0]

            for potential_move in self.potential_moves:
                if potential_move.score > best_move_score:
                    best_move_score = potential_move.score
                    best_move = potential_move

            return best_move
        except IndexError:
            raise IndexError("Check your list before you wreck your list")


class AbstractPlayer(abc.ABC):
    def __init__(self):
        self.player_number = None
        self.color = None
    @abc.abstractmethod
    def make_move(self, board: GameBoard) -> Move:
        pass





