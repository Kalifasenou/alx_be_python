def perform_operation(num1, num2, operation):
    """
    Effectue des opérations arithmétiques de base
    
    Args:
        num1: Premier nombre
        num2: Deuxième nombre
        operation: Opération à effectuer (add, subtract, multiply, divide)
    
    Returns:
        Résultat ou message d'erreur
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
        raise ValueError(f"Invalid operation: {operation}")
