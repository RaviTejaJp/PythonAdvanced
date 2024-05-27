from dataclasses import dataclass


@dataclass
class Point:
    x: float
    y: float


# Creating instances of Point
p1 = Point(1.0, 2.0)
p2 = Point(1.0, 2.0)

# Printing instances
print(p1)  # Outputs: Point(x=1.0, y=2.0)

# Checking equality
print(p1 == p2)  # Outputs: True

# Immutable nature
# p1.x = 3.0  # Raises AttributeError: can't set attribute
