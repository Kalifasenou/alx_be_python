# pattern_drawing.py

def draw_square_pattern():
    """Utilize while loops and nested for loops to draw a simple text-based pattern.    """
    #  input a positive integer
    size = int(input("Enter the size of the pattern: "))
    
    # Initialisation du compteur de lignes
    row = 0
    
    # Boucle while pour gérer chaque ligne
    while row < size:
        # Boucle for pour imprimer les astérisques sur une ligne
        for col in range(size):
            print("*", end="")
        
        # Passage à la ligne suivante après chaque rangée
        print()
        row += 1

if __name__ == "__main__":
    draw_square_pattern()
