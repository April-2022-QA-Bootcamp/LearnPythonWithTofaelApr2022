# (initialization block, conditional block, increment/decremental block), we use coma, in java we used ;
# Incremental for loop
print("----- Use of for Loop 01 -----\n")
for a in range(0, 10, 1):
    print(a)
print("----- Use of for Loop 02 -----\n")
for b in range(1, 10, 2):
    print(b)

# Decremental for loop
for c in range(10, 1, -2):
    print(c)

print("----- Use of for Loop 04 -----\n")
# calculate the total of all even numbers from 0-10
total1 = 0
for d in range(0, 10, 2):
    total1 = total1+d
print("Sum of all even numbers:", total1, "\n")

# sum of numbers
n = int(input("Enter the range of the loop: "))
total2 = 0
for e in range(0, n, 1):
    total2 = total2 + e
print("sum of all even and odd numbers:", total2)