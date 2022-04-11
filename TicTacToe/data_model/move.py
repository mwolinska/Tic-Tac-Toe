from dataclasses import dataclass
from typing import Tuple


@dataclass
class Click(object):
    x: int
    y: int

@dataclass
class Position(object):
    row: int
    column: int

    @classmethod
    def from_tuple(cls, position):
        return cls(position[0], position[1])

    @classmethod
    def from_index(cls, index, n_columns:int):
        return cls((index // n_columns), (index % n_columns))

@dataclass
class PositionIndex(object):
    position_index: int

    @classmethod
    def from_position(cls, position: Position, n_columns: int):
        return position.row * n_columns + position.column

@dataclass
class Move(object):
    position: Position
    player_number: int

@dataclass
class Color(object):
    r: int
    g: int
    b: int

    @property
    def rgb(self) -> Tuple[int, int, int]:
        return self.r, self.g, self.b
