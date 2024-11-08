# Parent class 1
class Employee:
    def getCompanyName(self):
        print("Company is Fiverr")
        
# Parent class 2
class Freelancer:
    def getSalary(self):
        print("Salary is 1000")

# Child class      
class Programmer(Employee, Freelancer):
    def getName(self):
        print("Name is Rohit")
        
p = Programmer()
p.getCompanyName()
p.getSalary()
p.getName()
