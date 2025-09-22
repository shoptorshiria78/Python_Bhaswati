class Person(object):
    
    def __init__(self, name, idname):
        self.name = name
        self.idname = idname
        
    def display(self):
        print(self.name)
        print(self.idname)
        
class Employee(Person):
    
    def __init__(self, name, idname, salary, post):
        
        self.salary = salary
        self.post = post
        Person.__init__(self, name, idname)
        
        
aloo = Employee("Aloo", 2352352, 25000, "asistant")

aloo.display()
print(aloo.post)
print(aloo.salary)