'''Compute gini index along axis of n-dimensional array.'''

import numpy as np

from pygini import gini

if __name__ == '__main__':

    RG = np.random.default_rng(0)
    N = 100
    A = RG.random((N, N-20, N-20))

    # Control: manually along 0th axis
    G0 = np.zeros(A.shape[1:])
    for ii in range(A.shape[1]):
        for jj in range(A.shape[2]):
            G0[ii, jj] = gini(A[:, ii, jj])

    # Compute Gini along 0th axis
    G = gini(A, axis=0)

    # Sanity check:
    assert np.allclose(G0, G), 'pygini is not working correctly!'
