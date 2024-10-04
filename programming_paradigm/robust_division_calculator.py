def safe_divide(numerator, denominator):
  """
  Performs division with robust error handling for division by zero and non-numeric input.

  Args:
      numerator (str or float): The numerator of the division.
      denominator (str or float): The denominator of the division.

  Returns:
      str: A message indicating the result or an error message.
  """
  try:
    # Attempt conversion to floats and perform division
    numerator = float(numerator)
    denominator = float(denominator)
    result = numerator / denominator
    return f"The result of the division is {result:.2f}"  # Format result with 2 decimals
  except ZeroDivisionError:
    return "Error: Cannot divide by zero."
  except ValueError:
    return "Error: Please enter numeric values only."