age = int(input("Enter age: "))

if age < 5:
    price = "Free"
elif age <=12:
    price = "$5"
elif age <=64:
    price = "$12"
else:
    price = "$8"
    
print(price)
