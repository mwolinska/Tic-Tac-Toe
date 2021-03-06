from typing import Optional

from TicTacToe.data_model.move import Color, Move
from TicTacToe.interface.board import GameBoard
from TicTacToe.players.player import AbstractPlayer


class Player(AbstractPlayer):
    def __init__(self, player_number: int, color: Color):
        super().__init__()
        self.player_number = player_number
        self.color = color

    def make_move(self, board: GameBoard) -> Optional[Move]:
        user_interaction = board.game_visual.get_user_interaction()
        if user_interaction is None:
            return None
        else:
            move_address = board.game_visual.translate_user_click_to_coords(user_interaction)
        return Move(position=move_address, player_number=self.player_number)
