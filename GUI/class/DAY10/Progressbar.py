from tkinter import*
from tkinter.ttk import *
import time

w=Tk()
w.geometry('600x600')



def prgstart():
    pgb.start(3)
    '''val=ent.get()
    pgb.config(value=val)'''
    
    #using loop
    '''while(bt):
        for x in range(0,100,10):
            w.update_idletasks()
            pgb['value']=x
            time.sleep(0.1)
        for y in range(100,0,-10):
            w.update_idletasks()
            pgb['value']=y
            time.sleep(0.1)'''

def prgstp():
    pgb.stop()
    
    

    

    

lbl2=Label(w,text='PROGRESS BAR DEMO',font=('impact',20))
lbl2.pack(pady=20)

#pgb=Progressbar(w,length=500,maximum=100,mode='indeterminate').pack()
pgb=Progressbar(w,length=500,maximum=100,mode='indeterminate')
pgb.pack(pady=10)


lbl2=Label(w,text='',font=('impact',20))
lbl2.pack(pady=20)

'''ent=Entry(w)
ent.pack(padx=10)
'''
btn=Button(w,text='START',command=prgstart)
btn.pack(pady=10)

btn=Button(w,text='STOP',command=prgstp)
btn.pack(pady=10)

w.mainloop()