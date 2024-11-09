from abc import ABC, abstractmethod

from color import Color


class Shape(ABC):
    def __init__(self, color: Color):
        self.color = color

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        return (f"Drawing {self.color.fill()} {self.__class__.__name__} with area {self.area()} "
                f"and perimeter {self.perimeter()}")
