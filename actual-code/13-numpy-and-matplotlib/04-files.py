import numpy as np

# for consistent data with no missing elements
# data = np.loadtxt("data.csv", delimiter=",")

# If there are gaps in data - we can fill them in!
data = np.genfromtxt("data.csv", delimiter=",", filling_values=-1)

# np.savetxt("data-updated.csv", data * 2, delimiter=",", fmt="%.2f")

print(np.isnan(data))
data[np.isnan(data)] = 1  # replacing missing values
print(data)

mask = data == -1
# print(data[mask])
# data[mask] = 100
# print(data)
#
# mask = (data > 20) & (data < 50)
# # print(data[mask])
# data[mask] = 35
# print(data)

print(np.mean(data, axis=1))