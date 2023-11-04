name  = input("Enter name:")
print("Welcome to my BMI Calculator",name,".")
print("You will be required to enter some details to know your BMI weight status.")
weight = float(input("Enter weight in kgs :"))
height = float(input("Enter height in m :"))
BMI = weight / (height*height)
rounded_number = round(BMI,2)
print(name,"Your BMI weight is :",rounded_number)

if BMI < 18:
    print("You are Underweight",name,"!")
elif BMI > 24.9:
    print("You are Overweight",name,"!")
else:
    print("You have a Normal Weight",name,"!")
print("Thankyou for using my BMI calculator.")