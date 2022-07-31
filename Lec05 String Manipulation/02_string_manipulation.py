s = "My name is Alex I live at woodside, NY, USA. My neighbourhood is really very convenient to live at."
print(s)

print("------------ How to print multi-line string ------------")
# use '''-----'''  or """------""" line will be printed as given in code
s = '''My name is Alex. 
I live at Woodside, NY, USA.
My neighbourhood is really very convenient to live at.'''
print(s)

print("----------- strip() functions ---------------")
# strip() method removes any leading and trailing whitespace
s1 = "     My Name is Alex     Ferguson     "
print(s1)
print(s1.strip())  # similar like Java trim()

print("\n----- Use of lstrip(), rstrip() & strip() -----")
# lstrip() --> Returns a left trim version of the string
# rstrip() --> Returns a right trim version of the string
txt = "     My Name is Alex     "
x = txt.lstrip()  # --> Remove spaces from the left side of the string
print("Among all", x, "is the best")
y = txt.rstrip()  # --> Remove spaces from the right side of the string
print("Among all", y, "is the best")
z = txt.strip()  # -->Remove spaces from left & right of the string
print("Among all", z, "is the best")

print("\n------------------------------------")
# replace() method replaces a string with another string
m = "My NAme Is Alex Ferguson"
print(m.replace("A", "C"))  # will replace all A to C. Case sensitive
print(m.replace("a", "C"))  # will replace all A to C. Case sensitive

print("\n------------------------------------")
txt = "My Name Is Alex Ferguson 41"
print("Alex" in txt) #boolean
# in Java, contains()
print("Blex" in txt)
print("Dlex" not in txt)

# split() method splits the string into substrings if it finds instances of the separator
x = txt.split(" ")
print(x)  # so now strings are going to split
print(x[3])