from typing import Optional

import numpy as np
import pygame

from TicTacToe.data_model.move import Position, Color, Click, Move
from TicTacToe.utils.utils import find_index_of_closest_value


class GameWindow(object):
    def __init__(self, width: int = 600,
                 height: int = 600,
                 n_columns: int = 3,
                 n_rows: int = 3,
                 ):

        pygame.init()

        self.width = width
        self.height = height
        self.n_columns = n_columns
        self.n_rows = n_rows
        self.symbol_size = None
        self.vertical_line_position_list = []
        self.horizontal_line_position_list = []

        self.screen = pygame.display.set_mode([self.width, self.height])

        self.prepare_board()

    @classmethod
    def from_existing_board(cls, current_board: np.ndarray):
        visual = cls()
        for row_number in range(current_board.shape[0]):
            for column_number in range(current_board[row_number].shape[0]):
                if current_board[row_number][column_number] != 0:
                    if current_board[row_number][column_number] == 1:
                        stone_color = pygame.Color(132, 165, 157)
                    else:
                        stone_color = Color(242, 132, 130)
                    test_position = Move(Position(row_number, column_number), stone_color)
                    visual.draw_symbol(test_position, stone_color)

    def prepare_board(self):
        self.screen.fill((234, 228, 233))
        horizontal_margin = 0.05 * self.width
        vertical_margin = 0.05 * self.height
        board_width = self.width - 2 * horizontal_margin
        board_height = self.height - 2 * vertical_margin

        column_width = board_width / self.n_columns
        row_width = board_height / self.n_rows

        self.symbol_size = 0.25 * board_width / min(self.n_rows, self.n_columns)

        # draw vertical lines. This corresponds to x values
        for i in range(self.n_columns):

            start_pos = (horizontal_margin + i * column_width, vertical_margin)
            end_pos = (horizontal_margin + i * column_width, self.height - vertical_margin)
            if i != 0:
                pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos)
            self.vertical_line_position_list.append(start_pos[0] + column_width / 2)

        for i in range(self.n_rows):
            start_pos = (horizontal_margin, vertical_margin + i * row_width)
            end_pos = (self.width - horizontal_margin, vertical_margin + i * row_width)
            if i != 0:
                pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos)
            self.horizontal_line_position_list.append(start_pos[1] + row_width / 2)

        pygame.display.flip()

    def print_starting_player(self, player_number):
        running = True
        while running:
            welcome_string = "Player " + str(player_number) + " will start the game"
            my_font = pygame.font.SysFont("menlo", 30)
            text_img = my_font.render(welcome_string, True, (0, 0, 0))
            rect_placement_adjust = 0.1 * self.height
            pygame.draw.rect(self.screen,
                             (245, 202, 195),
                             (0, self.height / 2 - rect_placement_adjust, self.width, rect_placement_adjust * 2),
                             0)
            self.screen.blit(text_img,
                             ((self.width - text_img.get_size()[0]) / 2, (self.height - text_img.get_size()[1]) / 2))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False
                    self.prepare_board()

    @staticmethod
    def get_user_interaction() -> Optional[Click]:
        running = True
        while running:

            for event in pygame.event.get():
                if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (event.key == pygame.K_ESCAPE)):
                    running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return Click(event.pos[0], event.pos[1])

        pygame.quit()
        return None

    def translate_user_click_to_coords(self, user_click: Click) -> Position:
        column = find_index_of_closest_value(user_click.x, self.vertical_line_position_list)
        row = find_index_of_closest_value(user_click.y, self.horizontal_line_position_list)
        move_address = Position(row, column)
        return move_address

    def draw_symbol(self, move_location: Move, color: Color):
        # there is a difference between the row and column within the GameBoard and GameVisualisation.
        # The Position row and column reflect the logic of a numpy array.
        # row corresponds to the y coordinates of the Game Visualisation
        # column corresponds to the x coordinates of the game visualisation

        if move_location.player_number == 1:
            self.draw_cross(self.vertical_line_position_list[move_location.position.column], self.vertical_line_position_list[move_location.position.row])
        elif move_location.player_number == 2:
            pygame.draw.circle(self.screen,
                               color.rgb,
                               (self.vertical_line_position_list[move_location.position.column], self.vertical_line_position_list[move_location.position.row]),
                               self.symbol_size,
                               5)
        pygame.display.flip()

    def draw_cross(self, x, y):
        cross_radius = self.symbol_size * 0.8

        pygame.draw.line(self.screen,
                         (132, 165, 157),
                         (x - cross_radius, y - cross_radius), (x + cross_radius, y + cross_radius),
                         5)
        pygame.draw.line(self.screen,
                         (132, 165, 157),
                         (x - cross_radius, y + cross_radius), (x + cross_radius, y - cross_radius),
                         5)

    def game_outcome(self, outcome_string: str):
        running = True
        while running:
            my_font = pygame.font.SysFont("menlo", 30)
            text_img = my_font.render(outcome_string, True, (0, 0, 0))
            rect_placement_adjust = 0.1 * self.height
            pygame.draw.rect(self.screen,
                             (245, 202, 195),
                             (0, self.height / 2 - rect_placement_adjust, self.width, rect_placement_adjust * 2),
                             0)
            self.screen.blit(text_img, ((self.width - text_img.get_size()[0])/2,  (self.height - text_img.get_size()[1])/2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    running = False

    def connect_winning_points(self):
        pass

    def play_again(self):
        running = True
        while running:
            check_string = "Do you want to play again? Press y or n"
            my_font = pygame.font.SysFont("menlo", 24)
            text_img = my_font.render(check_string, True, (0, 0, 0))
            rect_placement_adjust = 0.1 * self.height
            pygame.draw.rect(self.screen,
                             (245, 202, 195),
                             (0, self.height / 2 - rect_placement_adjust, self.width, rect_placement_adjust * 2),
                             0)
            self.screen.blit(text_img,
                             ((self.width - text_img.get_size()[0]) / 2, (self.height - text_img.get_size()[1]) / 2))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        return True
                    elif event.key == pygame.K_n:
                        pygame.quit()
                        return False
