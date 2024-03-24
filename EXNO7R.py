def divide_numbers():
    try:
        # Get user input for two numbers
        while True:
            num1 = input("Enter the first number (or 'q' to quit): ")
            if num1.lower() == 'q':
                return
            num1 = float(num1)

            num2 = input("Enter the second number (or 'q' to quit): ")
            if num2.lower() == 'q':
                return
            num2 = float(num2)

            # Perform division
            result = num1 / num2
            print(f"The result of division is: {result}")

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    divide_numbers()