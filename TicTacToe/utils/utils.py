from typing import List

import numpy as np


def find_index_of_closest_value(click: int, allowed_positions_list: List[int]) -> int:
    allowed_positions_array = np.asarray(allowed_positions_list)
    closest_position_index = (np.abs(allowed_positions_array - click)).argmin()
    return closest_position_index
