class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def instance_method(self):
        return f"Instance method: Ingredients are {self.ingredients}"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomato"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomato", "ham"])

    @staticmethod
    def calculate_area(radius):
        import math

        return math.pi * radius**2


# Instance method
pizza = Pizza(["cheese", "tomato"])
print(pizza.instance_method())  # Instance method: Ingredients are ['cheese', 'tomato']

# Class methods
margherita = Pizza.margherita()
print(
    margherita.instance_method()
)  # Instance method: Ingredients are ['mozzarella', 'tomato']

prosciutto = Pizza.prosciutto()
print(
    prosciutto.instance_method()
)  # Instance method: Ingredients are ['mozzarella', 'tomato', 'ham']

# Static method
print(Pizza.calculate_area(7))  # 153.93804002589985
