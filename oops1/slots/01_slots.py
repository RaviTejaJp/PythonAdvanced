class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Creating instances of Point
p1 = Point(1, 2)
p2 = Point(3, 4)

# Accessing attributes
print(p1.x, p1.y)  # Outputs: 1 2
print(p2.x, p2.y)  # Outputs: 3 4

# Trying to add a new attribute raises an AttributeError
# p1.z = 5  # Raises AttributeError: 'Point' object has no attribute 'z'
