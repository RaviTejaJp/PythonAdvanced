def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    else:
        print("Division successful")
    finally:
        print("Execution completed")


def test():
    try:
        divide(10, 0)
    except Exception as e:
        print("---")


print(divide(10, 2))  # Outputs: Division successful, Execution completed, 5.0
divide(10, 0)  # Outputs: Error: division by zero, Execution completed, None
