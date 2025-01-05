import matplotlib.pyplot as plt
import numpy as np

x = np.random.random(100)

y = np.array([0, 20, 81, 78, 34, 47])



plt.hist(x,label='Toni',color='green',bins=30,edgecolor='blue',alpha=0.5,density=True)



#plt.legend()

plt.title('Power Check')
plt.show()