import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane()

# {(m, 2m) | m=0,+-1, +-2}
points = [
    (0, 0),
    (1, 2),
    (-1, -2),
    (2, 4),
    (-2, -4),
]

for point in points:
    ax.plot(point[0], point[1], "o", color="blue", markersize=8)

fig.savefig(output)
plt.close()
