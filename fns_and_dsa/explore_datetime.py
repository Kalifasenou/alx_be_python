# alx_be_python/fns_and_dsa/explore_datetime.py

import datetime

def display_current_datetime():
    """
    Obtains and displays the current date and time in "YYYY-MM-DD HH:MM:SS" format.
    """
    # Get the current date and time
    current_date = datetime.datetime.now()

    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print(f"Current date and time: {formatted_datetime}")
    return current_date # Return current_date for potential use in other functions, as it's needed for calculate_future_date.

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
    # A timedelta object represents a duration
    future_date = current_date + datetime.timedelta(days=days_to_add)

    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")

    # Print the future date
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    # Part 1: Display the current date and time
    # Call the function to get and display the current date and time,
    # storing the returned datetime object for Part 2.
    current_dt = display_current_datetime()

    # Part 2: Calculate a future date
    # Pass the current_dt obtained from Part 1 to calculate the future date.
    calculate_future_date(current_dt)
