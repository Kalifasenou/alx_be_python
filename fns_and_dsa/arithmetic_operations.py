# alx_be_python/fns_and_dsa/arithmetic_operations.py

def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations based on the given numbers and operation.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operation (str): The arithmetic operation to perform.
                         Accepted values are 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: The result of the operation if successful,
                      or an error message string if division by zero occurs.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            # Handle division by zero error
            return "Error: Division by zero"
        else:
            return num1 / num2
    else:
        # This case handles any unrecognised operation strings,
        # although the prompt implies only valid operations will be provided.
        return "Error: Invalid operation"