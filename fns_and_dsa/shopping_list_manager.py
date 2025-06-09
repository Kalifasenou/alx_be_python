# alx_be_python/fns_and_dsa/shopping_list_manager.py

def display_menu():
    """
    Displays the menu options for the shopping list manager.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Manages adding, removing, and viewing items in the shopping list.
    """
    shopping_list = []  # Initialize an empty list for the shopping list

    while True:
        display_menu()  # Display the menu options
        choice = input("Enter your choice: ").strip() # Get user's choice and remove leading/trailing whitespace

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item: # Ensure the item name is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please try again.")
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue # Skip to the next loop iteration
            
            item_to_remove = input("Enter the item to remove: ").strip()
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' not found in your shopping list.")
        elif choice == '3':
            # View List functionality
            if not shopping_list: # Check if the list is empty
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1): # Enumerate to display numbered list
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit functionality
            print("Goodbye! Thank you for using the Shopping List Manager.")
            break # Exit the loop
        else:
            # Handle invalid choices
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main() # Call the main function when the script is executed