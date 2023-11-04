name = input()
print("Welcome to my calculator",name,".")
message = int(input("How many numbers do you want to enter?"))
print("You entered an option for",message,"numbers.")
print("In my calculator you will be required to enter only 2 numbers.")
num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
sum = num1 + num2
print("The sum of the two numbers is:",sum)
print("Thankyou for using my calculator.")

print("Welcome Back to my calculator",name)
birth_year = int(input("Enter your year of birth:"))
current_year = int(input("Enter the current year:"))
current_age = current_year - birth_year
print("Your current age in years is:",current_age,"years.")
current_age_months = current_age * 12
print("Your current age in months is:",current_age_months,"months.")
current_age_days = current_age * 365
print("Your current age in days is:",current_age_days,"days.")