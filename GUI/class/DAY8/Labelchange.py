from tkinter import *

window=Tk()
window.geometry("420x480+30+0")
window.title("TONI BANK")
window.config(background="skyblue")



global lbl

def Openf():
    global lbl
    lbl=Label(window,text="OPENED",font=('Impact',20),justify='center',fg='navyblue',bg='skyblue')
    lbl.pack(expand=True)


def Closef():
   global lbl
   lbl.destroy()
   lbl=None


'''lbl= Label(window,text="CLICK THE \nBELOW BUTTON \nTO ENTER MY WORLD",font=('Impact',20),justify='center',fg='navyblue',bg='skyblue')
lbl.pack(expand=True)

'''
btn=Button(window,height=2,width=2,text='OPEN ',font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Openf)
btn.pack()
btn1=Button(window,height=2,width=2,text='CLOSE',font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Closef)
btn1.pack()

window.mainloop()