# -*- coding: utf-8 -*-

'''
`daskfitsio`

Module to wrap a fits hdu in a dask array to enable out of core
parallel computation
'''

import dask.array as da
import numpy as np

class DaskAdapter(object):
    '''
    Adapter object, which wraps a `fitsio.ImageHDU` object
    '''
    def __init__(self, hdu):
        self.hdu = hdu
        self.info = self.hdu.get_info()

    @property
    def shape(self):
        return tuple(self.info['dims'])

    @property
    def dtype(self):
        t = self.info['img_type']
        try:
            return {
                8: np.int8,
                16: np.int16,
                32: np.int32,
                -32: np.float32,
                -64: np.float64,
            }[t]
        except KeyError:
            err_msg = 'Unsupported data type: {}. Please open a new issue: https://github.com/mindriot101/daskfitsio/issues/new'.format(t)
            raise ValueError(err_msg)

    def __getitem__(self, item):
        return self.hdu[item]


def read_hdu(hdu, chunks):
    '''
    High level interface to access hdu data

    >>> with fitsio.FITS(fname) as infile:
    ...     hdu = infile[0]
    ...     data = df.read_hdu(hdu, chunks=(10, 10))
    ...     print(data.mean(axis=1).compute())
    ...
    '''
    return da.from_array(DaskAdapter(hdu), chunks=chunks)
