# Regular way, logical and operator, both condition should be true, then outcome is true
num = 4
if num >= 3 and num < 5:
    print(num, 'follow the conditions')

# how to use chained comparison (new here)
if 3 <= num < 5:
    print(num, 'following the conditions')

# How to ignore cases
name1 = 'Mohammad'
name2 = 'mohammad'

if name1.lower() == name2.lower():
    print("\nSame name by converting both to lower case")

if name1.upper() == name2.upper():
    print("\nSame name by converting both to upper case")

if name1 != 'Sharkar':
    print(name1, "is not equal to Sharkar")

if name1 == 'Mohammad':
    print(name1, "is equal to Mohammad")

if name1 != 'Mohammad':  # Not printing anything
    print(name1, "is not equal to Mohammad")
