class Employee:
    
    # constructor
    def __init__(self, name):
        # create and initialize class or instance attributes
        self.name = name
    
    def getName(self):
        print("The name of the employee is " + self.name)
   
# __init__ function can be used to define class or instance attributes and 
# assign values to them at the time of object creation 
e1 = Employee("Harry")
print(e1.name)
e1.getName()