pygini
======

Very simple module that computes the Gini index of a numpy array.

Installation
============

.. code-block:: bash

    pip install pygini

Usage
=====

.. code-block:: python

    import numpy as np
    from pygini import gini

    RG = np.random.default_rng(0)
    A = RG.random(100)
    GI = gini(A)

    # Also compute along axis
    A = RG.random((100, 80, 80))
    GI = gini(A, axis=0)

    # GI.shape = (80, 80)

See `examples` directory.
