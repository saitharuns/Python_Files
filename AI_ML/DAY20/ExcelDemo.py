import matplotlib.pyplot as plt
import pandas as pd


data=pd.read_excel('MARKS.xlsx')



#ENGLISH	KANNADA	HINDI	MATHS	SCIENCE	SOCIAL


subj=data['CLS']
eng=data['ENGLISH']
kan=data['KANNADA']
hin=data['HINDI']
mat=data['MATHS']
sci=data['SCIENCE']
soc=data['SOCIAL']

plt.plot(subj,eng,marker='D',color='blue',label='ENGLISH')
plt.plot(subj,kan,marker='D',color='red',label='KANNADA')
plt.plot(subj,hin,marker='D',color='yellow',label='HINDI')
plt.plot(subj,mat,marker='D',color='green',label='MATHS')
plt.plot(subj,sci,marker='D',color='brown',label='SCIENCE')
plt.plot(subj,soc,marker='D',color='grey',label='SOCIAL')




plt.grid(1)
plt.legend()
plt.show()