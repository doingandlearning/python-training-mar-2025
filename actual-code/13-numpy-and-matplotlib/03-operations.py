import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([10,20,30,40,50])

print(arr1 + arr2)
print(arr1 * arr2)

list1 = [1,2,3,4,5]
list2 = [10,20,30,40,50]

result = []
for index in range(5):
    result.append(list1[index] * list2[index])
print(result)

# Broadcasting

print(arr1 + 10)
print(arr1 * 2)
print(arr1 ** 2)