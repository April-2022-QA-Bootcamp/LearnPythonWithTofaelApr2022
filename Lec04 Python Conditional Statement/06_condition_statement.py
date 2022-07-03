# 1 Nested if
marks = int(input("Enter the marks here: "))
if marks >= 40:
    if marks >= 80:
        print("distinct")
    elif marks >= 75:
        print("Excellent")
    else:
        print("pass")
else:
    print("Fail")

# 4

num1 = int(input("Enter the num1: "))
num2 = int(input("Enter the num2: "))

if num1 > num2:
    if num1 % 2 == 0:
        print(num1, "is an even number and greater than", num2)
    elif num1 % 2 == 1:
        print(num1, "is an odd number and greater than", num2)
elif num1 < num2:
    if num1 % 2 == 0:
        print(num1, "is an even number and less than", num2)
    elif num1 % 2 == 1:
        print(num1, "is an odd number and less than", num2)
else:
    print(num1, "is equal to", num2)
