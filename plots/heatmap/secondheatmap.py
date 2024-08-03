import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib import colormaps

import numpy as np

import matplotlib
import matplotlib as mpl


vegetables = ["Red Meat",
              "Fish",
              "High-fat dairy",
              "Low-fat dairy",
              "Eggs",
              "Nuts",
              "Beans"]

farmers = ["Low", "Medium",
           "High", "Very High"]

harvest = np.array([[1.15,1.18,1.33,1.75],
                    [0.64,0.86,0.59,0.67],
                    [0.79,0.86,0.89,1.15],
                    [0.68,0.63,0.63,0.67],
                    [0.92,0.74,1.17,0.98],
                    [0.61,0.85,0.63,0.54],
                    [0.56,0.73,0.83,0.75]])


fig, ax = plt.subplots()
im = ax.imshow(harvest,cmap=mpl.colormaps['coolwarm'])

# Show all ticks and label them with the respective list entries
# ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

# Rotate the tick labels and set their alignment.
# plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
#          rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="black")

ax.set_title("Risk of Coronary Heart Disease by Amount of Protein Consumed")
fig.tight_layout()
plt.show()

print(len())
