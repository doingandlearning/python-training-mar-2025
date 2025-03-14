import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 101)
y = np.sin(x)

plt.plot(
    x,
         y,
         label="Sine Wave",
         color="darkmagenta",
         linestyle=":", # -, --, :
         linewidth=5
)

plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Sine Wave Plot")
plt.grid()

plt.legend()



plt.show()