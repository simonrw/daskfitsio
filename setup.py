from setuptools import setup

install_requires = ['numpy', 'dask']
test_requires = install_requires + ['pytest']

with open('README.rst') as infile:
    readme = infile.read()

setup(
    name='daskfitsio',
    version='0.0.1',
    author='Simon Walker',
    author_email='s.r.walker101@googlemail.com',
    description='Wrapper around `fitsio.ImageHDU` creating a `dask.Array`',
    long_description=readme,
    py_modules=['daskfitsio'],
    install_requires=install_requires,
    tests_require=test_requires,
)
