class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative numbers are not allowed: {value}")


def check_positive(number):
    if number < 0:
        raise NegativeNumberError(number)
    return number


def process_numbers(numbers):
    for number in numbers:
        try:
            print(check_positive(number))
        except NegativeNumberError as e:
            print(e)


numbers = [10, -5, 20, -1]
process_numbers(numbers)
