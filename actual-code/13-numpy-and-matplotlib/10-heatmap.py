import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(6,6)  # you're going looking at real data!

row_labels = ["A", "B", "C", "D", "E", "F"]
col_labels = ["U", "V", "W", "X", "Y", "Z"]

plt.imshow(data,
           cmap="inferno",  # viridis, coolwarm, gray, inferno
           interpolation="bicubic"  # nearest, bilinear, bicubic
           )
plt.colorbar(label="Intensity")
plt.title("Heatmap of Random Data")
plt.xticks(ticks=np.arange(6), labels=col_labels)
plt.yticks(ticks=np.arange(6), labels=row_labels)
plt.show()