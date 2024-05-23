class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


singleton1 = Singleton.instance()
singleton2 = Singleton.instance()
singleton3 = Singleton()
print(singleton1 is singleton2)  # Output: True
print(singleton2 is singleton3)  # Output: True
