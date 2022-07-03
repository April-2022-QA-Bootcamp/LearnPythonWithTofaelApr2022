# get accepted or denied return by using if twice, but not a good practice
age = 40
if age >= 18:
    print("Eligible for driving license")
if age < 18:
    print("Not Eligible for driving license")

# by using if else
age = 40
if age >= 18:
    print("Eligible for driving license")
else:
    print("Not Eligible for driving license")

# another example by using if else
num1 = 10
num2 = 15

if num1 >= num2:
    print(num1, 'is greater than or equal to', num2)
else:
    print(num1, 'is not greater than or equal to', num2)

# Even/Odd
num = int(input("Enter the number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# using input()
var1 = 34
print("please put a number:")
var2 = int(input())

if var2 > var1:
    print(var2, "is greater than", var1)
else:
    print(var2, "is smaller than", var1)

