#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fitsio
import dask.array as da
import numpy as np

class DaskAdapter(object):
    def __init__(self, hdu):
        self.hdu = hdu
        self.info = self.hdu.get_info()

    @property
    def shape(self):
        return tuple(self.info['dims'])

    @property
    def dtype(self):
        t = self.info['img_type']
        return {
            -32: np.float32,
            -64: np.float64,
        }[t]

    def __getitem__(self, item):
        return self.hdu[item]

# with fitsio.FITS('test.fits') as infile:
#     hdu = infile[0]
#     x = da.from_array(DaskAdapter(hdu), chunks=(10, 10))
#     print(x.mean(axis=1).compute())

