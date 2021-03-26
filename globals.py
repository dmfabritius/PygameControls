import pygame
from pygame import display, font, time, Surface
from pygame.font import Font

FPS = 60

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

GUI_WIDTH = 400
DRAWING_WIDTH = 800

BLACK = (0, 0, 0)  # rgb color
BLUE = (100, 100, 255, 180)  # rgba color
GREEN = (40, 255, 40, 180)
YELLOW = (200, 200, 40)
LIGHT_GRAY = (214, 214, 214)
DARK_GRAY = (80, 80, 80)
DARKER_GRAY = (40, 40, 40)

pygame.init()  # initialize the pygame environment


class Global:
    window = display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), pygame.DOUBLEBUF)  # create a display window

    guiSurface = Surface((GUI_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    drawSurface = Surface((DRAWING_WIDTH, WINDOW_HEIGHT), pygame.SRCALPHA)
    cx = DRAWING_WIDTH * 0.5
    cy = WINDOW_HEIGHT * 0.5

    clock: time.Clock = time.Clock()  # create a reference to the game clock
    font: Font = font.SysFont("Calibri", 18)
    lineColor = BLUE
