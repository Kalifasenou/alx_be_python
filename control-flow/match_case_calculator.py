# match_case_calculator.py

def simple_calculator():
    """
    Calculette simple utilisant l'instruction match-case
    pour gérer les opérations arithmétiques de base.
    """
    # Saisie des nombres
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Saisie de l'opération
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    # Traitement avec match-case
    match operation:
        case "+":
            result = num1 + num2
            print(f"The result is {result}")
        case "-":
            result = num1 - num2
            print(f"The result is {result}")
        case "*":
            result = num1 * num2
            print(f"The result is {result}")
        case "/":
            if num2 == 0:
                print("Cannot divide by zero")
            else:
                result = num1 / num2
                print(f"The result is {result}")
        case _:
            print(f"Invalid operation: '{operation}'. Please use +, -, *, or /")

if __name__ == "__main__":
    simple_calculator()
