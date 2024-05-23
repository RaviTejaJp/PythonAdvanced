class Animal:
    species = "Animal"

    @classmethod
    def get_species(cls):
        return cls.species


class Dog(Animal):
    species = "Canine"


print(Dog.get_species())  # Output: Canine
