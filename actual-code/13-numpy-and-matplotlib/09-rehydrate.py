import pickle
import numpy as np
import matplotlib.pyplot as plt

with open("saved_figure.pkl", "rb") as file:
    loaded_fig = pickle.load(file)

print(loaded_fig)
loaded_fig.show()  #