'''Compute Gini index.

This implementation is inspired by the one found in [1]_.  This
implementation handles multidimensional arrays.

References
----------
.. [1] https://github.com/oliviaguest/gini/blob/master/gini.py
'''

import numpy as np

def gini(data, axis=None, eps=1e-8):
    '''Calculate the Gini coefficient of a numpy array.

    Parameters
    ----------
    data : array_like
        Array to compute the Gini index of along axis.
    axis : None or int, optional
        If axis=None, data is flattened before Gini index is computed.
        If axis is int, Gini index will be computed along the
        specified axis.
    eps : float, optional
        Small, positive number to make sure we don't divide by 0.

    Returns
    -------
    res : array_like
        The Gini coefficients of numpy array data.

    Notes
    -----
    Based on bottom eq on [2]_.

    References
    ----------
    .. [2]_ http://www.statsdirect.com/help/
            default.htm#nonparametric_methods/gini.htm
    '''

    # Work out dimensions
    if axis is None:
        data = data.flatten()
        N = data.shape[0]
        idx = np.arange(N) + 1 # 1-based indexing
    else:
        # Move gini index axis up front
        data = np.moveaxis(data, axis, 0)

        # Reshape so we only have two axes to deal with:
        N, sh_orig = data.shape[0], data.shape[1:]
        data = np.reshape(data, (N, -1))
        idx = np.arange(N)[:, None] + 1

    # Values cannot be negative
    minval = np.amin(data.flatten())
    if minval < 0:
        data -= minval

    # Values must be nonzero
    data += eps

    # Values must be sorted
    data = np.sort(data, axis=0)

    # Calculate Gini coefficient
    num = np.sum((2*idx - N - 1)*data, axis=0)
    den = N*np.sum(data, axis=0)
    res = num/den
    if axis is None:
        return res
    return np.reshape(res, sh_orig)
