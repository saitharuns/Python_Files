import matplotlib.pyplot as plt


x = [1,2,3,4]
y=[10,16,27,38]
fig,ax=plt.subplots(facecolor='beige')

#plt.scatter(x,y)
plt.gca().set_facecolor('yellow')
plt.plot(x,y,label='Screen Time',color='green',marker='o',linestyle='dashed',linewidth=2)#linestyle='dashed'
plt.legend()
plt.xlabel('Time')
plt.ylabel('Screen time')
plt.title('ScreenTime')
plt.show()