with open("coding.txt", 'w') as file:
    file.write("Hi, this is penguin , I am 1 years old. I like to play football. \n  I also love traveling a lot.")
file.close()

with open("coding.txt", 'r') as file:
    
    data = file.readlines()
    
    for line in data:
        word = line.split()
        print(word)
        
file.close()