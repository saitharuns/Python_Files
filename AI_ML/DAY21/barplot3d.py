import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



x=np.array([1, 2, 3, 4, 5])

y=np.array([1, 2, 3, 4, 5])

z= np.zeros_like(x)

dx=0.8
dy=0.8 # Dimensions of each bar

dz=[ 2, 3, 5, 1, 4] # Heights of bars

# Create a 3D figure

fig =plt.figure()

ax =fig.add_subplot(111, projection='3d')

#Plot 3D bars

ax.bar3d(x, y, z, dx, dy, dz, color='cyan', edgecolor='black')

ax.set_xlabel('X-axis')

ax.set_ylabel('Y-axis')

ax.set_zlabel('Z-axis')

ax.set_title('3D Bar Plot')

plt.show()