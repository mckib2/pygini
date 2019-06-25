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

    A = np.random.random(100)
    GI = gini(A)

See `examples` directory.
