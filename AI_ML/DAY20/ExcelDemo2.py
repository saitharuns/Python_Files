import matplotlib.pyplot as plt
import pandas as pd


data=pd.read_excel('datas.xlsx')



data.columns=data.columns.str.strip()

x=data['X AXIS']
y=data['Y AXIS']
plt.plot(x,y,marker='o',color='blue',label='data line')

plt.show()