import pytest
import numpy as np
import fitsio
from .context import daskfitsio as df

@pytest.fixture
def da(fitsfile):
    with fitsio.FITS(fitsfile) as infile:
        return df.DaskAdapter(infile[0])

try:
    from unittest import mock
except ImportError:
    import mock

def test_shape(da, dim):
    assert da.shape == (dim, dim)


def test_dtype(da, data):
    assert da.dtype == data.dtype


def test_getitem(da):
    with mock.patch.object(da, 'hdu') as hdu:
        lc = hdu[0:1, :]

    hdu.__getitem__.assert_called_once_with(
        (slice(0, 1, None), slice(None, None, None)))
