# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5


def convert_to_celsius(fahrenheit):
  """Converts temperature from Fahrenheit to Celsius.

  Args:
      fahrenheit: The temperature in Fahrenheit.

  Returns:
      The temperature in Celsius.
  """
  return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
  """Converts temperature from Celsius to Fahrenheit.

  Args:
      celsius: The temperature in Celsius.

  Returns:
      The temperature in Fahrenheit.
  """
  return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
  """Prompts user for temperature, converts it, and displays the result."""
  try:
    temperature = float(input("Enter the temperature to convert: "))
  except ValueError:
    raise ValueError("Invalid temperature. Please enter a numeric value.")

  unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

  if unit == "C":
    converted_temp = convert_to_fahrenheit(temperature)
    print(f"{temperature:.1f}°C is {converted_temp:.1f}°F")
  elif unit == "F":
    converted_temp = convert_to_celsius(temperature)
    print(f"{temperature:.1f}°F is {converted_temp:.1f}°C")
  else:
    print("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
  main()