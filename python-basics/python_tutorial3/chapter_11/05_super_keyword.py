class Person:
    def __init__(self, name):
        self.name = name
    
    def getName(self):
        print("The name of employee is " + self.name)
        
class Employee(Person):
    def __init__(self,name, company):
        # invoking the constructor of parent class
        super().__init__(name)
        self.company = company
        
    def getCompany(self):
        print("The company is " + self.company)
        
e1 = Employee("Rohit", "Google")

e1.getName()
e1.getCompany()