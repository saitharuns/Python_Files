import sqlite3
from tkinter import *
from tkinter import messagebox

w=Tk()
w.geometry('500x500+400+80')
w.config(bg='light blue')
w.overrideredirect(1)

def database():
    global conn,cursor
    conn = sqlite3.connect("BIT.db")
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS STUDENT_DATA("NAME" VARCHAR(20),"MOBILE" LONGINT(10),"MAIL" VARCHAR(20))')
    cursor.execute('CREATE TABLE IF NOT EXISTS STAFF_DATA("NAME" VARCHAR(20),"MOBILE" LONGINT(10),"MAIL" VARCHAR(20))')
    conn.commit()
    
def stdata():
    stop=Toplevel(w)
    stop.config(bg='pink')
    stop.geometry('500x500+400+80')
    stop.overrideredirect(1)
    

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

    hlbl=Label(stop,text='STUDENT DATA',font=('Impact',25),bg='pink').grid(column=0,row=0,padx=3,pady=5,columnspan=2)
    nm=Label(stop,text='NAME',font=('Impact',20),bg='pink').grid(column=0,row=1,padx=3,pady=5)
    name=Entry(stop,width=20,textvariable=ST_NAME,font=('Impact',20))
    name.grid(column=1,row=1,padx=3,pady=5)
    mob=Label(stop,text='MOBILE',font=('Impact',20),bg='pink').grid(column=0,row=2,padx=3,pady=5)
    mobile=Entry(stop,width=20,textvariable=ST_MOBILE,font=('Impact',20))
    mobile.grid(column=1,row=2,padx=3,pady=5)
    mailid=Label(stop,text='MAIL',font=('Impact',20),bg='pink').grid(column=0,row=3,padx=3,pady=5)
    mail=Entry(stop,width=20,textvariable=ST_MAIL,font=('Impact',20))
    mail.grid(column=1,row=3,padx=3,pady=5)
    submit=Button(stop,text='SUBMIT',command=update_st,font=('Impact',20),fg='white',bg='black',width=10).grid(column=0,row=4,padx=3,pady=5)
    ext=Button(stop,text='BACK',command=stop.destroy,font=('Impact',20),fg='white',bg='black',width=10).grid(column=1,row=4,columnspan=2,padx=3,pady=5)



#STAFF DATA INSERTION

def stfdata():
    stf=Toplevel(w)
    stf.config(bg='light yellow')
    stf.geometry('500x500+400+80')
    stf.overrideredirect(1)
    

    def update_stf():
        database()
        if messagebox.askyesno('DB','DO YOU LIKE TO JOIN'):
            cursor.execute("INSERT INTO `STAFF_DATA` (name,mobile,mail) VALUES(?, ?, ?)",(str(STF_NAME.get()),int(STF_MOBILE.get()),str(STF_MAIL.get())))
            name.delete(0,END)
            mobile.delete(0,END)
            mail.delete(0,END)
            messagebox.showinfo('DB','VALUE INSERTED')
            conn.commit()
            cursor.close()
            update_stf()
        else:
            update_stf()
            messagebox.showinfo('DB','VALUE NOT INSERTED')



    STF_NAME=StringVar()
    STF_MOBILE=StringVar()
    STF_MAIL=StringVar()

    hlbl=Label(stf,text='STAFF DATA',font=('Impact',25),bg='light yellow').grid(column=0,row=0,padx=3,pady=5,columnspan=2)
    nm=Label(stf,text='NAME',font=('Impact',20),bg='light yellow').grid(column=0,row=1,padx=3,pady=5)
    name=Entry(stf,width=20,textvariable=STF_NAME,font=('Impact',20))
    name.grid(column=1,row=1,padx=3,pady=5)
    mob=Label(stf,text='MOBILE',font=('Impact',20),bg='light yellow').grid(column=0,row=2,padx=3,pady=5)
    mobile=Entry(stf,width=20,textvariable=STF_MOBILE,font=('Impact',20))
    mobile.grid(column=1,row=2,padx=3,pady=5)
    mailid=Label(stf,text='MAIL',font=('Impact',20),bg='light yellow').grid(column=0,row=3,padx=3,pady=5)
    mail=Entry(stf,width=20,textvariable=STF_MAIL,font=('Impact',20))
    mail.grid(column=1,row=3,padx=3,pady=5)
    submit=Button(stf,text='SUBMIT',command=update_stf,font=('Impact',20),fg='white',bg='black',width=10).grid(column=0,row=4,padx=3,pady=5)
    ext=Button(stf,text='BACK',command=stf.destroy,font=('Impact',20),fg='white',bg='black',width=10).grid(column=1,row=4,columnspan=2,padx=3,pady=5)



lbl=Label(w,text='',font=('Impact',25),bg='light blue' ,fg='black').pack(pady=10)
lbl=Label(w,text='TONI DATABASE ',font=('Impact',25),bg='light blue' ,fg='black').pack(pady=20)
stubtn=Button(w,text='STUDENT DATA',font=('Impact',20),bg='black' ,fg='white',width=20,command=stdata).pack(pady=10)
stfbtn=Button(w,text='STAFF DATA',font=('Impact',20),bg='black' ,fg='white',width=20,command=stfdata).pack(pady=10)
exitbtn=Button(w,text='EXIT',font=('Impact',20),bg='black' ,fg='white',width=20,command=w.destroy).pack(pady=10)
w.mainloop()