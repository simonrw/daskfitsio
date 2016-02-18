import pytest
import numpy as np
import fitsio
from .context import daskfitsio as df
try:
    from unittest import mock
except ImportError:
    import mock


@pytest.fixture
def da(fitsfile):
    with fitsio.FITS(fitsfile) as infile:
        return df.DaskAdapter(infile[0])


def test_shape(da, dim):
    assert da.shape == (dim, dim)


def test_dtype(da, data):
    assert da.dtype == data.dtype


def test_getitem(da):
    with mock.patch.object(da, 'hdu') as hdu:
        lc = hdu[0:1, :]

    hdu.__getitem__.assert_called_once_with(
        (slice(0, 1, None), slice(None, None, None)))


@pytest.mark.parametrize('dtype', [
    np.int8, np.int16, np.int32, np.float32, np.float64,
])
def test_multiple_dtypes(dtype, tmpdir, dim):
    data = np.random.uniform(10, 100, size=(dim, dim)).astype(dtype)
    fname = tmpdir.join('test.fits')
    with fitsio.FITS(str(fname), 'rw', clobber=True) as outfile:
        outfile.write(data)

    with fitsio.FITS(str(fname)) as infile:
        adapter = df.DaskAdapter(infile[0])
        assert adapter.dtype == dtype


def test_int64_support(tmpdir, dim):
    data = np.random.uniform(10, 100, size=(dim, dim)).astype(np.int64)
    fname = tmpdir.join('test.fits')
    with fitsio.FITS(str(fname), 'rw', clobber=True) as outfile:
        outfile.write(data)

    with fitsio.FITS(str(fname)) as infile:
        adapter = df.DaskAdapter(infile[0])
        assert adapter.dtype == np.int32


def test_unsupported_dtypes():
    hdu = mock.MagicMock(get_info=lambda: {'img_type': 10203})
    adapter = df.DaskAdapter(hdu)
    with pytest.raises(ValueError) as err:
        print(adapter.dtype)
    issues_url = 'https://github.com/mindriot101/daskfitsio/issues/new'
    assert issues_url in str(err)
