"""Setup file and install scripts.

Copyright (c) 2020 Shujia Huang
Date: May 23, 2020
"""
import os
from argparse import Namespace

DESCRIPTION = ("qmplot: Create high-quality manhattan and QQ plots for PLINK association "
               "output (or any dataframe with chromosome, position, and p-value).")
meta = Namespace(
    __DISTNAME__="qmplot",
    __AUTHOR__="Shujia Huang",
    __AUTHOR_EMAIL__="huangshujia9@gmail.com",
    __URL__="https://github.com/ShujiaHuang/qmplot",
    __LICENSE__="BSD (3-clause)",
    __DOWNLOAD_URL__="https://github.com/ShujiaHuang/qmplot",
    __VERSION__="0.3.0",
)

try:
    from setuptools import setup, find_packages

    _has_setuptools = True
except ImportError:
    from distutils.core import setup, find_packages

INSTALL_REQUIRES = [
    "numpy",
    "scipy",
    "pandas",
    "matplotlib",
]

ROOT_DIR = os.path.split(os.path.realpath(__file__))[0]

if __name__ == "__main__":
    setup(name=meta.__DISTNAME__,
          author=meta.__AUTHOR__,
          author_email=meta.__AUTHOR_EMAIL__,
          maintainer=meta.__AUTHOR__,
          maintainer_email=meta.__AUTHOR_EMAIL__,
          description=DESCRIPTION,
          long_description=(open(ROOT_DIR + "/README.rst").read()),
          license=meta.__LICENSE__,
          url=meta.__URL__,
          download_url=meta.__DOWNLOAD_URL__,
          packages=find_packages(),
          install_requires=INSTALL_REQUIRES,
          version=meta.__VERSION__,
          include_package_data=True,
          entry_points={
              "console_scripts": [
                  'qmplot = qmplot.main:main'
              ]
          },
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 3.7',
              'Programming Language :: Python :: 3.8',
              'Programming Language :: Python :: 3.9',
              'Programming Language :: Python :: 3.10',
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Bio-Informatics',
              'Operating System :: POSIX',
              'Operating System :: POSIX :: Linux',
              'Operating System :: MacOS'],
          )
