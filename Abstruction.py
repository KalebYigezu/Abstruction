import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


rect = Rectangle(5, 10)
print(rect.area())  # Output: 50
print(rect.perimeter())  # Output: 30

circle = Circle(5)
print(circle.area())  # Output: 78.53981633974483
print(circle.perimeter())  # Output: 31.41592653589793
