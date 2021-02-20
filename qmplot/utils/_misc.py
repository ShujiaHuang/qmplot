"""This module contains miscellaneous functions for ``qqman``.
"""
import operator
import numpy as np
from scipy import stats


def chr_id_cmp(a, b):
    """
    Sorted the chromosome by the order.
    
    Parameters
    ----------
        a, b : string or int. 
            a and b are the chromosomes' id. They could be 'chr1', 'chr2'
            or '1' and '2'.
    
    Returns
    -------
    Must be one of the number in [True, False]
    """
    a = a.lower().replace("_", "")
    b = b.lower().replace("_", "")
    achr = a[3:] if a.startswith("chr") else a
    bchr = b[3:] if b.startswith("chr") else b

    try:
        # 1~22 chromosome
        return operator.le(int(achr), int(bchr))
    except ValueError:
        # [1] 22 X
        # [2] X Y
        return operator.le(achr, bchr)


def is_numeric(s):
    """
    It's a useful function for checking if a data is a numeric.

    This function could identify any kinds of numeric: e.g. '0.1', '10', '-2.',
    2.5, etc

    Parameters
    ----------
    s : int, float or string.
        The input could be any kind of single value except the scalable
        type of python like 'list()', 'dict()', 'set()'

    Returns
    -------
        A boolean. Ture if `s` is numeric else False

    Notes
    -----
        http://stackoverflow.com/questions/354038/how-do-i-check-if-a-string-is-a-number-float-in-python
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_integer(s):
    """
    This function could identify any kinds of integer

    Parameters
    ----------
        s : int, float or string.
            The input could be any kind of single value except the scalable
            type of python like 'list()', 'dict()', 'set()'

    Returns
    -------
        A boolean. Ture if `s` is integer value else False
    """
    if is_numeric(s):
        return True if '.' not in s else False
    else:
        return False


def iqr(a):
    """Calculate the IQR for an array of numbers."""
    a = np.asarray(a)
    q1 = stats.scoreatpercentile(a, 25)
    q3 = stats.scoreatpercentile(a, 75)
    return q3 - q1


def freedman_diaconis_bins(a):
    """Calculate number of hist bins using Freedman-Diaconis rule."""
    # From http://stats.stackexchange.com/questions/798/
    a = np.asarray(a)
    h = 2 * iqr(a) / (len(a) ** (1 / 3))
    # fall back to sqrt(a) bins if iqr is 0
    if h == 0:
        return int(np.sqrt(a.size))
    else:
        return int(np.ceil((a.max() - a.min()) / h))
