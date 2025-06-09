def safe_divide(numerator, denominator):
    """
    Effectue une division sécurisée avec gestion d'erreurs
    
    Args:
        numerator: Numérateur (chaîne ou numérique)
        denominator: Dénominateur (chaîne ou numérique)
    
    Returns:
        float | str: Résultat de la division ou message d'erreur
    """
    try:
        # Conversion des entrées en nombres flottants
        num = float(numerator)
        den = float(denominator)
    except ValueError:
        return "Error: Please enter numeric values only."
    
    try:
        # Tentative de division
        result = num / den
        return f"The result of the division is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
