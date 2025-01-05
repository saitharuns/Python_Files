import matplotlib.pyplot as plt
import numpy as np

x = np.array([10, 20, 30, 25, 40, 51])
y = np.array(['a','b','c','d','e','f'])


plt.bar(y,x,label='Toni',color='green')


plt.legend()
plt.xlabel('Time')
plt.ylabel('Power')
plt.title('Power Check')
plt.show()