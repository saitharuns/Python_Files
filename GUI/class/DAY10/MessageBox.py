from tkinter import*
from tkinter import messagebox
import time

w=Tk()
w.geometry('600x600')


def click():
    messagebox.showwarning('TONI','showing warning')
    messagebox.showerror('TONI','showing error')
    messagebox.showinfo('TONI','showing info')
    messagebox.askokcancel('TONI','showing ask or cancel')
    messagebox.askquestion('TONI','asking question')
    messagebox.askyesno('TONI','asking yes no')



btn=Button(w,text='CLICK',command=click)
btn.pack(pady=10)


w.mainloop()