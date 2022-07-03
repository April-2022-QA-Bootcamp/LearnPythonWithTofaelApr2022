print("\n----- define variables in a single line -----")
a = 12
b = 13
c = 24
# Generally we write like above

a, b, c = 10, 20, 30  # multiple variable assigned in one line is new here
print("a =", a)  # 10
print("b =", b)  # 20
print("c =", c)  # 30

print("\n----- same value many variables -----")
x = y = "Hello"
print("x =", x)  # Hello
print("y =", y)  # Hello

print("\n----- Use of global and local variable -----")
name1 = "I am outside of function/method --> I am a global variable"
print(name1)


def var():
    name2 = "I am inside of a function --> I am a local variable"
    print(name2)
    # Expected an indented block after function definition
    # don't forget indentation


var()
# to format: Alt + Shift + Enter

print("\n----- global & local variable has same variable name -----")
age = 40
print("global variable age:", age)


def varAge():
    age = 60
    myAge = 50
    print("local variable myAge:", myAge)
    print("local variable age is same as like global:", age)


varAge()
print("still global variable age value that means no impact if changed in function that means that is not same :", age)
print("\n----- uses of local and global variable-----")
id1 = 101  # global variable


# Can a global variable called inside a local variable? Yes, see line 53
def varId():
    id2 = 102  # local variable
    print("Global id can be called, inside the function", id1)
    print("Local id can be called, inside the function as usual", id2)


varId()
print("global id is called out side of the function:", id1)
print("here, local id is called out side of the function:",
      "sorry first make id2 global, not possible to call outside of the function")

# local variable can't be call outside the function

print("\n----- How can we turn a global variable to local variable from the function 01 -----")
city = "NY"


def varCity():
    global city  # Called the global variable inside the function and turned it to local variable
    city = "woodside"  # local variable
    print("Local variable is called from inside the function: ", city)


varCity()
print("calling the global variable outside the function after using global keyword inside the function : ", city)

print("\n----- How can we turn a global variable to local variable from the function 02 -----")
phone = 3474005813
print("Global variable is called-before change in function : ", phone)


def varPhone():
  #  global phone
    cell = 55555
    phone = 4648876482
    print("Local variable is called from inside the function: ", phone)


varPhone()
# print("calling local variable outside the function:",cell) #not possible
print("Global variable is called from outside the function after changing global in funciotn: ", phone)
