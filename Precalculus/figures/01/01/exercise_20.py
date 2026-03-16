import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from figures.common.style import setup_cartesian_plane
import math

output = Path(__file__).with_suffix(".pdf")

fig: Figure
ax: Axes
fig, ax = setup_cartesian_plane()

points = [
    (-3, 7),
    (1.3, -2),
    (math.pi, math.sqrt(10)),
    (0, 8),
    (-5.5, 0),
    (-8, 4),
    (9.2, -7.8),
    (7, 5),
]

for point in points:
    ax.plot(point[0], point[1], "o", color="blue", markersize=8)

fig.savefig(output)
plt.close()
