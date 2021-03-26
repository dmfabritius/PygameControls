from typing import Tuple
import pygame
from pygame import draw as pygame_draw
from globals import *
from control import Control


class Button(Control):

    def __init__(self, position: Tuple[float, float] = (0, 0), text: str = "Button", action=None):
        "A basic button."
        super().__init__()
        self.action = action
        self.text = text
        self.color = DARK_GRAY
        self.label = Global.font.render(self.text, True, LIGHT_GRAY)
        w = self.label.get_width() + 20
        h = self.label.get_height() + 8
        self.bounds = pygame.Rect(position[0], position[1], w, h)

    def update(self, mousedown: bool, position: Tuple[float, float]):
        if mousedown and self.bounds.collidepoint(position):
            self.color = BLUE
            if self.action != None:
                self.action()
        else:
            self.color = DARK_GRAY

    def draw(self, surface: Surface):
        surface.fill(self.color, self.bounds)
        pygame_draw.rect(surface, LIGHT_GRAY, self.bounds, 1)
        surface.blit(self.label, (self.bounds.x + 9, self.bounds.y + 5))
