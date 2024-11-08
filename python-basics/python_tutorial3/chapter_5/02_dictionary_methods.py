myDict = {
    "fast": "In a quick manner",
    "harry": "A coder",
    "marks": [20, 50, 70],
    "anotherDict": {"Harry": "Player"}
}

print(myDict.keys())
print(myDict.values())
print(myDict.items())
print(list(myDict.items()))

myDict.update({"marks": [20, 50, 100]})
print(myDict)

print(myDict.get("harry"))
print(myDict.get("Harry2"))
#
# print(myDict["Harry2"])