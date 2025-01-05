import matplotlib.pyplot as plt
import numpy as np


y = np.array([0, 2, 8, 1, 14, 7])

plt.plot(y,label='Screen Time',color='green',marker='o',linestyle='dashed',linewidth=2)#linestyle='dashed'
plt.legend()
plt.xlabel('Time')
plt.ylabel('Screen time')
plt.title('ScreenTime')
plt.show()