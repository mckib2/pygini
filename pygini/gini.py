'''Compute Gini index.

This implementation is inspired by the one found in [1]_.

References
----------
.. [1] https://github.com/oliviaguest/gini/blob/master/gini.py
'''

import numpy as np

def gini(arr, axis=None, eps=1e-8):
    '''Calculate the Gini coefficient of a numpy array.

    Parameters
    ----------
    arr : array_like
        Array to compute the Gini index of along axis.
    axis : None or int, optional
        If axis=None, arr is flattened before Gini index is computed.
        If axis is int, Gini index will be computed along the
        specified axis.
    eps : float, optional
        Small, positive number to make sure we don't divide by 0.

    Notes
    -----
    Based on bottom eq on [2]_.

    References
    ----------
    .. [2]_ http://www.statsdirect.com/help/
            default.htm#nonparametric_methods/gini.htm
    '''

    # Work out dimensions:
    if axis is None:
        arr = arr.flatten()
        axis = 0

    # All values are treated equally, arrays must be 1d and > 0:
    arr = np.abs(arr) + eps

    # Values must be sorted:
    arr = np.sort(arr, axis=axis)

    # Index per array element:
    idx = np.arange(1, arr.shape[axis] + 1)

    # Number of array elements:
    N = arr.shape[0]

    # Numerator
    sh = list(arr.shape)
    sh[axis] = 1
    for ax in range(len(sh)):
        if ax != axis:
            idx = np.expand_dims(idx, ax)
    numerator = np.sum(np.tile(2*idx - N - 1, sh)*arr, axis=axis)

    # Gini coefficient:
    return numerator/(N*np.sum(arr, axis=axis))
