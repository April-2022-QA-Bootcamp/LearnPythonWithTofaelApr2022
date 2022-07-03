# if else condition (not Ternary operator)
# if use else, no condition required
num1 = 20
num2 = 30
if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 == num2:
    print(num1, "is equal to", num2)
elif num1 < num2:
    print(num1, "is less than", num2)

# Alternate way below
# Called Ternary operator -- Ternary means 3
print(num1 if num1 > num2 else num2)
