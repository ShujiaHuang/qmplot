"""
Utility functionality (:mod:`qqman.utils`)
============================================

This package provides general exception/warning definitions used throughout
qqman, as well as various utility functionality, including plotting and
unit-testing convenience functions.

"""
from ._misc import chr_id_cmp, is_numeric, is_integer, iqr, freedman_diaconis_bins

__all__ = ["chr_id_cmp",
           "is_numeric",
           "is_integer",
           "iqr",
           "freedman_diaconis_bins"]

