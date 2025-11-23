def divide_numbers(a, b):
    """
    Divide two numbers with safe error handling.

    Returns the result of a / b.
    If invalid input or division by zero occurs,
    a descriptive error message is returned.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except TypeError:
        return "Error: Inputs must be numbers."


def main_division():
    """
    Gets two numbers from the user and calls the division function.
    Handles non-numeric input and prints the result or an error message.
    """
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Error: Please enter valid numeric values.")
        return

    result = divide_numbers(a, b)
    print("Result:", result)


# Run division input program
main_division()
