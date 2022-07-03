import datetime

print(datetime.datetime.now())  # it will give you current time

print("\n-------------------------------------------------")
print("# 1 (String type 01, Presented by single or double quotation)\n")
name1 = "Mohammad"
print("My First name: " + name1)  # use of +
print(type(name1))

name2 = 'Tofael'
print("Middle Name:", name2)  # use of ,
print(type(name2))
print("Middle Name:", name2, type(name2))  # we can also present it together, separated by coma

name3 = 'Kabir'
print(name3)
print(type(name3))

print("\n-------------------------------------------------")
print(name1 + " " + name2 + " " + name3)   # without empty String this line can't produce space
print(name1, name2, name3)  # below one is mostly used in python

print(name1, end=" ")  # use of end feature for variable
print(name2, name3)
print("\n")

print("# 2 (String type 02, The way we will use)\n")
name = "Tofael"
print("My Name is:" + name)  # don't give a space, see below line
print("My Name is:", name)
print("Type of my Name is:", type(name))
print("\n")

print("# 3 (int type)\n")
age = 87
print("My age is: ", age)
print("Type of my age is:", type(age))
print("\n")

print("# 4 (floating type)\n")
grade = 3.9987
print("My grade is: ", grade)
print("Type of my grade is:", type(grade))
print("\n")

print("# 5 (boolean type 01)\n")
print("When we use true/false, the type is: ", type(True))  # in Java, it is in lower case, but in python in upper case
print("\n")

print("# 5 (boolean type 02)\n")
print("When we use true/false, the type is: ", type(False))
print("\n")

print("# 6 (boolean type 03)\n")
country1 = "USA"
country2 = "BD"
print("Is Country 1 and Country2 is same?", country1 == country2)  # == Equality operator
print("Type is:", type(country1 == country2))
print("\n")

print("# 7 (Combining few variables)\n")
print(name, age, grade)
print("My Name:", name, "Age:", age, "grade:", grade)  # you can use coma for different variable to concat
# what is the mistake in below line? we can solve it by casting, see next file
# you can't use + symbol for different variable type to concat, remove # to test
# print("My Name: " + name + ",Age: " + age + ",grade: " + grade)
# There is a solution, but please see next file to understand it
print("My Name: " + name + ", Age: " + str(age) + ", grade: " + str(grade))

