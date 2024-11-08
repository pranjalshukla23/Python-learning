name = input("Enter your name: ")

print(name + " Good Afternoon")

letter = '''Dear <Name> you are selected <Date>'''

letter = letter.replace("<Name>", "Harry")
letter = letter.replace("<Date>", "27/10/2024")

print(letter)

st = "This is a string with double  spaces"

print(st.find("  "))
print(st.replace("  ", ""))

letter = "Dear Harry, this python course is nice. Thanks!"

new_letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"

print(new_letter)