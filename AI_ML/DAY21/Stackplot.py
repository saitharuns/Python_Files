import matplotlib.pyplot as plt
import numpy as np

# Define the x values and corresponding y values
x = np.arange(1,11)

y1= np.array([10,2,3,4,10,6,7,8,9,10])
y3 = np.array([10,2,3,4,10,6,7,8,9,10])
y2 = np.array([10,9,8,7,6,10,4,3,2,10])


plt.stackplot(x,y1,y2,y3,labels=['y1','y2','y3'],colors=['maroon','yellow','maroon'],alpha=0.8)

# Add title and grid
plt.title('TVK')


# Display the plot
plt.show()
