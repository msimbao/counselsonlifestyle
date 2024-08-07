# useful libraries, including pyWaffle
import matplotlib.pyplot as plt
from pywaffle import Waffle

plt.style.use('rose-pine-dawn.mplstyle')

# create simple dummy data
data = {'Kevin': 10, 'Joseph': 7, 'Yan': 8}

# Basic waffle
plt.figure(
  FigureClass=Waffle,
  rows=5,
  columns=20,
  values=data,
  legend={'loc': 'upper left', 'bbox_to_anchor': (1.05, 1)},
)
plt.show()