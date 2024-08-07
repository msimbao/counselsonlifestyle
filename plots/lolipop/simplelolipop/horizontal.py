import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

sns.set_theme(style="white")

# plt.style.use('ggplot')

x=['Beans','Fish','Nuts','Poultry','Low-Fat Dairy','High-Fat Dairy','Red Meat']

y=[0.48,0.54,0.63,0.73,0.91,1.07,1.46]

my_range=range(1,len(x)+1)
plt.hlines(y=x, xmin = 1 , xmax = y,linestyles="--")
plt.plot(y, x, 'o')
plt.show()

