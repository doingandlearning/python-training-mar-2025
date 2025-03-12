data = [5, 2, 9, 1, 6, 8, 3, 7]

result = sorted(filter(lambda x: x % 2 == 0, data))
print(result)  # Output: [2, 6, 8]
