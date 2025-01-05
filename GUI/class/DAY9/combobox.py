from tkinter import*
from tkinter.ttk import *

web=Tk()
web.geometry('600x600')

def submit():
    c=combo.get()
    if c not in country:
        lbl.config(text='invalid option')
    else:
        lbl.config(text=c)

country=['India','Sri Lanka','China','Russia']
combo=Combobox(web,width=10,values=country)
combo.set("Country")
combo.pack()

b1=Button(web,text='submit',command=submit).pack()

lbl=Label(web,text="",font=('calibri',20))
lbl.pack()

web.mainloop()