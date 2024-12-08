from tkinter import *




window=Tk()
window.geometry("420x480")
window.title("TONI BANK")
window.config(background="skyblue")

def Opened():
    lbl['text']='FILE OPENED'
   
def Nfile():
    lbl['text']='NEW FILE'

menu=Menu(window)
window.config(menu=menu)
fmenu=Menu(menu)
emenu=Menu(menu)


menu.add_cascade(label='File',menu=fmenu)
menu.add_cascade(label='Edit',menu=emenu)

fmenu.add_cascade(label='Open',command=Opened)
fmenu.add_cascade(label='New', command=Nfile)
fmenu.add_cascade(label='Save')
fmenu.add_separator()
fmenu.add_cascade(label='Save All')



lbl= Label(window,text="CLICK THE \nBELOW BUTTON \nTO ENTER MY WORLD",font=('Impact',20),justify='center',fg='navyblue',bg='skyblue')
lbl.pack(expand=True)

def Openf():
    lbl['text']='FILE IS OPENED'

def Closef():
    lbl['text']='FILE IS CLOSED'

btn=Button(window,text='OPEN ',font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Openf)
btn.pack()
btn1=Button(window,text='CLOSE',font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Closef)
btn1.pack()

window.mainloop()
