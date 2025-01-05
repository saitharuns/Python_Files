import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


# Define the x values and corresponding y values
np.random.seed(100)
data=np.random.randn(100)
data1=np.random.randn(300)+2
data2=np.random.randn(100)



sb.violinplot(data=[data,data1,data2])

plt.grid(True)

# Display the plot
plt.show()
