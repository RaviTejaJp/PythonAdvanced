from abc import ABC, abstractmethod


class Flyable(ABC):

    @abstractmethod
    def fly(self):
        pass


class Swimmable(ABC):

    @abstractmethod
    def swim(self):
        pass


# in other languages like Java inheriting more than one abstract class is not allowed
# for that behavior they use interfaces
class Duck(Flyable, Swimmable):

    def fly(self):
        return "Duck flying"

    def swim(self):
        return "Duck swimming"


duck = Duck()
print(duck.fly())  # Output: Duck flying
print(duck.swim())  # Output: Duck swimming
