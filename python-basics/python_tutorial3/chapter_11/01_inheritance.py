# Parent class
class Employee:
    def showDetails(self):
        print("This is an employee")

# Child or derived class    
class Programmer(Employee):
    def getName(self):
        print("The language is python")
        
    # method overriding
    # def showDetails(self):
        #print("This is a person")
 
# object instantiation       
e = Employee()
p = Programmer()

# invoking methods 
p.showDetails()
p.getName()

        
