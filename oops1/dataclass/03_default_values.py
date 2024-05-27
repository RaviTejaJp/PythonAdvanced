from dataclasses import dataclass


@dataclass
class MyClass:
    attribute1: int = 0
    attribute2: str = "default"

    def custom_method(self):
        return f"Custom method: {self.attribute1}, {self.attribute2}"


# Creating instance of MyClass
obj = MyClass(100, "custom")

# Printing instance and custom method output
print(obj)  # Outputs: MyClass(attribute1=100, attribute2='custom')
print(obj.custom_method())  # Outputs: Custom method: 100, custom
