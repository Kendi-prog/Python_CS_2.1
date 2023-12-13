#SCT211-0091/2022
def sum_calculator():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 + num2
        print("The sum of", num1, "and", num2, "is:", result)
    
    except ValueError:
        print("Invalid input. Please enter numeric values.")

sum_calculator()