import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane(ylim=(-1, 12))


points = [
    (-3, 10),
    (-2, 5),
    (-1, 2),
    (0, 1),
    (1, 2),
    (2, 5),
    (3, 10),
]


for point in points:
    ax.plot(point[0], point[1], "o", color="blue", markersize=6)

x = np.linspace(-10, 10, 400)
y = x**2 + 1

ax.plot(x, y, color="darkblue")

fig.savefig(output)
plt.close()
