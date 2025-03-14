import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
x = np.random.rand(500) * 10   # 50 random 0 - 10
y = np.random.rand(500) * 100  # 50 random 0 - 100

plt.scatter(x, y,
            color="blue",
            marker="o", # o or x
            alpha=0.4, # 1 - opaque, 0 - transparent
            label="Data points",
            s=200  # size of the marker
             )

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot Example")

plt.legend()


plt.show()