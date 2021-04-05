import pygame
import numpy as np
from pygame import color

from environment import dim, env, get_target, get_adjacent

# colors
BLACK = (50, 50, 50)
BLACK2 = (0, 0, 0)
WHITE = (240, 237, 235)
GREEN = (114, 148, 78)
RED = (181, 89, 89)
DARK_GREY = (124, 118, 118)
GREY = (193, 189, 189)

# window
WINDOW_SIZE = (800, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Search and Destroy")
screen.fill(BLACK2)

MARGIN = 1
CELL_SIZE = WINDOW_SIZE[0] / dim - 1

# initializes pygame
pygame.init()

def show_terrain(_env, target):
    """
    Takes in an environment and displays terrain.
    :param _env:
    :return: n/a
    """

    for row in range(dim):
        for col in range(dim):
            e = _env[row][col]
            
            # flat
            if e[0] == 0:
                # color as flat
                # create rectangle with margins based on it's position
                cell = pygame.Rect((MARGIN + CELL_SIZE) * col + MARGIN,
                                   (MARGIN + CELL_SIZE) * row + MARGIN,
                                   CELL_SIZE,
                                   CELL_SIZE)
                # draw cells to the screen
                pygame.draw.rect(screen, WHITE, cell)

            # hilly
            elif e[0] == 1:
                cell = pygame.Rect((MARGIN + CELL_SIZE) * col + MARGIN,
                                   (MARGIN + CELL_SIZE) * row + MARGIN,
                                   CELL_SIZE,
                                   CELL_SIZE)
                pygame.draw.rect(screen, GREY, cell)
            
            # forest
            elif e[0] == 2:
                cell = pygame.Rect((MARGIN + CELL_SIZE) * col + MARGIN,
                                   (MARGIN + CELL_SIZE) * row + MARGIN,
                                   CELL_SIZE,
                                   CELL_SIZE)
                pygame.draw.rect(screen, GREEN, cell)

            # cave
            elif e[0] == 3:
                cell = pygame.Rect((MARGIN + CELL_SIZE) * col + MARGIN,
                                   (MARGIN + CELL_SIZE) * row + MARGIN,
                                   CELL_SIZE,
                                   CELL_SIZE)
                pygame.draw.rect(screen, BLACK, cell)

            if e[1] == True:
                # mark target
                cell = pygame.Rect((MARGIN + CELL_SIZE) * col + MARGIN,
                                    (MARGIN + CELL_SIZE) * row + MARGIN,
                                    CELL_SIZE,
                                    CELL_SIZE)
                font = pygame.font.SysFont('Gill Sans MT', int(1200*CELL_SIZE/800), bold=True)
                text = font.render(str("X"), True, RED)
                text_rect = text.get_rect()
                text_rect.centerx = cell.centerx
                text_rect.centery = cell.centery + 1
                screen.blit(text, text_rect)
    # update entire display so the rectangles are actually drawn on the screen
    pygame.display.flip()


show_terrain(env, get_target)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False