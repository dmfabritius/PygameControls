from typing import Dict, Sequence
import pygame
from pygame import display, draw as pygame_draw, event as pygame_event
import math
import random
from control import Control
from slider import Slider
from checkbox import Checkbox
from button import Button
from label import Label
from globals import *


class Program:

    def __init__(self):
        self.running = True
        self.numLoops = 300  # the number of times to loop around the circle
        self.step = 0.05    # take little steps
        self.spinAngle = 0.0
        self.controls: Dict[str, Control] = {
            "lblNumerator": Label((10, 14), "Numerator:"),
            "Numerator": Slider((150, 20), 1, 10, 4.3, 0.1),
            "lblDenominator": Label((10, 44), "Denominator:"),
            "Denominator": Slider((150, 50), 1, 10, 7.6, 0.1),
            "lblSpinning": Label((10, 80), "Spin?"),
            "Spinning": Checkbox((150, 80), True),
            "lblSpeed": Label((10, 104), "Spin speed:"),
            "Speed": Slider((150, 110), 1, 50, 3, 1),
            "lblScale": Label((10, 144), "Scale:"),
            "Scale": Slider((150, 150), 50, 380, 200, 10),
            "Color": Button((150, 200), "Change Color", Program.ChangeColor),
        }

    def run(self):
        while self.running:  # the main game/drawing loop
            self.handleEvents()
            self.update()
            self.draw()
            Global.clock.tick(FPS)

    def handleEvents(self):
        for event in pygame_event.get():  # process all events
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            for c in self.controls.values():
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    c.update(True, event.pos)
                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    c.update(False, event.pos)
                elif event.type == pygame.MOUSEMOTION:
                    c.move(event.pos)

    def update(self):
        spinning: Checkbox = self.controls["Spinning"]
        if spinning.checked:
            self.spinAngle += (0.001 * self.controls["Speed"].value)
        self.vertices: Sequence[pygame_draw._Coordinate] = []
        a = 0.0
        while a < self.numLoops:  # loop around and around in a circle
            k = self.controls["Numerator"].value / self.controls["Denominator"].value
            r = self.controls["Scale"].value * math.cos(k * (a + self.spinAngle))  # calculate a radius that varies proportionally to the cosine of the angle
            x = r * math.cos(a) + Global.cx
            y = r * math.sin(a) + Global.cy
            self.vertices.append((x, y))
            a += self.step

    def draw(self):
        Global.window.fill(BLACK)  # clear display window

        Global.drawSurface.fill(DARKER_GRAY)  # clear drawing surface
        pygame_draw.aalines(Global.drawSurface, Global.lineColor, False, self.vertices, 1)
        #image = pygame.transform.rotate(Global.drawSurface, self.spinAngle)
        # rect = image.get_rect(center = (GUI_WIDTH + Global.cx, Global.cy)) # set the position of the image's center
        # Global.window.blit(image, rect)  # draw the rotated surface onto the window
        Global.window.blit(Global.drawSurface, (GUI_WIDTH, 0))

        Global.guiSurface.fill(BLACK)  # clear GUI surface
        for c in self.controls.values():
            c.draw(Global.guiSurface)  # draw all controls onto the GUI surface
        Global.window.blit(Global.guiSurface, (0, 0))  # draw the surface onto the window

        display.update()

    @staticmethod
    def ChangeColor():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        Global.lineColor = (r, g, b)

### Start of Execution ####################################


# code in globals.py runs first via import statement above
Program().run()
