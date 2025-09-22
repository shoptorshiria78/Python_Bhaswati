class Parrot:
    
    species = "bird"
    
    def __init__(self, name, age):
        
        self.name = name
        self.age = age
        
        
kewkew = Parrot("Kewkew", 5)
blue = Parrot("Blue", 10)

print(" Blue is a {}".format(blue.species))
print("Kewkew is also {}".format(kewkew.species))


print("{} is a beautiful bird".format(kewkew.name))
print("Blue is {} years old".format(blue.age))
       