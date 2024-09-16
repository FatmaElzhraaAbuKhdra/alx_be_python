# Input numbers from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# Perform operation based on the chosen operator using match-case
match operator:
    case '+':
        result = f"The result is {num1 + num2}."
    case '-':
        result = f"The result is {num1 - num2}."
    case '*':
        result = f"The result is {num1 * num2}."
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
            result = None  # Avoid printing result if there's an error
        else:
            result = f"The result is {num1 / num2}."
    case _:
        print("Error: Invalid operation. Please enter +, -, *, or /.")
        result = None  # Avoid printing result if there's an error

# Print the result if it was calculated successfully
if result is not None:
    print(result)
