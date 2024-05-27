class Duck:
    def quack(self):
        return "Quack!"


class Person:
    def quack(self):
        return "I'm quacking like a duck!"


def make_it_quack(thing):
    print(thing.quack())


duck = Duck()
person = Person()

make_it_quack(duck)  # Outputs: Quack!
make_it_quack(person)  # Outputs: I'm quacking like a duck!
