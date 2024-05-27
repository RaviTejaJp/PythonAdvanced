def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    else:
        print("Division successful")
        return result
    finally:
        print("Execution completed")


print(divide(10, 2))  # Outputs: Division successful, Execution completed, 5.0
print(divide(10, 0))  # Outputs: Error: division by zero, Execution completed, None
