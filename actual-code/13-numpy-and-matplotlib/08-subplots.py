import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2,2, figsize=(10, 8))


# Line Plot
x = np.linspace(0, 10, 101)
y = np.sin(x)

axs[0][0].plot(x, y, color="blue")
axs[0][0].set_title("Sine Wave")
axs[0][0].set_xlim(3.0, 6.0)
axs[0][0].set_ylim(-1.1, -0.4)

x = np.random.rand(500) * 10   # 50 random 0 - 10
y = np.random.rand(500) * 100  # 50 random 0 - 100

axs[0][1].scatter(x, y,
            color="blue",
            marker="o", # o or x
            alpha=0.4, # 1 - opaque, 0 - transparent
            label="Data points",
            s=200  # size of the marker
             )

data = np.round(
    np.random.normal(loc=50, scale=15, size=1000), # loc => mean, scale => sd
    3)
axs[1][0].hist(data, bins=50, color="blue", edgecolor="black", alpha=0.7)

# Line Plot
x = np.linspace(0, 10, 101)
y1 = np.cos(x)
y = np.sin(x)
axs[1][1].plot(x, y1, color="blue")
axs[1][1].plot(x, y, color="red")
axs[1][1].set_title("Cosine and Sine Wave")
axs[1][1].grid(True)



# plt.show()
# plt.savefig("subplots.png", dpi=300)

import pickle
with open("saved_figure.pkl", "wb") as file:
    pickle.dump(fig, file)