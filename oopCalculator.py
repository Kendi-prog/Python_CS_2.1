class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        self.result = num1 + num2

    def get_result(self):
        return self.result


# Create an instance of the Calculator class
calculator = Calculator()

# Perform addition using the calculator object
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
calculator.add(num1, num2)

# Get and display the result
result = calculator.get_result()
print("The sum of", num1, "and", num2, "is:", result)