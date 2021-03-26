from typing import Tuple
import pygame
from pygame import draw as pygame_draw
from globals import *
from control import Control


class Slider(Control):

    def __init__(self, position: Tuple[float, float] = (0, 0), min: float = 0, max: float = 20, value: float = 10, step: float = 2):
        "A basic slider."
        super().__init__()
        self.dragging = False
        self.bar = pygame.Rect(position[0], position[1], 200, 3)
        self.bounds = pygame.Rect(0, self.bar.y - 8, 10, 19)
        self.min = min
        self.max = max
        self.step = step
        self.markerStep = (self.bar.width - self.bounds.width) / ((max - min) / self.step)
        self.setValue(value)

    def setValue(self, value: float):
        self.value = min(max(value, self.min), self.max)
        self.label = Global.font.render(str(round(self.value, 2)), True, YELLOW)
        self.bounds.x = self.bar.x + ((self.value - self.min) / self.step * self.markerStep)

    def move(self, position: Tuple[float, float]):
        if self.dragging:
            mouse_x = position[0]
            value = self.min + self.step * ((mouse_x - self.bar.x) / self.markerStep)
            value = round(value / self.step) * self.step
            self.setValue(value)

    def update(self, mousedown: bool, position: Tuple[float, float]):
        self.dragging = mousedown and self.bounds.collidepoint(position)

    def draw(self, surface: Surface):
        surface.fill(LIGHT_GRAY, self.bar)
        pygame_draw.line(surface, DARK_GRAY,
                         (self.bar.left, self.bar.top + 1),
                         (self.bar.right, self.bar.top + 1))
        surface.fill(BLUE, self.bounds)
        surface.blit(self.label, (self.bar.right + 10, self.bar.y - 6))
