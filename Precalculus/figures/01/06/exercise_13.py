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

x1 = np.linspace(-10, 3)
y1 = 4 - x1
x2 = np.linspace(3, 10)
y2 = np.full_like(x2, 2.0)


ax.plot(x1, y1, color="blue")
ax.plot(x2, y2, color="blue")
ax.plot(3, 1, "o", color="blue", markeredgewidth=2)
ax.plot(3, 2, "o", markerfacecolor="white", markeredgecolor="blue", markeredgewidth=2)

fig.savefig(output)
plt.close()
