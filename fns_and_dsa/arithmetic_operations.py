def perform_operation(num1: float, num2: float, operation: str) -> float | str:
    """
    Effectue des opérations arithmétiques de base sur deux nombres.
    
    Args:
        num1: Premier nombre (float)
        num2: Deuxième nombre (float)
        operation: Type d'opération ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        Résultat de l'opération (float) ou message d'erreur en cas de division par zéro (str)
    """
    operation = operation.lower()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        raise ValueError(f"Invalid operation: {operation}. Use 'add', 'subtract', 'multiply', or 'divide'")
