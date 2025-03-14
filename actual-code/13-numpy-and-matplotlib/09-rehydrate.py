import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("saved_figure.pkl", "rb") as file:
    loaded_fig = pickle.load(file)

print(loaded_fig)

# Apparently this works in some environments
# loaded_fig.show()

# This is what I had to do to show the figure again.
plt.figure(loaded_fig.number)
plt.show() 