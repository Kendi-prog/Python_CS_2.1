print("***Welcome Dear User.***")
print("***This is a Tip Calculator.***")
total = int(input("Enter the total bill amount:"))
tip = total * (12/100)
print("The tip amount is:",tip)
number_of_users = int(input("Enter the number of people splitting the bill:"))
overall_amount = total + tip
sharing_amount = overall_amount / number_of_users 
rounded_number = round(sharing_amount,2)
print("Amount payabale by each person is:",rounded_number)
print("Thankyou for using the Tip Calculator.")

