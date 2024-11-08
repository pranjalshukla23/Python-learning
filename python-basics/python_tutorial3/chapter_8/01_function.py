def get_percentage(marks):
    return (sum(marks) / 400) * 100

percentage = get_percentage([45, 58, 76, 90])
print(percentage)

def add(num1, num2):
    return num1 + num2

result = add(4, 5)
print(result)

def greet (name): 
    print("Good morning " + name)
    
greet(input("Enter your name: "))