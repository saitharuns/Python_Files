import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb

# Define the x values and corresponding y values
data=np.random.randn(100)
data1=np.random.randn(300)




plt.boxplot([data,data1])

plt.grid(True)

# Display the plot
plt.show()
