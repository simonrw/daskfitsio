import pytest
import dask.array as da
import fitsio
from .context import daskfitsio as df


@pytest.fixture
def chunks():
    return (10, 10)


def test_hdu(fitsfile, dim, chunks):
    with fitsio.FITS(fitsfile) as infile:
        hdu = infile[0]
        data = df.read_hdu(hdu, chunks=chunks)
        assert isinstance(data, da.Array)
