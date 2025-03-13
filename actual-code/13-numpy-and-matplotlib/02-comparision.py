import time
import numpy as np

size = 10 ** 7

py_list = list(range(size))
start = time.time()
sum(py_list)
print(f"Python list sum time: {time.time() - start}")

np_arr = np.arange(size)
start = time.time()
np.sum(np_arr)
print(f"Numpy array sum time: {time.time() - start}")