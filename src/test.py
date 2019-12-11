import numpy as np
from pygini import gini

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]).astype(float)

print(gini(arr, eps=0))
