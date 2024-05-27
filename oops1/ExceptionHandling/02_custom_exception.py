class CustomError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"CustomError: {self.message}"


# Raising the custom exception
def risky_operation():
    raise CustomError("Something went wrong in the risky operation")


try:
    risky_operation()
except CustomError as e:
    print(e)  # Outputs: CustomError: Something went wrong in the risky operation
