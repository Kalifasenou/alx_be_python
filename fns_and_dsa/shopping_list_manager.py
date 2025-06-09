# alx_be_python/fns_and_dsa/shopping_list_manager.py

def display_menu():
    """
    Displays the menu options for the shopping list manager.
    Strictly matches the skeleton's print statements.
    """
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """
    Main function to run the shopping list manager.
    Implements adding, removing, and viewing items using a list.
    """
    shopping_list = [] # Initialize an empty list as per skeleton

    while True:
        display_menu() # Call display_menu as per skeleton
        choice = input("Enter your choice: ") # Get user's choice, exactly as per skeleton (without .strip())

        if choice == '1':
            # Logic for adding an item
            item = input("Enter the item to add: ").strip() # Keep .strip() for user-entered item name
            if item: # Ensure item is not empty
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            else:
                print("Item name cannot be empty. Please enter a valid item.")
        elif choice == '2':
            # Logic for removing an item
            if not shopping_list:
                print("Your shopping list is empty. Nothing to remove.")
                continue # Skip the rest of this iteration if list is empty

            item_to_remove = input("Enter the item to remove: ").strip() # Keep .strip() for user-entered item name
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from your shopping list.")
            else:
                print(f"'{item_to_remove}' not found in your shopping list.")
        elif choice == '3':
            # Logic for displaying the shopping list
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("\n--- Your Shopping List ---")
                for i, item in enumerate(shopping_list, 1):
                    print(f"{i}. {item}")
                print("--------------------------")
        elif choice == '4':
            # Exit functionality, exactly as per skeleton
            print("Goodbye!")
            break # Exit the loop
        else:
            # Handle invalid choices, exactly as per skeleton
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
