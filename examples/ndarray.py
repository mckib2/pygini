'''Compute gini index along axis of n-dimensional array.'''

import numpy as np

from pygini import gini

if __name__ == '__main__':

    RG = np.random.default_rng(0)
    N = 100
    A = RG.random((N, N-20, N-20))

    # Compare results:
    G0 = np.apply_along_axis(gini, axis=0, arr=A)
    G = gini(A, axis=0)
    assert np.allclose(G0, G), 'pygini is not working correctly!'
