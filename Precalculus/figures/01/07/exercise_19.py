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

x1 = np.linspace(-10, 10, 1000)
y1 = np.abs(x1)

x2 = np.linspace(-10, 10, 1000)
y2 = np.abs(x2) + 1

ax.plot(x1, y1, color="gray")
ax.plot(x2, y2, color="blue")

fig.savefig(output)
plt.close()
