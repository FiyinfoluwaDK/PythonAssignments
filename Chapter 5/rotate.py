def rotate(first, second, third):
    return third, first, second


hobby_one = "Coding"
hobby_two = "Drawing"
hobby_three = "gaming"

for call in range(3):
    hobby_one, hobby_two, hobby_three = rotate(hobby_one, hobby_two, hobby_three)
    print(hobby_one, hobby_two, hobby_three)
