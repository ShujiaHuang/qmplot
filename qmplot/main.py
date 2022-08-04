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
    cmdparser.add_argument("--outfiletype", dest="outfiletype", type=str, required=False, default="png",
                           help="The file type of output plot. [png]")
    cmdparser.add_argument("-T", "--title", dest="title", type=str, help="Title of plot", default=None)
    cmdparser.add_argument("-P", "--sign-mark-pvalue", dest="sign_pvalue", type=float,
                           help="Genome wide significant p-value sites. [1e-6]", default=1e-6)
    cmdparser.add_argument("-M", "--top-sign-signal-mark-id", dest="m_id", type=str,
                           help="A string denoting the column name for which you want to annotate "
                                "the top Significant loci. Default: \"ID\"(PLINK2.x)", default="ID")

    cmdparser.add_argument("--ld-block-size", dest="ld_block_size", type=int, default=500000,
                           help="The size of LD block for finding top SNPs. default: 500000")
    cmdparser.add_argument("--dpi", dest="dpi", type=float,
                           help="The resolution in dots-pet-inch for plot. [300]", default=300)
    cmdparser.add_argument("--display", dest="display", action="store_true", 
                           help="Display the plot in screen.")

    args = cmdparser.parse_args()

    return args


def main():
    kwargs = parse_commandline_args()

    if not kwargs.display:
        import matplotlib
        # Using agg, which is a non-GUI backend, so cannot show the plot in screen.
        matplotlib.use("agg")

    import matplotlib.pyplot as plt

    # loading data
    data = pd.read_table(kwargs.input, sep="\t")
    data = data.dropna(how="any", axis=0)  # clean data
    data[["#CHROM"]] = data[["#CHROM"]].astype(str)

    if data["#CHROM"][0].startswith("chr"):
        print("[WARNING] Find 'chr' is the start characters of chromosomal name, this program will "
              "enhance cut the 3 characters when generate manhattan plot. If you want to keep the "
              "original name please write new Python codes by using qmplot as a Python package and "
              "import manhattanplot() function from qmplot then generate the plot by yourself. You "
              "can find more detail of tutorials in github: <https://github.com/ShujiaHuang/qmplot>.")

    data["#CHROM"] = data["#CHROM"].map((lambda x: x[3:] if x.startswith("chr") else x))

    # common parameters for plotting
    plt_params = {
        "pdf.fonttype": 42,
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
                  ld_block_size=kwargs.ld_block_size,
                  text_kws={"fontsize": 12,  # The fontsize of annotate text
                            "arrowprops": dict(arrowstyle="-", color="k", alpha=0.6)},
                  ax=ax)

    plt.savefig(kwargs.outprefix + ".manhattan." + kwargs.outfiletype, dpi=kwargs.dpi)
    if kwargs.display:
        plt.show()

    # Create a Q-Q plot
    f, ax = plt.subplots(figsize=(6, 6), facecolor="w", edgecolor="k")
    qqplot(data=data["P"],
           marker="o",
           title=kwargs.title,
           xlabel=r"Expected $-log_{10}{(P)}$",
           ylabel=r"Observed $-log_{10}{(P)}$",
           ax=ax)

    plt.savefig(kwargs.outprefix + ".QQ." + kwargs.outfiletype, dpi=kwargs.dpi)
    if kwargs.display:
        plt.show()

    print(">>>>>>>>>>>>>>>>> Create Manhattan and Q-Q plots done <<<<<<<<<<<<<<<<<")
    return
