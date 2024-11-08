# class 
class RailwayForm:
    # class variable
    formType = "Railway Form"
    
    # method
    def printData(self):
        print(self.formType)

# object
harryApplication = RailwayForm()

# invoking class method
harryApplication.printData()