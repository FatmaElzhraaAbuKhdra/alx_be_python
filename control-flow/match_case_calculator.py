# Input numbers from user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

# Perform operation based on the chosen operator
match operator:
    case '+':
        result = int(num1 + num2)  # Convert result to integer
        print(f"The result is {result}.")
    case '-':
        result = int(num1 - num2)  # Convert result to integer
        print(f"The result is {result}.")
    case '*':
        result = int(num1 * num2)  # Convert result to integer
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = int(num1 / num2)  # Convert result to integer
            print(f"The result is {result}.")
    case _:
        print("Error: Invalid operation. Please enter +, -, *, or /.")
