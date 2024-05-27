class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        return "Engine started"


class Car:
    def __init__(self, model, horsepower):
        self.model = model
        self.engine = Engine(horsepower)

    def start(self):
        return f"{self.model}: {self.engine.start()}"


# Creating a Car instance
car = Car("Toyota", 120)

# Using the Car instance
print(car.start())  # Outputs: Toyota: Engine started
