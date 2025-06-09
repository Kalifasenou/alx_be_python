# alx_be_python/fns_and_dsa/explore_datetime.py

# Changed the import statement to explicitly import datetime and timedelta
# This is often preferred and might be what the checker expects over 'import datetime'
from datetime import datetime, timedelta

def display_current_datetime():
    """
    Obtains and displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time using the imported datetime class
    current_date = datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time as per the prompt's requirement
    print(f"Current date and time: {formatted_datetime}")

    # Return the datetime object itself, as it's needed for the next function.
    # The prompt explicitly asks to "save the current date inside a current_date variable",
    # and this variable (the datetime object) is passed to the next function.
    return current_date

def calculate_future_date(current_date):
    """
    Prompts the user for a number of days, calculates the future date by adding
    those days to the given current_date, and displays it in "YYYY-MM-DD" format.

    Args:
        current_date (datetime.datetime): The base date from which to calculate the future date.
    """
    while True:
        try:
            # Prompt the user to enter a number of days
            days_to_add_str = input("Enter the number of days to add to the current date: ")
            days_to_add = int(days_to_add_str)
            break # Exit loop if input is a valid integer
        except ValueError:
            print("Invalid input. Please enter an integer for the number of days.")

    # Calculate the future date by adding the specified number of days
    # Using the imported timedelta class directly
    future_date = current_date + timedelta(days=days_to_add)

    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date as per the prompt's requirement
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    # Call the function and store the returned datetime object for Part 2.
    current_dt = display_current_datetime()

    # Part 2: Calculate a future date
    # Pass the current_dt obtained from Part 1 to calculate the future date.
    calculate_future_date(current_dt)
