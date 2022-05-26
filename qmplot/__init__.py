import matplotlib
from .modules import manhattanplot, qqplot, qqnorm

matplotlib.rcParams['ps.fonttype']     = 42
matplotlib.rcParams['pdf.fonttype']    = 42
matplotlib.rcParams['font.sans-serif'] = ["Arial","Lucida Sans","DejaVu Sans","Lucida Grande","Verdana"]
matplotlib.rcParams['font.family']     = 'sans-serif'

__all__ = ["manhattanplot", "qqplot", "qqnorm"]
