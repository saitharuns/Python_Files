from tkinter import*

web=Tk()
web.geometry('600x600')

def select():
    var=pan.get(),aadhaar.get()
    lbl.config(text=var)

pan=IntVar()
aadhaar=IntVar()

cb1=Checkbutton(web,text='PAN CARD',variable=pan,onvalue=1,offvalue=0,command=select).pack()
cb2=Checkbutton(web,text='ADHAAR',variable=aadhaar,onvalue=2,offvalue=0,command=select).pack()

lbl=Label(web,text="")
lbl.place(x=250,y=300)

web.mainloop()