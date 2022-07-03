# Incremental for loop
for a in range(1, 10, 2):
    print(a)

# Decremental for loop
print("\n---------------------------------")
for b in range(10, 1, -2):
    print(b)

print("\n------ Use of break in for loop ---------")
print("\nAfter use of break the output is below:")
for c in range(1, 20, 3):
    if c == 13:
        break
    print(c)

print("\nAfter use of break the output is below:")
for d in range(0, 20, 3):
    if d == 14:
        break
    print(d)

print("------Use of continue in for loop------")
print("\nAfter use of continue the output is below:")
# outcome: 1, 4, 7, 10, 13, 16, 19
# 4, 10 and 16 will be out
for x in range(1, 20, 3):
    if x % 2 == 0:
        continue
    print(x)

print("\n------continue---------")
# outcome: 1, 4, 7, 10, 13, 16, 19
for x in range(1, 20, 3):
    # print(x)
    if x % 2 == 1:  # skipping condition
        continue
    print(x)


















