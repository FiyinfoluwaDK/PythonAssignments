weight = float(input("Enter weight(kg): "))
height = float(input("Enter height(m): "))

bmi = weight/(height*height)

if bmi < 18.5:
    print("Underweight")
elif bmi <= 24.9:
    print("Normal")
elif bmi <= 29.9:
    print("Overweight")
else:
    print("Obese")
    
