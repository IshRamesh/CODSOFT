num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter your choice (1/2/3/4): ")

if choice == '1' or choice == '+':
    result = num1 + num2
    print("Result: ", result)
elif choice == '2' or choice == '-':
    result = num1 - num2
    print("Result: ", result)
elif choice == '3' or choice == '*':
    result = num1 * num2
    print("Result: ", result)
elif choice == '4' or choice == '/':
    if num2 != 0:
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid input. Please enter 1, 2, 3, or 4.")
