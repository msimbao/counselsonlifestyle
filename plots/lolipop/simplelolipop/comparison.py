import matplotlib.pyplot as plt
import numpy as np
x = list(map(str, range(1, 35)))
y = list(np.random.random(34))
f, axs = plt.subplots(1,2,figsize=(12,6))
axs[0].barh(x,y)
axs[1].hlines(y=x, xmin = 0 , xmax = y, color='skyblue')
axs[1].plot(y, x, marker = "o", linewidth = 0)
plt.show()