class Employee:
    # class attributes
    company = "Google"

e1 = Employee()
# defining instance attribute
e1.name = "Harry"
# accessing class attribute
print(e1.company)
# accessing instance attribute
print(e1.name)
# changing class attribute´s value
e1.company = "Youtube"
# accessing class attribute
print(e1.company)

e2 = Employee()
# print(e2.name)
    