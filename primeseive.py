def seiveOfEratosthenes(num):
    
    prime = [True for i in range(num+1)]
    
    p = 2
    
    while p * p <= num:
        
        if (prime[p] == True):
            
            for i in range(p*p, num+1, p):
                
                prime[i] = False
                
        p+=1
        
    for i in range(2, num+1):
        
        if(prime[i]):
            print(i)
            

number = int(input("Enter the number."))

seiveOfEratosthenes(number)