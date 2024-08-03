import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl


vegetables = ["Oral Cavity and Pharyngeal",
              "Laryngeal",
              "Esophageal",
              "Gastric",
              "Colorectal",
              "Liver",
              "Pancreatic Men",
              "Pancreatic Women",
              "Lung",
              "Bladder",
              "Kidney",
              "Thyroid",
              "Non-Hodgkin Lymphoma",
              "Leukemia",
              "Melanoma",
              "Brain",
              "Myeloma",
              "Prostate",
              "Female Breast",
              "Endometrial",
              "Ovarian",
              "Cervical"]

farmers = ["Ref", "Low", "Medium",
           "High", "Very High"]

harvest = np.array([[1, 1.07, 0.96, 0.97, 1.17],
                    [1, 1.23, 1.35, 1.32, 1.33],
                    [1, 0.95, 0.96, 1.00, 0.94],
                    [1, 0.92, 0.78, 0.90, 1.00],
                    [1, 1.05, 1.09, 1.18, 1.20],
                    [1, 1.13, 1.11, 1.16, 1.09],
                    [1, 1.24, 1.06, 1.39, 1.31],
                    [1, 1.03, 1.16, 1.00, 0.86],
                    [1, 1.08, 1.07, 1.16, 1.16],
                    [1, 1.13, 1.14, 1.19, 1.16],
                    [1, 1.13, 1.15, 1.20, 1.18],
                    [1, 0.88, 0.71, 0.89, 0.93],
                    [1, 1.10, 1.05, 1.08, 1.03],
                    [1, 0.83, 0.88, 0.82, 0.80],
                    [1, 0.81, 0.88, 0.90, 0.82],
                    [1, 1.14, 1.01, 0.94, 0.88],
                    [1, 0.94, 0.91, 0.98, 1.30],
                    [1, 1.01, 1.01, 1.01, 1.02],
                    [1, 1.04, 0.94, 1.09, 1.03],
                    [1, 0.93, 0.99, 0.91, 1.02],
                    [1, 1.14, 1.21, 1.13, 1.23],
                    [1, 0.97, 0.77, 1.05, 1.72]])


fig, ax = plt.subplots()
im = ax.imshow(harvest)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(vegetables)):
    for j in range(len(farmers)):
        text = ax.text(j, i, harvest[i, j],
                       ha="center", va="center", color="w")

ax.set_title("Harvest of local farmers (in tons/year)")
fig.tight_layout()
plt.show()

print(len())
