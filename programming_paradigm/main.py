import sys
from robust_division_calculator import safe_divide

def main():
    # Vérification du nombre d'arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        print("Example: python main.py 10 5")
        sys.exit(1)
    
    # Récupération des arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]
    
    # Calcul et affichage du résultat
    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
