total_bill = float(input("Enter toatl bill: "))
member_check = input("Are you a member? (yes/no): ")

if total_bill >= 1000 and member_check == "yes":
    discount = 0.1
elif total_bill >= 1000:
    discount = 0.05
else:
    discount = 0
