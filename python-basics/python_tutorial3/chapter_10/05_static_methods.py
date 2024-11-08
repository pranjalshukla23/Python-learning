class Employee:
    def getData(self):
        print(self)
        # self will help to access class and instance attributes
        print(self.salary)
        
    @staticmethod
    def greet():
        print("Good morning Sir")
        
e1 = Employee()
e1.salary = 1000
# here self is passed as e1 automatically
e1.getData()
# no self is passed
e1.greet()