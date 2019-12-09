'''Compute Gini index of random array.'''

import numpy as np
from pygini import gini

if __name__ == '__main__':

    # Random array 1D array
    RG = np.random.default_rng(0)
    A = RG.random(100)
    GI = gini(A)
    print(GI)
