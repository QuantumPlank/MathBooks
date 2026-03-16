import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
import numpy as np


def setup_cartesian_plane(
    xlim: tuple[int, int] = (-10, 10),
    ylim: tuple[int, int] = (-10, 10),
    figsize: tuple[int, int] = (6, 6),
) -> tuple[Figure, Axes]:
    """
    Returns:
        tuple[Figure, Axes]: A Matplotlib Figure and its primary Axes object.
    """
    fig, ax = plt.subplots(figsize=figsize)

    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")

    ax.tick_params(axis="both", which="major", labelsize=6)
    ax.grid(True, linestyle="--", linewidth=0.5)
    ax.set_aspect("equal", adjustable="box")

    xticks = np.arange(xlim[0], xlim[1] + 1, 1)
    xticks = xticks[xticks != 0]
    ax.set_xticks(xticks)

    yticks = np.arange(ylim[0], ylim[1] + 1, 1)
    yticks = yticks[yticks != 0]
    ax.set_yticks(yticks)

    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])

    return fig, ax
