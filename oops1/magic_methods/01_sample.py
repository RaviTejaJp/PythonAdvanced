class CustomList:
    def __init__(self, *args):
        self._items = list(args)

    # Representation methods
    def __str__(self):
        return str(self._items)

    def __repr__(self):
        return f'CustomList({", ".join(repr(item) for item in self._items)})'

    # Arithmetic operations
    def __add__(self, other):
        if isinstance(other, CustomList):
            return CustomList(*(self._items + other._items))
        elif isinstance(other, list):
            return CustomList(*(self._items + other))
        else:
            raise TypeError(
                f"unsupported operand type(s) for +: 'CustomList' and '{type(other).__name__}'"
            )

    def __mul__(self, other):
        if isinstance(other, int):
            return CustomList(*(self._items * other))
        else:
            raise TypeError(
                f"unsupported operand type(s) for *: 'CustomList' and '{type(other).__name__}'"
            )

    # Comparison operations
    def __eq__(self, other):
        if isinstance(other, CustomList):
            return self._items == other._items
        return False

    def __lt__(self, other):
        if isinstance(other, CustomList):
            return self._items < other._items
        return NotImplemented

    # Container emulation
    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __delitem__(self, index):
        del self._items[index]

    def __contains__(self, item):
        return item in self._items

    # Attribute access
    def __getattr__(self, name):
        return f"{name} attribute not found"

    def __setattr__(self, name, value):
        if name == "_items":
            super().__setattr__(name, value)
        else:
            self.__dict__[name] = value

    def __delattr__(self, name):
        if name == "_items":
            raise AttributeError("Cannot delete _items attribute")
        else:
            super().__delattr__(name)

    # Context management
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting context")

    # Callable
    def __call__(self, *args, **kwargs):
        print("Called with:", args, kwargs)

    # Object lifecycle
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __del__(self):
        print(f"CustomList instance is being destroyed : {self}")


# Example usage of CustomList class
if __name__ == "__main__":
    cl = CustomList(1, 2, 3)
    customlist = CustomList(1, 2, 3)
    print(cl)  # Uses __str__
    breakpoint()
    print(repr(cl))  # Uses __repr__

    # Arithmetic operations
    cl2 = CustomList(4, 5)
    print(cl + cl2)  # Uses __add__
    print(cl * 2)  # Uses __mul__

    # Comparison operations
    print(cl == CustomList(1, 2, 3))  # Uses __eq__
    print(cl < cl2)  # Uses __lt__

    # Container emulation
    print(len(cl))  # Uses __len__
    print(cl[1])  # Uses __getitem__
    cl[1] = 42  # Uses __setitem__
    print(cl)
    del cl[1]  # Uses __delitem__
    print(cl)
    print(3 in cl)  # Uses __contains__

    # Attribute access
    print(cl.non_existent)  # Uses __getattr__
    cl.new_attr = "Test"  # Uses __setattr__
    print(cl.new_attr)
    del cl.new_attr  # Uses __delattr__

    # Context management
    with CustomList(7, 8, 9) as cl_context:  # Uses __enter__ and __exit__
        print(cl_context)

    # Callable
    cl(10, 20, a=30, b=40)  # Uses __call__

    # Object lifecycle
    cl3 = CustomList(5, 6, 7)  # Uses __new__
    del cl3  # Uses __del__
