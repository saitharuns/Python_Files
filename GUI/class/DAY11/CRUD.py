import sqlite3
from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('500x500+400+80')

def database():
    global conn,cursor
    conn = sqlite3.connect("BIT.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS STUDENT_DATA("NAME" VARCHAR(20),"MOBILE" LONGINT(10),"MAIL" VARCHAR(20))')
    cursor.execute('CREATE TABLE IF NOT EXISTS STAFF_DATA("NAME" VARCHAR(20),"MOBILE" LONGINT(10),"MAIL" VARCHAR(20))')
    conn.commit()
    


def update_st():
    database()
    if messagebox.askyesno('DB','DO YOU LIKE TO JOIN'):
        cursor.execute("INSERT INTO `STUDENT_DATA` (name,mobile,mail) VALUES(?, ?, ?)",(str(ST_NAME.get()),int(ST_MOBILE.get()),str(ST_MAIL.get())))
        name.delete(0,END)
        mobile.delete(0,END)
        mail.delete(0,END)
        messagebox.showinfo('DB','VALUE INSERTED')
        conn.commit()
        cursor.close()
    else:
        messagebox.showinfo('DB','VALUE NOT INSERTED')



ST_NAME=StringVar()
ST_MOBILE=StringVar()
ST_MAIL=StringVar()

hlbl=Label(w,text='STUDENT DATA',font=('Impact',20)).grid(column=0,row=0,padx=3,pady=5,columnspan=2)
nm=Label(w,text='NAME',font=('Impact',20)).grid(column=0,row=1,padx=3,pady=5)
name=Entry(w,width=20,textvariable=ST_NAME,font=('Impact',20))
name.grid(column=1,row=1,padx=3,pady=5)
mob=Label(w,text='MOBILE',font=('Impact',20)).grid(column=0,row=2,padx=3,pady=5)
mobile=Entry(w,width=20,textvariable=ST_MOBILE,font=('Impact',20))
mobile.grid(column=1,row=2,padx=3,pady=5)
mailid=Label(w,text='MAIL',font=('Impact',20)).grid(column=0,row=3,padx=3,pady=5)
mail=Entry(w,width=20,textvariable=ST_MAIL,font=('Impact',20))
mail.grid(column=1,row=3,padx=3,pady=5)
submit=Button(w,text='SUBMIT',command=update_st,font=('Impact',20),fg='white',bg='black').grid(column=0,row=4,columnspan=2,padx=3,pady=5)


w.mainloop()