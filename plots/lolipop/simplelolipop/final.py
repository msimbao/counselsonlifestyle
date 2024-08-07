import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

x=['Beans','Fish','Nuts','Poultry','Low-Fat Dairy','High-Fat Dairy','Red Meat']
y=[0.48,0.54,0.63,0.73,0.91,1.07,1.46]
y.sort()

plt.stem(x, y, markerfmt = 'o', linefmt='-', basefmt = '-', orientation="horizontal", bottom=1)
sns.set_theme(style="white", palette="Greys")

# (markers, stemlines, baseline) = plt.stem(
#     x,
#     y,
#     bottom=1,
#     markerfmt = 'X',
#     linefmt='-',
#     basefmt = '-',
#     )

# plt.setp(
#     markers,
#     marker="o",
#     color="lightblue",
#     markersize=2,
#     markeredgecolor="lightgreen",
#     markeredgewidth="0.5"
#     )
# plt.set_title("Risk of Coronary Heart Disease by Amount of Protein Consumed")

plt.show()
