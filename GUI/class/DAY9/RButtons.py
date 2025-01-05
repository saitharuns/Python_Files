from tkinter import*

web=Tk()
web.geometry('600x600')



gender=StringVar()

def select():
    print(gender.get())
    lbl.config(text=gender.get())
    
r1=Radiobutton(web,text='male',variable=gender,value='MALE',background='white',font=("bold",20),command=select).place(x='50',y='200')
r1=Radiobutton(web,text='female',variable=gender,value='FEMALE',background='white',font=("bold",20),command=select).place(x='150',y='200')
r1=Radiobutton(web,text='others',variable=gender,value='OTHER',background='white',font=("bold",20),command=select).place(x='270',y='200')


lbl=Label(web,text="")
lbl.place(x=250,y=300)

web.mainloop()