from typing import Tuple
from pygame import Surface


class Control:

    def __init__(self):
        self.value: float = 0.0

    def move(self, position: Tuple[float, float]):
        pass  # controls can optionally overwrite this default move() method

    def update(self, mousedown: bool, position: Tuple[float, float]):
        pass  # controls can optionally overwrite this default update() method

    def draw(self, surface: Surface):
        raise Exception("All controls need to implement a draw() method")
