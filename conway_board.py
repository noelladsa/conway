import pygame
import pygcurse
import sys
import random

HEIGHT = 41
WIDTH = 41
FPS = 40
BLUE = (0, 0, 128)
BLACK = (0, 0, 0)


class ConwayBoard(object):

    def __init__(self, board, width, height):
        self.board = board
        self.w = width
        self.h = height

    def _get_neighbours(self, i, j):
        return [(x, y) for x in range(i-1, i+2)
                for y in range(j-1, j+2)
                if (0 <= x < self.h) and  # Neighbour is in board
                (0 <= y < self.w) and    # Neighbour is in board
                (x, y) != (i, j)           # Ignore current element
                ]

    def _check_rules(self, live_count, old_state):
        if old_state:
            if live_count < 2 or live_count > 3:
                return 0
            if 2 <= live_count <= 3:
                return 1
        else:
            if live_count == 3:
                return 1
        return 0

    def _get_next_state(self, i, j):
        if i > self.h or i < 0:
            return
        if j > self.w or j < 0:
            return
        neighbours = self._get_neighbours(i, j)
        live_count = 0
        for (x, y) in neighbours:
            if self.board[x][y]:
                live_count += 1

        return self._check_rules(live_count, self.board[i][j])

    def get_next_board(self):
        self.board = [[self._get_next_state(j, i)
                      for i in range(0, self.w)]
                      for j in range(0, self.h)]
        return self.board


def read_board():
    return


def generate_board():
    return [[random.choice((1, 0)) for x in range(10)] for y in range(10)]


def get_initial_board():
    init_board = read_board()
    if init_board:
        return init_board
    return generate_board()


def get_board_dimens(board):
    h = len(board)
    w = len(board[0])
    return w, h


def draw_board(win, board):
    w, h = get_board_dimens(board)
    for x in range(h):
        for y in range(w):
            if board[x][y]:
                win.paint(x, y, BLUE)
            else:
                win.paint(x, y, BLACK)


def game_loop():
    clock = pygame.time.Clock()
    win = pygcurse.PygcurseWindow(30, 25)
    board = get_initial_board()
    w, h = get_board_dimens(board)
    game = ConwayBoard(board, w, h)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                pygame.quit()
                sys.exit()
        draw_board(win, board)
        board = game.get_next_board()
        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    game_loop()
