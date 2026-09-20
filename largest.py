number_one = int(input("Enter first number: "))
number_two = int(input("Enter second number: "))
number_three = int(input("Enter third number: "))

largest = number_one

if number_two > largest:
    largest = number_two
    
if number_three > largest:
    largest = number_three
    
print(largest)
