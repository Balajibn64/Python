#math_operations.py
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
import math_operations
print("***Mathematical operations usingmodule***")
print("Please select an operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
operation = input("Enter the number of the operation you want to perform: ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number:"))
if operation == '1':
    print(f"The sum of {num1} and {num2} is {math_operations.add(num1, num2)}")
elif operation == '2':
    print(f"The difference of {num1} and {num2} is {math_operations.subtract(num1,
num2)}")
elif operation == '3':
    print(f"The product of {num1} and {num2} is {math_operations.multiply(num1, num2)}")
elif operation == '4':
    print(f"The quotient of {num1} and {num2} is {math_operations.divide(num1, num2)}")
else:
    print("Invalid input!")