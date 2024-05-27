from dataclasses import dataclass


@dataclass
class Parent:
    attribute1: int


@dataclass
class Child(Parent):
    attribute2: str


# Creating instances of Child
child = Child(10, "hello")

# Printing instance
print(child)  # Outputs: Child(attribute1=10, attribute2='hello')
