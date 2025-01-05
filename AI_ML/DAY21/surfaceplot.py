import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D



x= np.linspace(-5, 5, 100)

y=np.linspace(-5, 5, 100)

x, y = np.meshgrid(x, y)

z=np.sin(np.sqrt(x**2+ y**2))

#Create a 3D surface plot

fig=plt.figure()

ax=fig.add_subplot(111, projection='3d')

custom_color=(0.6,0.6,0.6)
#Plot the surface 
surface =ax.plot_surface(x, y, z, cmap='viridis',color=custom_color,edgecolor='yellow')


fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Surface Graph')

plt.show()