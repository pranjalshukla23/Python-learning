fruit1 = input("Enter first fruit: ")
fruit2 = input("Enter second fruit: ")
fruit3 = input("Enter third fruit: ")
fruit4 = input("Enter forth fruit: ")
fruit5 = input("Enter fifth fruit: ")
fruit6 = input("Enter sixth fruit: ")

fruits_list = [fruit1, fruit2, fruit3, fruit4, fruit5, fruit6]


print(fruits_list)

m1 = int(input("Enter marks for student 1: "))
m2 = int(input("Enter marks for student 2: "))
m3 = int(input("Enter marks for student 3: "))
m4 = int(input("Enter marks for student 4: "))
m5 = int(input("Enter marks for student 5: "))
m6 = int(input("Enter marks for student 6: "))

marks_list = [m1, m2, m3, m4, m5, m6]

marks_list.sort()
print(marks_list)
print(sum(marks_list))

tup2 = (2, 7, 0, 3, 0)

print(tup2.count(0))


