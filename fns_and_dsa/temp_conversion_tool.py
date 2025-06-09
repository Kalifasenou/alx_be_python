# alx_be_python/fns_and_dsa/temp_conversion_tool.py

# Define Global Conversion Factors
# These factors are accessible by all functions in this script.
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit: float) -> float:
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.

    Args:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature converted to Celsius.
    """
    # The global FAHRENHEIT_TO_CELSIUS_FACTOR is used here directly.
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius: float) -> float:
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature converted to Fahrenheit.
    """
    # The global CELSIUS_TO_FAHRENHEIT_FACTOR is used here directly.
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Handles user interaction for temperature conversion.
    Prompts for temperature and unit, performs conversion, and displays the result.
    Includes error handling for invalid temperature input.
    """
    try:
        # Prompt user for temperature and attempt to convert to float
        temp_input_str = input("Enter the temperature to convert: ")
        temperature = float(temp_input_str)
    except ValueError:
        # If conversion to float fails, it means the input is not a numeric value
        print("Invalid temperature. Please enter a numeric value.")
        return # Exit the function as invalid temperature cannot be processed

    # Prompt user for the unit and normalize input to uppercase for comparison
    unit_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit_input == 'F':
        # If input is Fahrenheit, convert to Celsius
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    elif unit_input == 'C':
        # If input is Celsius, convert to Fahrenheit
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    else:
        # Handle cases where the unit input is neither 'C' nor 'F'
        print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

if __name__ == "__main__":
    main()