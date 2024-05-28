class DefaultMethodMeta(type):
    def __new__(cls, name, bases, dct):
        # Check if the class already has a method named 'default_method'
        if "default_method" not in dct:
            # Define a default method and add it to the class dictionary
            def default_method(self):
                return f"Default method called from {self.__class__.__name__}"

            dct["default_method"] = default_method
        return super().__new__(cls, name, bases, dct)


# Using the DefaultMethodMeta metaclass to define a class
class MyClass(metaclass=DefaultMethodMeta):
    pass


# Creating an instance of MyClass and calling the default method
obj = MyClass()
print(obj.default_method())  # Outputs: Default method called from MyClass
