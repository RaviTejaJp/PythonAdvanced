class Car:
    car_count = 0

    def __init__(self, name):
        self.name = name
        Car.car_count += 1

    @classmethod
    def car_made_count(cls):
        return cls.car_count


print(f"cars made till now - {Car.car_made_count()}")
Car("Punch")
Car("Nexon")
print(f"cars made till now - {Car.car_made_count()}")
