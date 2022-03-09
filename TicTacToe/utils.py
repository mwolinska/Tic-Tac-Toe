from typing import List

import numpy as np


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