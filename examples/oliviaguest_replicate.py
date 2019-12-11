'''Replicate results found at https://github.com/oliviaguest/gini.'''

import numpy as np
from pygini import gini

if __name__ == '__main__':

    A = np.zeros(1000)
    A[0] = 1

    GA = gini(A, eps=1e-7)
    assert GA == 0.99890010998900103

    RG = np.random.default_rng(1)
    S = RG.uniform(-1, 0, 1000)
    GS = gini(S, eps=1e-7)
    assert np.allclose(GS, 1/3, atol=1e-2)

    B = np.ones(1000)
    GB = gini(B, eps=1e-7)
    assert GB == 0
