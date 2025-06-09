# alx_be_python/fns_and_dsa/temp_conversion_tool.py

# Define Global Conversion Factors exactly as specified to ensure checker compatibility
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # Uses the globally defined FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # Uses the globally defined CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Handles user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays the result.
    Includes error handling for invalid temperature input.
    """
    try:
        # Prompt for temperature and attempt to convert to float
        temp_input_str = input("Enter the temperature to convert: ")
        temperature = float(temp_input_str)
    except ValueError:
        # If input is not a valid number, print the specified error message and exit.
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the main function

    # Prompt for the unit (C/F) and convert to uppercase for case-insensitive comparison
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit_input == 'F':
        # If the unit is Fahrenheit, convert to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit_input == 'C':
        # If the unit is Celsius, convert to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Handle invalid unit input
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()

