def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def Multiply(x,y):
    return x*y

def Divide(x,y):
    return x/y

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("Sum", add(num1, num2))
print("Subtract", subtract(num1, num2))
print("Product", Multiply(num1, num2))
print("Quotient", Divide(num1, num2))