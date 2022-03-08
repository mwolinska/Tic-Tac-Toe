from typing import Optional, Tuple

import pygame
from pygame import event


class GameWindow(object):
    def __init__(self, width: int = 600, height: int = 600):
        self.y_position_grid_centre = None
        pygame.init()

        self.width = width
        self.height = height

        self.screen = pygame.display.set_mode([self.width, self.height])

        self.symbol_size = None
        self.vertical_lines = None
        self.horizontal_lines = None
        self.x_position_grid_centre = None
        self.x_symbol_centre = None
        self.y_symbol_centre = None

    def prepare_board(self):
        self.screen.fill((234, 228, 233))
        width_adjust = 0.05 * self.width
        height_adjust = 0.05 * self.height

        self.symbol_size = 0.22 * self.width / 3
        self.vertical_lines = []
        self.horizontal_lines = []

        for i in range(1, 3):
            start_pos = (i * self.width / 3, height_adjust)
            end_pos = (i * self.width / 3, self.height - height_adjust)
            pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos)
            self.vertical_lines.append(start_pos[0])

        self.x_position_grid_centre = (self.vertical_lines[1] - self.vertical_lines[0]) / 2

        for i in range(1, 3):
            start_pos = (width_adjust, i * self.height / 3)
            end_pos = (self.width - width_adjust, i * self.height / 3)
            pygame.draw.line(self.screen, (0, 0, 0), start_pos, end_pos)
            self.horizontal_lines.append(start_pos[1])

        self.y_position_grid_centre = (self.horizontal_lines[1] - self.horizontal_lines[0]) / 2
        pygame.display.flip()

    def print_starting_player(self, player_number):
        pass

    def get_user_interaction(self):
        running = True
        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                elif event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        running = False
                        pygame.quit()

                    else:
                        print(event.key)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    return event.pos[0], event.pos[1]

    def get_move_location(self, click_x, click_y) -> Tuple[int, int]:

        if click_x < self.vertical_lines[0]:
            column = 0
            self.x_symbol_centre = self.vertical_lines[0] - self.x_position_grid_centre

        elif self.vertical_lines[0] < click_x < self.vertical_lines[1]:
            column = 1
            self.x_symbol_centre = self.vertical_lines[1] - self.x_position_grid_centre
        else:
            column = 2
            self.x_symbol_centre = self.vertical_lines[1] + self.x_position_grid_centre

        if click_y < self.horizontal_lines[0]:
            row = 0
            self.y_symbol_centre = self.horizontal_lines[0] - self.y_position_grid_centre
        elif self.horizontal_lines[0] < click_y < self.horizontal_lines[1]:
            row = 1
            self.y_symbol_centre = self.horizontal_lines[1] - self.y_position_grid_centre
        else:
            row = 2
            self.y_symbol_centre = self.horizontal_lines[1] + self.y_position_grid_centre

        return row, column

    def draw_symbol(self, player_number):
        if player_number == 1:
            self.draw_cross(self.x_symbol_centre, self.y_symbol_centre)
        elif player_number == 2:
            pygame.draw.circle(self.screen,
                               (242, 132, 130),
                               (self.x_symbol_centre, self.y_symbol_centre),
                               self.symbol_size,
                               5)
        pygame.display.flip()

    def draw_cross(self, x, y):
        cross_radius = 0.2 * self.width / 3

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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            my_font = pygame.font.SysFont("menlo", 36)
            text_img = my_font.render(outcome_string, True, (0, 0, 0))
            rect_placement_adjust = 0.1 * self.height
            pygame.draw.rect(self.screen,
                             (245, 202, 195),
                             (0, self.height / 2 - rect_placement_adjust, self.width, rect_placement_adjust * 2),
                             0)
            self.screen.blit(text_img, ((self.width - text_img.get_size()[0])/2,  (self.height - text_img.get_size()[1])/2))
            pygame.display.flip()

    def connect_winning_points(self):
        pass

    def test(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
            my_font = pygame.font.SysFont("menlo", 36)
            text_img = my_font.render(" has won", True, (0, 128, 0))
            rect_placement_adjust = 0.1 * self.height
            pygame.draw.rect(self.screen,
                             (0, 0, 255),
                             (0, self.height / 2 - rect_placement_adjust, self.width, rect_placement_adjust * 2),
                             0)
            self.screen.blit(text_img, ((self.width - text_img.get_size()[0])/2,  (self.height - text_img.get_size()[1])/2))
            pygame.display.flip()


if __name__ == '__main__':
    game_window = GameWindow(800, 800)
    game_window.prepare_board()
    game_window.get_user_interaction(1, -1)
    game_window.game_outcome(0)

