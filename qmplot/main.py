"""The main function for qmplot

Author: Shujia Huang
Date: 2021-02-04 12:01:34
"""
import argparse
import pandas as pd

from qmplot import manhattanplot, qqplot


def parse_commandline_args():
    """Parse input commandline arguments, handling multiple cases.
    """
    desc = ("qmplot: Creates high-quality manhattan and QQ plots from PLINK association output (or "
            "any dataframe with chromosome, position, and p-value).")
    cmdparser = argparse.ArgumentParser(description=desc)
    cmdparser.add_argument("-I", "--input", dest="input", type=str, required=True, help="Input file")
    cmdparser.add_argument("-O", "--outprefix", dest="outprefix", type=str, required=True,
                           help="The prefix of output file")
    cmdparser.add_argument("-T", "--title", dest="title", type=str, help="Title of figure", default=None)
    cmdparser.add_argument("-P", "--sign-mark-pvalue", dest="sign_pvalue", type=float,
                           help="Genome wide significant p-value sites. [1e-6]", default=1e-6)
    cmdparser.add_argument("-M", "--top-sign-signal-mark-id", dest="m_id", type=str,
                           help="A string denoting the column name for which you want to annotate "
                                "the Top Significant SNPs. Default: PLINK2.x's \"ID\"", default="ID")

    cmdparser.add_argument("--dpi", dest="dpi", type=float,
                           help="The resolution in dots-pet-inch for plot. [300]", default=300)
    cmdparser.add_argument("--open-gui", dest="open_gui", action="store_true",
                           help="Set to be GUI backend, which can show the figure.")

    args = cmdparser.parse_args()

    return args


def main():
    kwargs = parse_commandline_args()

    import matplotlib
    if not kwargs.open_gui:
        matplotlib.use("agg")  # Using agg, which is a non-GUI backend, so cannot show the figure.
    import matplotlib.pyplot as plt

    # loading data
    data = pd.read_table(kwargs.input, sep="\t")
    data = data.dropna(how="any", axis=0)  # clean data

    # common parameters for plotting
    plt_params = {
        "font.sans-serif": "Arial",
        "legend.fontsize": 14,
        "axes.titlesize": 18,
        "axes.labelsize": 16,
        "xtick.labelsize": 14,
        "ytick.labelsize": 14
    }
    plt.rcParams.update(plt_params)

    # Create a manhattan plot
    f, ax = plt.subplots(figsize=(12, 4), facecolor='w', edgecolor='k')
    xtick = set(list(map(str, range(1, 15))) + ['16', '18', '20', '22', 'X'])
    manhattanplot(data=data,
                  marker=".",

                  sign_marker_p=kwargs.sign_pvalue,  # Genome wide significant p-value
                  sign_marker_color="r",
                  snp=kwargs.m_id,

                  title=kwargs.title,
                  xtick_label_set=xtick,  # CHR='8', # specific showing the chromosome 8th
                  xlabel="Chromosome",
                  ylabel=r"$-log_{10}{(P)}$",

                  sign_line_cols=["#D62728", "#2CA02C"],
                  hline_kws={"linestyle": "--", "lw": 1.3},

                  is_annotate_topsnp=True,
                  ld_block_size=50000,  # 50000 bp
                  annotext_kws={"size": 12,  # The fontsize of annotate text
                                "xycoords": "data",
                                "xytext": (15, +15),
                                "textcoords": "offset points",
                                "bbox": dict(boxstyle="round", alpha=0.2),  # dict(boxstyle="round", fc="0.8")
                                "arrowprops": dict(arrowstyle="->",  # "-|>"
                                                   connectionstyle="angle,angleA=0,angleB=80,rad=10",
                                                   alpha=0.6, relpos=(0, 0)),
                                # "arrowprops": dict(arrowstyle="wedge,tail_width=0.5", alpha=0.2, relpos=(0, 0)),
                                },

                  dpi=kwargs.dpi,
                  is_show=False,
                  figname=kwargs.outprefix + ".manhattan.png",
                  ax=ax)

    # Create a Q-Q plot
    f, ax = plt.subplots(figsize=(6, 6), facecolor="w", edgecolor="k")
    qqplot(data=data["P"],
           marker="o",
           title=kwargs.title,
           xlabel=r"Expected $-log_{10}{(P)}$",
           ylabel=r"Observed $-log_{10}{(P)}$",
           figname=kwargs.outprefix + ".QQ.png",
           dpi=kwargs.dpi,
           is_show=False,
           ax=ax)

    print(">>>>>>>>>>>>>>>>> Create Manhattan and Q-Q plots done <<<<<<<<<<<<<<<<<")
    return
