import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane()


ax.axvline(-2, color="blue", linewidth=2)

fig.savefig(output)
plt.close()
