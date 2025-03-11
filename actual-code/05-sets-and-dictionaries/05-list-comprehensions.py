values = [2, 3, 4, 5, 6]

squared_values = []
for value in values:
    square = value ** 2
    if square % 2 == 0:
        squared_values.append(square)


print(squared_values)

squared_values = [value ** 2 for value in values if value % 2 == 0]  # Pythonic??

# Clever solutions to problems ...
print(squared_values)



