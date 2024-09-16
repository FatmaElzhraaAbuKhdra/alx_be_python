num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# نحاول تحويل المدخلات إلى أرقام صحيحة
try:
    num1 = int(num1)
    num2 = int(num2)
except ValueError:
    print("Error: Invalid number entered. Please enter valid integers.")
    exit()

<<<<<<< HEAD
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
=======
>>>>>>> 72b6fe34fe2f9441e975aeebdb82b174b9ac51f7
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print("Error: Invalid operation. Please enter +, -, *, or /.")

