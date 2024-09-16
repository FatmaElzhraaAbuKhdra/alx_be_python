# match_case_calculator.py

# Prompt user for input
num1 = float(input("Enter the first number: ").strip() ) # Use float to handle decimal numbers
num2 = float(input("Enter the second number: ").strip())  # Use float to handle decimal numbers
operator = input("Choose the operation (+, -, *, /): ").strip()  # Ask for the operation

# Perform calculation based on the chosen operation using Match Case
match operator:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            exit()  # Exit the script if division by zero is attempted
        result = num1 / num2
    case _:
        print("Error: Invalid operation. Please enter +, -, *, or /.")
        exit()  # Exit the script if the operation is invalid

# Print result, formatting as integer if possible
if result.is_integer():
    result = int(result)  # Convert to integer if there’s no decimal part

print(f"The result is {result}.")

