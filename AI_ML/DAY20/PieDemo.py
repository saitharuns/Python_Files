import matplotlib.pyplot as plt


labels=['APPLE','MANGO','BANANA','ORANGE','GRAPES']
sizes=[20,30,10,25,15]
colors=['red','green','yellow','orange','blue']
explodes=(0,0.1,0,0,0)

plt.pie(sizes,explode=explodes,labels=labels,colors=colors,autopct='%1.1f%%',startangle=140)
#plt.legend(labels,loc='best')

plt.show()