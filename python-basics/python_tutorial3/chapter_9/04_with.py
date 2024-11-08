with open("chapter_9\\sample.txt", "r") as f:
    data = f.read()
    print(data)
    
with open("chapter_9\\text.txt", "w") as f:
    data = f.write("Please write this to the file")
    print(data)