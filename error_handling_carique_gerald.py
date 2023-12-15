import math

def calculator():
    previous_results = {}

    while True:
        try:
            num1 = input("Enter the first number (q to quit): ")
            
            if num1.lower() == 'q':
                break

            num1 = float(num1)

            num2 = float(input("Enter the second number: "))
            operation = input("Select operation (+, -, *, /, ** for exponentiation, sqrt for square root): ")

            if operation == 'sqrt':
                if num2 < 0:
                    raise ValueError("Cannot calculate the square root of a negative number.")
                result = math.sqrt(num2)
            elif operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            elif operation == '**':
                result = num1 ** num2
            else:
                raise ValueError("Invalid operation.")

        except ValueError as ve:
            print(f"Error: {ve}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        else:
            print(f"Result: {result}")
            previous_results[(num1, num2, operation)] = result
        finally:
            print("This block is executed whether an exception occurred or not.\n")

    print("Previous results:")
    for inputs, result in previous_results.items():
        num1, num2, operation = inputs
        print(f"{num1} {operation} {num2} = {result}")

if __name__ == "__main__":
    calculator()
