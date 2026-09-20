x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))

if x > 0 and y > 0:
    print("Q1")
if x < 0 and y > 0:
    print("Q2")
if x < 0 and y < 0:
    print("Q3")
if x > 0 and y < 0:
    print("Q4")
if x == 0 and y == 0:
    print("Origin")
if x == 0 and y != 0:
    print("Y-axis")
if x != 0 and y == 0:
    print("X-axis")
    
