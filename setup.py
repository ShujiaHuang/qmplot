"""Setup file and install scripts.

Version 1.0.0 (May 23, 2020)
Copyright (c) 2020 Shujia Huang
"""
import os

try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup, find_packages


DESCRIPTION = ("qmplot: Create high-quality manhattan and QQ plots for PLINK association output (or "
               "any dataframe with chromosome, position, and p-value).")
DISTNAME = "qmplot"
MAINTAINER = "Shujia Huang"
MAINTAINER_EMAIL = "huangshujia9@gmail.com"
URL = "https://github.com/ShujiaHuang/qmplot"
LICENSE = "BSD (3-clause)"
DOWNLOAD_URL = "https://github.com/ShujiaHuang/qmplot"
VERSION = "0.0.5"

INSTALL_REQUIRES = [
    "numpy",
    "scipy",
    "pandas",
    "matplotlib",
]

ROOT_DIR = os.path.split(os.path.realpath(__file__))[0]

if __name__ == "__main__":
    setup(name=DISTNAME,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=(open(ROOT_DIR + "/README.rst").read()),
          license=LICENSE,
          url=URL,
          download_url=DOWNLOAD_URL,
          packages=find_packages(),
          install_requires=INSTALL_REQUIRES,
          version=VERSION,
          include_package_data=True,
          entry_points={
              "console_scripts": [
                  'qmplot = qmplot.main:main'
              ]
          },
          classifiers=[
             'Intended Audience :: Science/Research',
             'Programming Language :: Python :: 3.7',
             'License :: OSI Approved :: BSD License',
             'Topic :: Scientific/Engineering :: Bio-Informatics',
             'Operating System :: POSIX',
             'Operating System :: POSIX :: Linux',
             'Operating System :: MacOS'],
    )
