a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
operation = input("Enter the operation (+, -, * or /): ")
if operation == "+":
    print(a + b)
elif operation == "-":
    print(a - b)
elif operation == "*":
    print(a * b)
elif operation == "/":
    print(a / b)
else:
    print("Error")
