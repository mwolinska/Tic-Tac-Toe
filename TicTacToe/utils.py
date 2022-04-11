from typing import List, Tuple

import numpy as np

from dataclasses import dataclass


def list_available_positions(board: np.ndarray) -> List[bool]:
    avail_positions = []
    current_board = board.flatten()
    for el in current_board:
        if el == 0:
            avail_positions.append(True)
        else:
            avail_positions.append(False)
    return avail_positions

def is_position_available(board: np.ndarray, row: int, column: int) -> bool:
    available_positions = list_available_positions(board)
    position_index = row * 3 + column
    if row > 2 or column > 2:
        print("Position doesn't exist, pick another one")
        return False

    if not available_positions[position_index]:
        print("Position is not available, try another one")
    return available_positions[position_index]


def find_index_of_closest_value(click: int, allowed_positions_list: List[int]) -> int:
    allowed_positions_array = np.asarray(allowed_positions_list)
    closest_position_index = (np.abs(allowed_positions_array - click)).argmin()
    return closest_position_index

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