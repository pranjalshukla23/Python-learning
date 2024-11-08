# use open function to read the content of a file
f = open("chapter_9\\sample.txt", "r")
# read the content of file
#data = f.read()
# read first 5 characters of the file
data = f.read(5)
print(data)
# close the file
f.close()