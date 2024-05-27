# Extensively used in our code base
# If it looks like a duck and quacks like a duck then it should be duck


class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm quacking like a duck!"


def animal_speak(animal):
    if hasattr(animal, "speak"):
        print(animal.speak())
    elif hasattr(animal, "quack"):
        print(animal.quack())
    else:
        print("Unknown animal sound")


dog = Dog()
cat = Cat()
duck = Duck()
person = Person()

animal_speak(dog)  # Outputs: Woof!
animal_speak(cat)  # Outputs: Meow!
animal_speak(duck)  # Outputs: Quack!
animal_speak(person)  # Outputs: I'm quacking like a duck!
