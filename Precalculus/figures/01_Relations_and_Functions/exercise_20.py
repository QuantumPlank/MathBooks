import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import math

output = Path(__file__).with_suffix(".pdf")

fig, ax = plt.subplots(figsize=(6,6))
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.tick_params(axis='both', which='major', labelsize=6)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_aspect('equal', adjustable="box")
ax.set_xlim(-10,10)
ax.set_ylim(-10,10)
xticks = np.arange(-10, 11, 1)
xticks = xticks[xticks != 0]
ax.set_xticks(xticks)
yticks = np.arange(-10, 11, 1)
yticks = yticks[yticks != 0]
ax.set_yticks(yticks)


points = [(-3, 7), (1.3, -2), (math.pi, math.sqrt(10)), (0,8), (-5.5,0), (-8,4), (9.2, -7.8), (7,5)]
x, y = zip(*points)
plt.scatter(x, y)

plt.savefig(output)
plt.close()

