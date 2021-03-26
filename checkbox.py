from typing import Tuple
import pygame
from pygame import draw as pygame_draw
from globals import *
from control import Control


class Checkbox(Control):

    def __init__(self, position: Tuple[float, float] = (0, 0), checked: bool = False):
        "A basic checkbox."
        super().__init__()
        self.checked: bool = checked
        self.bounds = pygame.Rect(position[0], position[1], 16, 16)
        self.checkmark = [
            (self.bounds.x + 3, self.bounds.y + 8),
            (self.bounds.x + 6, self.bounds.y + 11),
            (self.bounds.x + 12, self.bounds.y + 4)
        ]

    def update(self, mousedown: bool, position: Tuple[float, float]):
        if mousedown and self.bounds.collidepoint(position):
            self.checked = not self.checked

    def draw(self, surface: Surface):
        pygame_draw.rect(surface, LIGHT_GRAY, self.bounds, 1)
        if self.checked:
            pygame_draw.lines(surface, LIGHT_GRAY, False, self.checkmark, 2)
