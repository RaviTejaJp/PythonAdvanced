def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")

    return wrapper


@my_decorator
def say_hello():
    print("Hello!")


def testing_other_way():
    print("Testing other way")


say_hello()
testing_other_way = my_decorator(testing_other_way)
testing_other_way()
