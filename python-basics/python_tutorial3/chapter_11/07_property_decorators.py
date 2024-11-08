class Employee:
    salary = 5000
    bonus = 1000
    
    @property
    def totalSalary(self):
        return self.salary + self.bonus
        
e = Employee()
print(e.totalSalary)