def summary(a: float | int, b: float | int):
    """
    A function which adds two numbers
    :param a: First number
    :param b: Second number
    :return: The sum of the two numbers
    """
    # a = 10
    return a + b, a - b, (a + b) / 2


total, difference, mean = summary(5, 8)

print(type(total))
print(difference)
print(mean)

def cube(number):
    return number ** 3

if cube(4) < 100:
    print("This is quite a small number still.")

numbers = [1,2,3,4,5]
cube_numbers = [cube(number) for number in numbers]
print(cube_numbers)

print(f"19 cubed is {cube(19)}")  # Functions are first class
