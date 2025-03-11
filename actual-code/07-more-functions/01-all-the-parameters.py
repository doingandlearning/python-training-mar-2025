def add(a, b):
    return a + b


print(add(1,2))

def add(a, b, c=0):
    return a + b + c

print(add(1,2, 3))
print(add(1,2))


def add(name, *numbers):   # def add(arg1, arg2, *args, **kwargs):    # arbitrary arguments
    total = 0
    for number in numbers:
        total += number
    return f"{name} added up numbers to get {total}"


print(add("Ian", 1, 2, 3, 4))
print(add("Clement", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

def add(name, **numbers):
    total = sum(numbers.values())
    return f"{name} added some numbers and got {total}"

print(add("Anita", a=1, b=2, c=3, d=4))


def custom_sum(numbers, *args, **kwargs):
    total = sum(numbers, *args, **kwargs)
    return total


print(custom_sum((1,2,3,4,5), start=100))