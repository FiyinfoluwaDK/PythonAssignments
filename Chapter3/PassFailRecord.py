passed = 0
failed = 0
count = 0

while count < 10:
    result = int(input("Enter result (1 = success/ 2 = failed): "))
    
    if result == 1:
        passed += 1
        print("Passed")
        count += 1
    elif result == 2:
        failed += 1
        print("Failed")
        count += 1
    else:
        print("Invalid input")

print(f"Number of students passed: {passed}; Number of students failed: {failed}")
