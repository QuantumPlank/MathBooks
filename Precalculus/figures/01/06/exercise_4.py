import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane
import numpy as np

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane()

x = np.linspace(-10, 10)
y = 4 - x**2

ax.plot(x, y)

fig.savefig(output)
plt.close()
