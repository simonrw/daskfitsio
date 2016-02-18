==========
daskfitsio
==========

.. image:: https://travis-ci.org/mindriot101/daskfitsio.svg?branch=master
    :target: https://travis-ci.org/mindriot101/daskfitsio

Wrapper around ``fitsio.ImageHDU`` creating a ``dask.Array``.

Quickstart
----------

.. code-block:: python

    >>> with fitsio.FITS(fname) as infile:
    ...     hdu = infile[0]
    ...     data = df.read_hdu(hdu, chunks=(10, 10))
    ...     print(data.mean(axis=1).compute())
    ...
