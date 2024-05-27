class Battery:
    def __init__(self, capacity):
        self.capacity = capacity


class Laptop:
    def __init__(self, brand, battery):
        self.brand = brand
        self.battery = battery


# Creating a Battery instance
battery = Battery(5000)

# Creating a Laptop instance with the existing Battery instance
laptop = Laptop("Dell", battery)

# Using the Laptop instance
print(
    f"{laptop.brand} with battery capacity: {laptop.battery.capacity}mAh"
)  # Outputs: Dell with battery capacity: 5000mAh
