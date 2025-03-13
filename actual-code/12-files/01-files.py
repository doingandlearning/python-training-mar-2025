try:
    file = open("file.txt")  # file handle!
except FileNotFoundError:
    print("Does the file exist?")

print(file.read())  # .read() -> grabs the whole file as a single string!

file.seek(0)  # moves the cursor to the top of the file
print(file.readlines())  # .readlines() -> grabs the whole file, makes a list with each line as an element

file.seek(0)
print(file.readline())  # .readline() -> gets the next line as a string
print(file.readline())

file.seek(0)

next_line = file.readline()

while next_line:
    print(next_line.upper())  # pretending to process a line!
    next_line = file.readline()  # get the next line

file.close()
