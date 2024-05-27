from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def make_sound(self):
        return "Woof"

    def move(self):
        return "Run"


class Bird(Animal):

    def make_sound(self):
        return "Chirp"

    def move(self):
        return "Fly"


# Attempting to instantiate an abstract class will raise an error
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods make_sound, move

dog = Dog()
print(dog.make_sound())  # Output: Woof
print(dog.move())  # Output: Run

bird = Bird()
print(bird.make_sound())  # Output: Chirp
print(bird.move())  # Output: Fly
