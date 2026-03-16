import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane(xlim=(-3, 3), ylim=(-14, 1))


points = [(-2, -13), (-1, 10), (0, -7), (1, -4), (2, -1)]


for point in points:
    ax.plot(point[0], point[1], "o", color="blue", markersize=6)

x = np.linspace(-4, 4, 400)
y = 3 * x - 7

ax.plot(x, y, color="darkblue")

fig.savefig(output)
plt.close()
