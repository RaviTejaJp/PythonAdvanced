class Person:
    def __init__(self, name, age):
        self._name = name  # Private attribute with underscore prefix
        self._age = age  # Private attribute with underscore prefix

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

    # Optional deleter for age
    @age.deleter
    def age(self):
        del self._age


# Example usage
person = Person("Alice", 30)

# Accessing the attributes
print(person.name)  # Alice
print(person.age)  # 30

# Modifying the attributes
person.name = "Bob"
person.age = 25

print(person.name)  # Bob
print(person.age)  # 25

# Attempting to set invalid values
try:
    person.name = 123  # Raises ValueError
except ValueError as e:
    print(e)  # Name must be a string

try:
    person.age = -10  # Raises ValueError
except ValueError as e:
    print(e)  # Age must be a non-negative integer

# Deleting the age attribute
del person.age
