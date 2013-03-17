from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

import os
import glob

blosc_hdf5_dir = os.path.join(os.environ['BLOSC_DIR'], 'hdf5')
blosc_source_dir = os.path.join(os.environ['BLOSC_DIR'], 'blosc')
hdf5_inc = os.path.join(os.environ['HDF5_DIR'], 'include')

sources = ['hdf5_register_blosc.pyx'] + \
    glob.glob(os.path.join(blosc_source_dir, '*.c')) + \
    [os.path.join(blosc_hdf5_dir, 'blosc_filter.c')]

setup(
    cmdclass = {'build_ext': build_ext},
    ext_modules = [Extension("hdf5_register_blosc",
                             sources)],
    include_dirs = [blosc_hdf5_dir, blosc_source_dir, hdf5_inc]
)
