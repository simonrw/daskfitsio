import pytest
from .context import daskfitsio as df
import numpy as np
import fitsio

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
