import math

from shape import Shape
from color import Color


class Circle(Shape):
    def __init__(self, radius: float, color: Color):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius
