with open("example.txt", "r") as file:
    content = file.read()
# The file is automatically closed after this block


class CustomContextManager:
    def __enter__(self):
        print("Entering the context")
        return self  # returning the resource of the context

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")


# Using the custom context manager
with CustomContextManager() as manager:
    print("Inside the context")
