data = [1,2,3,4,5,6,7,8,9,10, 11,12,13]

#  x -> y

def cubic_transformation(x):
    return x**3 + 1 - 1 * x ** 2

squares = map(lambda x: x**3 + 1 - 1 * x ** 2, data)  # prototyping, one-off functions, throw-away
squares = map(cubic_transformation, data)
# print(list(squares))
for square in squares:
    print(square)