# Parent class
class Person:
    def getCountry(self):
        print("Country is India")
 
# Child class 1       
class Employee(Person):
    def getCompany(self):
        print("Company is Google")
    
# Child class 2       
class Programmer(Employee):
    def getSalary(self):
        print("Salary is 1000")
        
p = Programmer()

p.getCountry()
p.getCompany()
p.getSalary()