def recurse_num(n):
    
    if n == 1:
        return n
    else:
        return n * recurse_num(n-1)
    
num = int(input("Enter positive integer number"))

if num < 0:
    print("Negative number can not have factorial")
    
elif num == 0:
    print("factorial of 0 is 1")
    
else:
    print("the factorial of ", num , " is ", recurse_num(num) )