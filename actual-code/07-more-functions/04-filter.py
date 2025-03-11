

def always_true(value):
    return True

def always_false(value):
    return False

def greater_than_10(value):
    return value > 10

data = [1,2,3,4,5,6,7,8,9,10, 11,12,13]
# [True, True, .... False, False]

print(list(filter(greater_than_10, data)))
print(list(filter(lambda num: num % 2 == 0, data)))
print(data)


