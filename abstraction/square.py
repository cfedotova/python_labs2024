from color import Color
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, side: float, color: Color):
        super().__init__(side, side, color)
