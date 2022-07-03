print("..................................")
age = 24
print(age)  # 24

print("..................................")
age += 2.4
"""
i++
i=i+1
i+=1
al 3 is same, we learn from Java
"""
print(age)  # 26.4

print("..................................")
age -= 2.2  # 26.4 -2.2
print(age)  # 24.2

print("..................................")
age *= 2
print(age)  # 48.4

print("..................................")
age /= 2
print(age)

print("..................................")
x = 10
print(x)
x = -x
print(x)

print("..................................")
x = 11
y = 2

result1 = x / y
print(result1)  # 5.5, in Java it is 5, because Java consider it as in type

result2 = x // y
print(result2)  # 5
"""
odd number: (i%2==1)
what is the modulus/remainder here: 1
"""
result3 = x % y
print(result3)  # 1

"""
The number 11 is called the numerator or dividend, 
and the number 2 is called the denominator or divisor.
The quotient is 5,
Remainder or modulus is 1
"""

# something new
# Use of Divmod
result = divmod(x, y)  # this is a method
print(result)  # outcome as quotient 5, remainder 1
print(result[0])  # behaving like an Array, who is the first position, represented by [0] indexing
print(result[1])

x = 2
result5 = x ** 3  # 2 to the power 3
print(result5)

# alternate of line 64, you can use pow()
result6 = pow(2, 4)  # power function, similar like line 64
print(result6)

# Whitespace
name = "          Tofael          "  # whitespace
print('_*_' + name + '_*_')
print('_*_' + name.lstrip() + '_*_')  # left strip remove white space from left side
print('_*_' + name.rstrip() + '_*_')
print('_*_' + name.strip() + '_*_')
print('_*_' + name.lstrip().rstrip() + '_*_')  # Method chaining - one method after another

# Print separator
x = "NY"
y = "MD"
z = "NJ"
print(x + ' | ' + y + ' | ' + z)
print(x, y, z, sep=' | ')  # another way use sep feature

# String interpolation
# old style, no need to know
# %s is for presenting String and %d is for placeholder --> numbers
person = '%s\'s age is %d'  # need to know more
print(person % ('Bill', 55))

# New style
person = '{name}\'s age is {age}'
print(person.format(name='Bob', age=45))
print(person.format(name='Brian', age=35))
print(person.format(name='Boby', age=35))
print(person.format(name='Briana', age=25))
# we can use a lot of data by this format

# Formatted String literal Python 3.6+
name = 'Michael'
age = 25
person = f'{name}\'s age is {age}'
print(person)
