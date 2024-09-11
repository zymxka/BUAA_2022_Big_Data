import sys

sys.path.append("../")

import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import pandas as pd
import numpy as np


def boxplot(csv: str):
    ds = pd.read_csv(csv)
    sns.boxplot(x="contest", y="grade", data=ds, palette=sns.cubehelix_palette(9, start=1.5, rot=-0.75))
    plt.show()


def violinplot(csv: str):
    print(csv)
    ds = pd.read_csv(csv)
    # sns.violinplot(x="contest", y="grade", data=ds, palette=sns.cubehelix_palette(9, start=1.5, rot=-0.75))
    group = ds.groupby(["contest"])["grade"]
    medians = group.median().values
    print("medians = ", medians)
    avg = group.mean().values
    print("avg = ", avg)
    print("var = ", group.var().values)
    # plt.show()
    print()


def ridge(csv: str, cnt=13):
    ds = pd.read_csv(csv)
    sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0)})
    pal = sns.cubehelix_palette(cnt, rot=-.4, light=.7)
    g = sns.FacetGrid(ds, row="contest", hue="contest", aspect=9, height=1.2, palette=pal)
    g.map(sns.kdeplot, "grade",
          bw_adjust=.7, clip_on=False,
          fill=True, alpha=1, linewidth=1.5)
    g.map(sns.kdeplot, "grade", clip_on=False, color="w", lw=2, bw_adjust=.7)
    g.refline(y=0, linewidth=2, linestyle="-", color=None, clip_on=False)

    def label(x, color, label):
        ax = plt.gca()
        ax.text(0, .2, label, fontweight="bold", color=color,
                ha="left", va="center", transform=ax.transAxes)

    g.map(label, "grade")
    g.fig.subplots_adjust(hspace=-.5)
    g.set(yticks=[], ylabel="")
    g.set_titles("")
    g.despine(bottom=True, left=True)
    plt.show()


def numbers(title: str):
    with open(f"../../Output/contest/{title}/numbers_{title}.txt", 'w') as f:
        def calc(name: str):
            group = pd.read_csv(f"data{name}{title}.csv").groupby(["contest"])["grade"]
            f.write(f"{name}\n")
            f.write(f"medians = {group.median().values}\n")
            f.write(f"mean = {group.mean().values}\n")
            f.write(f"var = {group.var().values}\n")
            f.write(f"std = {group.std().values}\n\n")

        for i in ['C', 'E', 'CE']:
            calc(i)


matplotlib.rc("font", family="Microsoft YaHei")
title = '2175xwc'

# boxplot("dataCtot.csv")
# boxplot("dataEtot.csv")
# boxplot("dataCEtot.csv")

# violinplot(f"dataC{title}.csv")
# violinplot(f"dataE{title}.csv")
# violinplot(f"dataCE{title}.csv")

# ridge(f"dataC{title}.csv", 7)
# ridge(f"dataE{title}.csv", 7)
# ridge(f"dataCE{title}.csv")

for t in ['2104xwc', '2118', '2174', '2175', '2175xwc', '2176', 'tot']:
    numbers(t)
