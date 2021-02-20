qmplot: A Python tool for creating high-quality manhattan and Q-Q plots from GWAS results.
==========================================================================================

**qmplot** is a handy tool and Python package for creating high-quality manhattan and Q-Q plots from PLINK association output or any dataframe with chromosome, position and p-value.

This library is inspired by [r-qqman](https://github.com/stephenturner/qqman).

Dependencies
------------

qmplot supports Python 3.6+ and no longer supports Python 2.

Instatllation requires [numpy](https://numpy.org/), [scipy](https://www.scipy.org/), [pandas](https://pandas.pydata.org/) and [matplotlib](https://matplotlib.org/).

Installation
------------

**qmplot** is written by Python and release in PyPI. The latest stable release can be installed by running the following command:

.. code:: bash
    
    pip install qmplot


Quick Start
-----------

We use a PLINK2.x association output data "[gwas_plink_result.tsv](tests/data/gwas_plink_result.tsv)" which is in `tests/data` directory, 
as the input for the plots below. Here is the format preview of "gwas_plink_result.tsv":

|#CHROM|POS    |ID       |REF   |ALT   |A1    |TEST  |OBS_CT|BETA      |SE      |T_STAT   |P        |
|:----:|:-----:|:-------:|:----:|:----:|:----:|:----:|:----:|:--------:|:------:|:-------:|:-------:|
|1     |904165 |1_904165 |G     |A     |A     |ADD   |282   |-0.0908897|0.195476|-0.464967|0.642344 |
|1     |1563691|1_1563691|T     |G     |G     |ADD   |271   |0.447021  |0.422194|1.0588   |0.290715 |
|1     |1707740|1_1707740|T     |G     |G     |ADD   |283   |0.149911  |0.161387|0.928888 |0.353805 |
|1     |2284195|1_2284195|T     |C     |C     |ADD   |275   |-0.024704 |0.13966 |-0.176887|0.859739 |
|1     |2779043|1_2779043|T     |C     |T     |ADD   |272   |-0.111771 |0.139929|-0.79877 |0.425182 |
|1     |2944527|1_2944527|G     |A     |A     |ADD   |276   |-0.054472 |0.166038|-0.32807 |0.743129 |
|1     |3803755|1_3803755|T     |C     |T     |ADD   |283   |-0.0392713|0.128528|-0.305547|0.760193 |
|1     |4121584|1_4121584|A     |G     |G     |ADD   |279   |0.120902  |0.127063|0.951511 |0.342239 |
|1     |4170048|1_4170048|C     |T     |T     |ADD   |280   |0.250807  |0.143423|1.74873  |0.0815274|

**qmplot** apply two ways to generate manhattan and Q-Q plots:

1. Commandline options

This is the simplest way to plot manhattan and QQ plots if you already have PLINK2.x associtation output.
You can directly type `qmplot --help` and will find all the options below:

.. code:: bash

    usage: qmplot [-h] -I INPUT -O OUTPREFIX [-T TITLE] [-P SIGN_PVALUE] [-M M_ID]
              [--open-gui]

    qmplot: Creates high-quality manhattan and QQ plots from PLINK association
    output (or any dataframe with chromosome, position, and p-value).

    optional arguments:
      -h, --help            show this help message and exit
      -I INPUT, --input INPUT
                            Input file
      -O OUTPREFIX, --outprefix OUTPREFIX
                            The prefix of output file
      -T TITLE, --title TITLE
                            Title of figure
      -P SIGN_PVALUE, --sign-mark-pvalue SIGN_PVALUE
                            Genome wide significant p-value sites. [1e-6]
      -M M_ID, --top-sign-signal-mark-id M_ID
                            A string denoting the column name for which you want
                            to annotate the Top Significant SNPs. Default:
                            PLINK2.x's "ID"
      --open-gui            Set to be GUI backend, which can show the figure.


The following command will give you the two png plots with 300 dpi resolution:

.. code:: bash
    
    $ qmplot -I data/gwas_plink_result.tsv -T Test -M ID --dpi 300 -O test

The manhattan plot looks like:

![manhattanplot](tests/test.manhattan.png)

The Q-Q plot looks like:

![qqplot](tests/test.QQ.png)

Note: You can only modify the plots throught `qmplot` commandline options which whill be a big limitation when you want to make more change.

2. Python package

This is the most flexible way. You can use qmplot as a package in you Python code and create the plots by your mind. 

### Manhattan plot with default parameters:

.. code:: python

    import pandas as pd
    from qmplot import manhattanplot

    if __name__ == "__main__":

        df = pd.read_table("tests/data/gwas_plink_result.tsv", sep="\t")
        df = df.dropna(how="any", axis=0)  # clean data
        ax = manhattanplot(data=df, figname="output_manhattan_plot.png")

![output_manhattan_plot.png](tests/output_manhattan_plot.png)

### A better Manhattan plot

.. code:: python

    import pandas as pd
    from qmplot import manhattanplot

    if __name__ == "__main__":

        df = pd.read_table("tests/data/gwas_plink_result.tsv", sep="\t")
        df = df.dropna(how="any", axis=0)  # clean data

        # Create a manhattan plot
        f, ax = plt.subplots(figsize=(12, 4), facecolor='w', edgecolor='k')
        xtick = set(list(map(str, range(1, 15))) + ['16', '18', '20', '22', 'X'])
        manhattanplot(data=data,
                      marker=".",
                      sign_marker_p=1e-6,  # Genome wide significant p-value
                      sign_marker_color="r",
                      snp="ID",

                      title="Test",
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
                                    "bbox": dict(boxstyle="round", alpha=0.2), 
                                    "arrowprops": dict(arrowstyle="->",  # "-|>"
                                                       connectionstyle="angle,angleA=0,angleB=80,rad=10",
                                                       alpha=0.6, relpos=(0, 0))},

                      dpi=300,
                      figname="output_manhattan_plot.png",
                      ax=ax)

![manhattanplot](tests/test.manhattan.png)

Find more detail about the parameters by typing ``manhattanplot?`` in IPython console.

### QQ plot with defualt parameters.

.. code:: python

    import pandas as pd
    from qmplot import qqplot

    if __name__ == "__main__":

        df = pd.read_table("tests/data/gwas_plink_result.tsv", sep="\t")
        df = df.dropna(how="any", axis=0)  # clean data
        ax = qqplot(data=list(df["P"]), figname="output_QQ_plot.png")

![output_QQ_plot.png](tests/output_QQ_plot.png)

### A better QQ plot

.. code:: python

    import pandas as pd
    from qmplot import qqplot

    if __name__ == "__main__":

        df = pd.read_table("tests/data/gwas_plink_result.tsv", sep="\t")
        df = df.dropna(how="any", axis=0)  # clean data
        # Create a Q-Q plot
        f, ax = plt.subplots(figsize=(6, 6), facecolor="w", edgecolor="k")
        qqplot(data=list(data["P"]),
               marker="o",
               title="Test",
               xlabel=r"Expected $-log_{10}{(P)}$",
               ylabel=r"Observed $-log_{10}{(P)}$",
               dpi=300,
               figname="output_QQ_plot.png",
               ax=ax)

![qqplot](tests/test.QQ.png)

Find more detail about the parameters by typing ``qqplot?`` in IPython console.

