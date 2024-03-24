import math
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        print("Division by zero is not allowed.")
    return x / y

def square_root(x):
    if x < 0:
        print("Square root of negative number is not defined.")
    return math.sqrt(x)