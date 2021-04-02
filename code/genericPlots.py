"""genericPlots.py
Plots that require matplotlib (but not plotly)
"""
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def publisher_histogram(df, title, ylabel):
    """
    A specifically selected dataframe.
    From df->clean_df->pyblishers
    Plot a histogram showing the distribution
    """
    plt.close("all")
    fig, ax = plt.subplots(1, 1,figsize=(8,6))
    x = np.arange(len(df))
    ax.bar(x, df)
    ax.set_xticks(x)
    ax.set_xticklabels(df.index)
    ax.tick_params(axis="x", rotation=90)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    return fig, ax


def distribution(df, keys):
    """Plot the sorted values of the df based on list
    Input:
       df [pandas dataframe series] : With the data
       keys [list of strings]  : Names of columns to plot
    """
    fig, ax = plt.subplots(1,1,figsize=(12,10))

    for key in keys:
        x = np.arange(len(df))
        y = sorted(df[key].to_numpy(), reverse=False)
        ax.hist(y, bins=100, label=key, alpha=0.70)
    ax.grid(True)
    ax.legend()
    ax.set_xlim([-1, 5])
    ax.set_xlabel("No samples in value")

    return fig, ax
