import numpy as np

# list  -  array
number_list = [1,2,3,4]  # throw in whatever you want!

arr = np.array([1, 2, 3, 4])  # all of my values are of the same type
print(number_list)
print(arr)
print(type(arr))

python_range = [number for number in range(0, 10, 2)]
print(python_range)
arr = np.arange(0, 10, 2)
print(arr)

arr = np.linspace(0, 10, 21)
print(arr)

arr = np.arange(1,10)
reshaped = arr.copy().reshape(3,3)

reshaped[0][0] = 12
print(arr)
print(reshaped)  # view

arr = np.array([10,20,30,40,50])
print(arr[1])
print(arr[1:3])
print(arr[-2:])


