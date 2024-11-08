class Employee:
    @classmethod
    def getCompany(cls):
        print("The company is Google")
        
e = Employee()
Employee.getCompany()