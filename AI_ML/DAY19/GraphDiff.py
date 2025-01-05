import matplotlib.pyplot as plt
import numpy as np

fig,axs=plt.subplots(2,2)
y = np.array([0, 2, 8, 1, 14, 7])
x = np.array([1, 2, 3, 4, 5, 6])


axs[0, 0].plot(x,y)
axs[0, 1].scatter(x,y)
axs[1, 0].bar(x,y)
axs[1, 1].hist(x)

plt.show()