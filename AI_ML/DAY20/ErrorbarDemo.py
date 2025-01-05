import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,2*np.pi,100)
y=np.sin(x)
yerr=0.1
xerr=0.2

plt.errorbar(x,y,xerr=xerr,yerr=yerr,fmt='o',color='red',label='Data',elinewidth=2)

plt.title('Error Plt Example')
plt.grid(1)
plt.show()