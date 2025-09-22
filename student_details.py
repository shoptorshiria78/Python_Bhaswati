class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        
    def printname(self):
        print(self.fname, self.lname)
        
class Student(Person):
    
    def __init__(self, fname, lname, year):
        
        super().__init__(fname, lname)
        self.graduationyear = year
        
mina = Student("Mina", "Raju", 2007)

mina.printname()
print(mina.graduationyear)
        