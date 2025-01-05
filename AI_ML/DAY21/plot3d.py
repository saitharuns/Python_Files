import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



x=np.linspace(0,10,100)
y=np.sin(x)
z=np.cos(x)
a=np.tan(x)


fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

ax.scatter(x,z,a,color='maroon')



# Display the plot
plt.show()
