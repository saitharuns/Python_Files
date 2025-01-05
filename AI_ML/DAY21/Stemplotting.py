import matplotlib.pyplot as plt
import numpy as np

# Define the x values and corresponding y values
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a stem plot
plt.stem(x, y)

# Add title and grid
plt.title('(Stem Plot)')
plt.grid(True)

# Display the plot
plt.show()
