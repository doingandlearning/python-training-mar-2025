import numpy as np
import matplotlib.pyplot as plt

data = np.round(
    np.random.normal(loc=50, scale=15, size=1000), # loc => mean, scale => sd
    3)
plt.hist(data, bins=50, color="blue", edgecolor="red", alpha=0.7)

data = np.round(
    np.random.normal(loc=50, scale=15, size=1000), # loc => mean, scale => sd
    3)
plt.hist(data, bins=50, color="orange", edgecolor="black", alpha=0.7)



plt.show()



