import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane()

points = [
    (-3, 9),
    (-2, 4),
    (-1, 1),
    (0, 0),
    (1, 1),
    (2, 4),
    (3, 9),
]

for point in points:
    ax.plot(point[0], point[1], "o", color="blue", markersize=8)

fig.savefig(output)
plt.close()
