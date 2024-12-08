from tkinter import *

#Functionalities

def update():
    file=open("Database.txt",mode='a')
    data=('\nNAME   :',name.get(),
          '\nDOB    :',dob.get(),
          '\nPLACE  :',loc.get(),
          '\nMOBILE :',mobile.get(),
          '\nMAIL   :',email.get(),
          '\n________________________________')          
    file.writelines(data)
    
    name.delete(0,END)
    loc.delete(0,END)
    email.delete(0,END)
    mobile.delete(0,END)
    dob.delete(0,END)
    
    file.close()
    msg.config(text='DATA ADDED SUCCESSFULLY !!!',fg='green',bg='#ededab')

def upd():
    a=len(name.get())
    b=len(loc.get())
    c=len(dob.get())
    d=len(mobile.get())
    e=len(email.get())
    if a==0 or b==0 or c==0 or d==0 or e==0:
        msg.config(text="FILL THE MISSING FIELD.",fg='red',bg='#ededab')
    elif not(name.get().isalpha()) or not(mobile.get().isdigit()) or not(loc.get().isalpha()):
        msg.config(text="FILL THE CORRECT DATA.",fg='red',bg='#ededab')
    else:
        update()


def close():
    w.destroy()

#GUI

w=Tk()
w.geometry('1270x620+-1+-1')

w.config(bg='#ededab')
w.attributes('-fullscreen',True)

lbl=Label(w,text='TONI TECH DATABASE SYSTEM',font=('Impact',40),bg='#ededab',fg='#2e2347')
lbl.place(x=320,y=10)

nlbl=Label(w,text='NAME',font=('Impact',30),bg='#ededab',fg='#1b2224')
nlbl.place(x=320,y=100)

name=Entry(w,font=('Impact',30),fg='#f0f054',bg='#1b2224')
name.place(x=500,y=100)

dlbl=Label(w,text='DOB',font=('Impact',30),bg='#ededab',fg='#1b2224')
dlbl.place(x=320,y=200)

dob=Entry(w,font=('Impact',30),fg='#f0f054',bg='#1b2224')
dob.place(x=500,y=200)

plbl=Label(w,text='PLACE',font=('Impact',30),bg='#ededab',fg='#1b2224')
plbl.place(x=320,y=300)

loc=Entry(w,font=('Impact',30),fg='#f0f054',bg='#1b2224')
loc.place(x=500,y=300)

mlbl=Label(w,text='MOBILE',font=('Impact',30),bg='#ededab',fg='#1b2224')
mlbl.place(x=320,y=400)

mobile=Entry(w,font=('Impact',30),fg='#f0f054',bg='#1b2224')
mobile.place(x=500,y=400)

elbl=Label(w,text='EMAIL',font=('Impact',30),bg='#ededab',fg='#1b2224')
elbl.place(x=320,y=500)

email=Entry(w,font=('Impact',30),fg='#f0f054',bg='#1b2224')
email.place(x=500,y=500)

sbtn=Button(w,text='SUBMIT',command=upd,font=('Impact',30),fg='#f0f054',bg='#2e2347',width=10)
sbtn.place(x=400,y=570)
w.bind("<Return>", lambda event: sbtn.invoke())

qbtn=Button(w,text='EXIT',command=close,font=('Impact',30),fg='#f0f054',bg='#2e2347',width=10)
qbtn.place(x=700,y=570)

msg=Label(w,text="",font=('calibri',20),bg='#ededab')
msg.place(x=500,y=670)

w.mainloop()

