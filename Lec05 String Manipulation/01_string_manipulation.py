# https://www.programiz.com/python-programming/methods/string/isdecimal
# https://pythonguides.com/
# https://www.knowprogram.com/python-program-examples/


print("\n.......................................................")
myName = "Subdermatoglyphic"
print(myName)
print(len(myName))  # length also include the space
# Why below one is true?
print(myName.isalnum())  # Return True if the string is an alphabetic or numeric string, False otherwise.
print(myName.isalpha(), "\n")  # Return True if the string is an alphabetic string, False otherwise

print("\n.......................................................")
str1 = "HelloWorld123"
str2 = "HelloWorld"
str3 = "123"
str4 = "Hello World 123"  # contain space which is a special character, that's why false
print(str1.isalnum())  # it means either alphabetical or numeric
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum(), "\n")  # why it is False? -- because contain spaces, which is regarded as special character

print("\n.......................................................")
txt1 = "Hello, And Welcome You All."
txt2 = "Hello, And WELCOME You All."
print(txt1.isupper())
print(txt1.islower())
print(txt1.istitle())
print(txt2.istitle())  # Return true if the String is a title-cased String, txt1

print("\n.......................................................")
str5 = "123"
print(str5.isalnum())
print(str5.isnumeric())
print(str5.isdecimal())  # https://docs.python.org/3.10/library/stdtypes.html#str.isdecimal
# A string is a decimal string if all characters in the string are decimal and there is at
# least one character in the string.
print(str5.isdigit())

print("\n.......................................................")
s = "28212"
print(s.isdecimal())
# contains alphabets
s = "32ladk3"
print(s.isdecimal())
# contains alphabets and spaces
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

print("\n.......................................................")
myName = "Subdermatoglyphic"
print(myName.startswith("sub"))
print(myName.startswith("Sub"))  # case sensitive
print(myName.endswith("phic"))
print(myName.endswith("PHIC"))  # case sensitive

print("\n.......................................................")
myName = "suBDErmATOglyphic is A woRdy, is bordy!"
print(
    myName.capitalize())  # Return More specifically, make the first character of the first word - upper case and the rest - lower case.
print(myName.upper())  # Return a copy of the string converted to uppercase.
# in Java, toUpperCase()
print(myName.lower())  # Return a copy of the string converted to lowercase.
# in Java, toLowerCase()
print(myName.title())  # Return a version of the string where each word is title-cased.
print(myName.casefold())  # Return a version of the string suitable for case-less comparisons. generally to lower
print(myName.swapcase())  # Convert uppercase characters to lowercase and lowercase characters to uppercase.
print(myName.count("y"))  # Return a copy of the string converted to uppercase.
# in Java, indexOf()
print(myName.count("is"))
print(myName.count("bordy"))
print(myName.find("Erm"))  # similar like indexOf() of Java
print(myName.find("erm"))
print("Erm" in myName)  # boolean
""" S.find(sub[, start[, end]]) -> int
Return the lowest index in S where substring sub is found, such that sub is contained within S[start:end].  
Optional arguments start and end are interpreted as in slice notation.
Return -1 on failure. """
print(myName.replace("phic", " many"))  # Return a copy with all occurrences of substring old replaced by new.
print(myName)  # because String is immutable

print("\n...................... Indexing .................................")
# Smiliar like charAt() of Java
# Strings are Arrays --> strings in Python are arrays of bytes representing unicode characters.
# In python there is no char type --> a single character of a string is a string with length of 1
# we can use [] and index in it to access element of the string
myName = "SuBdermatogclyphi"
print(myName[0])  # Value at index 0
print(myName[1])  # Value at index 1
print(myName[2])
print(myName[3])
print(myName[15])
# Negative Indexing --> negative indexes to start the position from the end of the string
print(myName[-1])  # Value at index [length -1]
print(myName[-2])  # Value at index [length -2]
print(myName[-3])

print("\n.......................... Slicing .............................")
# --> return a range of characters by using the slice syntax.
# for 'String slice', we use 'range operator'
myName = "Subdermatoglyphic"
print((myName[0:8]))
# 0 is initialized value and 16 is the upper limit which is excluded by formula. So, upper boundary excluded
# in Java, substring(0, 8)
print((myName[1:16]))
print((myName[2:16]))
print((myName[0:6]))
print((myName[4:11]))  # 4 is initialized value and 11 is the upper limit which is excluded by formula
print((myName[0:25]))  # 0 is initialized value and 25 is the upper limit which is excluded by formula,
# although the length is not 25
print((myName[6:25]))  # 6 is initialized value and 25 is the upper limit which is excluded by formula,
# although the length is not 25

print("\n.......................................................")
myName = "Subdermatoglyphic"
print(myName[0:13:2])
print(myName[::2])  # value present in index 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
print(myName[::6])  # value present in index 0, 6, 12, 18
print(myName[0:17:3])  # It behaves like, but not truly -->0 is initialized value, 17 is conditional value <17,
# 3 is incremental value, value present in index 0, 3, 6, 9, 12, 15
# exclude--> upper boundary excluded
print(myName[0:17:2])  # It behaves like, but not truly -->0 is initialized value, 17 is conditional value <17,
# 2 is incremental value, value present in index 0, 2, 4, 6, 8, 10, 12, 14, 16. Similar like print(myName[::2])
print(myName[17:0:-2])
print(myName[-1:0:-1])  # start from last index, >0, i--
print(myName[-1:0:-2])
print(myName[-5:0:-1])
# This is decremental value above
print(s[-8:-2])  # [-1] exclude-->upper boundary excluded
print("s[-8:-2] =", s[-8:-2])
print(s[-8::-2])  # [-1] exclude-->upper boundary excluded
print("s[-8:-2] =", s[-8::-2])
