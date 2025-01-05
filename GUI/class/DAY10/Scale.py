from tkinter import*
#from tkinter.ttk import *

w=Tk()
w.geometry('600x600')


def submit(value):
    lbl.config(text=value)


def done():
    lbl2.config(text=int(sc.get()))



sc=Scale(w,length=500,width=20,from_=0,to=100,orient=HORIZONTAL,cursor='dot',tickinterval='10',bg='maroon',troughcolor='yellow',fg='white',command=submit)
sc.pack()

lbl=Label(w,text='TONI',font=('impact',20))
lbl.pack(padx=20)
lbl2=Label(w,text='',font=('impact',20))
lbl2.pack(padx=20)
btn=Button(w,text='SUBMIT',command=done).pack()


w.mainloop()