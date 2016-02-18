import pytest
from .context import daskfitsio as df
import numpy as np
import fitsio
try:
    from unittest import mock
except ImportError:
    import mock

@pytest.fixture(scope='session')
def dim():
    return 100


@pytest.fixture(scope='session')
def data(dim):
    return np.random.normal(100, 50, size=(dim, dim))


@pytest.fixture
def fitsfile(tmpdir, data):
    fname = tmpdir.join('test.fits')
    with fitsio.FITS(str(fname), 'rw', clobber=True) as outfile:
        outfile.write(data)
    return str(fname)

@pytest.fixture
def da(fitsfile):
    with fitsio.FITS(fitsfile) as infile:
        return df.DaskAdapter(infile[0])


def test_shape(da, dim):
    assert da.shape == (dim, dim)


def test_dtype(da, data):
    assert da.dtype == data.dtype


def test_getitem(da):
    pass
