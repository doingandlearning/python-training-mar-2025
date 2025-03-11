empty_list = []  # list()

numbers_list = [1, 1, 2, 3, 5, 8, 13]

for number in numbers_list:
    print(number)

beatles_list = ["John", "Paul", "George", "Ringo", "John"]

beatles_list.append("Fabian")  # add a single new element
beatles_list.extend(["Clement", "Serge"])  # add multiple new elements
print(beatles_list)
print(type(beatles_list))
print(len(beatles_list))
print(beatles_list.count("John"))
print(beatles_list.count("Kevin"))

if "Clement" in beatles_list:
    print(beatles_list.index("Clement"))

beatles_list.remove("John")
beatles_list.sort()
print(beatles_list)

name = beatles_list.pop()   # LIFO
print(name)
print(beatles_list)

print(beatles_list[0])
print(beatles_list[3:])
print(beatles_list[::-1])

while "John" in beatles_list:
    beatles_list.remove("John")

print(beatles_list)

number_list = [1, 2, 3, 4]
number_list_2 = number_list.copy()


number_list_2.append(5)
print(number_list_2)
print(number_list)
