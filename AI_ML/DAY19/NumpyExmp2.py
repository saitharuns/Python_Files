import matplotlib.pyplot as plt
import numpy as np

x = np.array([0, 1, 2, 3, 4, 5])

y = np.array([0, 2, 8, 1, 14, 7])



plt.plot(y,label='Toni',marker='*',markerfacecolor='blue',markeredgecolor='green',color='green')
plt.plot(x,label='Venki',marker='D',markerfacecolor='Black',markeredgecolor='yellow',color='yellow')


plt.legend()
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Check')
plt.show()