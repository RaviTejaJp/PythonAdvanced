from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        return "I am a shape"


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


rectangle = Rectangle(3, 4)
print(rectangle.area())  # Output: 12
print(rectangle.perimeter())  # Output: 14
print(rectangle.describe())  # Output: I am a shape
