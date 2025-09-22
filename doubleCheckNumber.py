

num = int(input("Enter  a number"))

if num > 50:
    print("the number is greater than 50")
    if num % 2 == 0:
        print(" and it is even too.")
        
    else:
        print("and the number is odd.")
        
else:
    print(" the number is smaller than 50")