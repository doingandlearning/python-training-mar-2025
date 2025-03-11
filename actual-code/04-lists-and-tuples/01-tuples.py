empty_tuple = ()  # or tuple()

print(empty_tuple)
print(type(empty_tuple))

print(empty_tuple.count("a"))
# print(empty_tuple.index("a"))
# Double Underscore __something__  - Dunder Method
#               0  1  2  3
number_tuple = (1, 3, 5, 7)
print(number_tuple[1])
print(number_tuple[2:])
print(number_tuple[1:3])
print(number_tuple[0:2:2])

print(3 in number_tuple)
print(19 in number_tuple)

test_value = 3
if test_value in number_tuple:
    print(f"{test_value} is at index {number_tuple.index(test_value)}")
else:
    print(f"{test_value} not in tuple")

for number in number_tuple:
    print(number)
    print(type(number))

mixed_tuple = (True, 0.2, "Hello", 10)

multi_tuple = ((1,2), (3,4))

print(multi_tuple[0][1])


lots_of_ones = (1,1,1,1,1,1)
print(lots_of_ones.count(1))
print(lots_of_ones.index(1))
print(lots_of_ones[1:].index(1) + 1)
