
n = int(input("Enter the number of row : "))

for i in range(1, n+1):
    for j in range(i):
        print("*", end=' ')
        
    print()