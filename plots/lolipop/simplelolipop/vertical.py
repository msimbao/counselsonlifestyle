import matplotlib.pyplot as plt
import numpy as np
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
y = list(np.linspace(1, (np.log(0.2 * np.pi)), 10))
y.sort()
plt.stem(x, y, markerfmt = 's', linefmt='--', basefmt = ':')
plt.show()