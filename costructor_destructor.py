class Employee:
    
    def __init__(self):
        print("Employee created")
        
    def __del__(self):
        print("Desturctor called, employee deleted")
    
    
Raju = Employee()
del Raju
         