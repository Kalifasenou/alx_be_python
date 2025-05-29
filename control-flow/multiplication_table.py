# multiplication_table

def generate_multiplication_table():
    """
   Use a for loop to generate and print the multiplication table for a given number
    """
    # input number
    number = float(input("Enter a number to see its multiplication table: "))
    
    # Generate and Print the Multiplication Table
    print(f"\nMultiplication table for {number}:")
    for i in range(1, 11):
        product = number * i
        print(f"{number} * {i} = {product}")

if __name__ == "__main__":
    generate_multiplication_table()
