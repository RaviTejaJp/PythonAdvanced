from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello():
    """This is the say_hello function."""
    print("Hello!")


say_hello()
print(say_hello.__name__)  # say_hello
print(say_hello.__doc__)  # This is the say_hello function.
