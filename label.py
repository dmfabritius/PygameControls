from typing import Tuple
from globals import *
from control import Control


class Label(Control):

    def __init__(self, position: Tuple[float, float] = (0, 0), text: str = "label"):
        "A basic text label."
        super().__init__()
        self.position = position
        self.text = text
        self.label = Global.font.render(self.text, True, LIGHT_GRAY)

    def draw(self, surface: Surface):
        surface.blit(self.label, self.position)
