from tkinter import *




window=Tk()
window.geometry("720x420+20+40")
window.title("TONI BANK")
window.config(background="skyblue")


'''def Opened():
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

'''


def Name():
    
    #lbl['text']='SAI THARUN S' alternate method
    lbl.config(text='SAI THARUN S',fg='maroon')
    lbl.grid(column=1,row=0)

def Age():
    #lbl['text']='23'
    lbl.config(text='23',fg='yellow')
    lbl.grid(column=1,row=1)
def Dob():
    #lbl['text']='21 December 2001'
    lbl.config(text='21 December 2001',fg='navy blue')
    lbl.grid(column=1,row=2)
def Clear():
    #lbl['text']=''
    lbl.config(text='           ')
    lbl.grid(column=1,row=3)

lbl= Label(window,text="",font=('Impact',20),justify='center',fg='navyblue',bg='skyblue',width=20)
lbl.grid(column=1,row=1)

btn1=Button(window,text='click for NAME ',width=20,font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Name)
btn1.grid(column=0,row=0)
btn2=Button(window,text='click for AGE',width=20,font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Age)
btn2.grid(column=0,row=1)
btn3=Button(window,text='click for DOB',width=20,font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Dob)
btn3.grid(column=0,row=2)
btn4=Button(window,text='clear',width=20,font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Clear)
btn4.grid(column=0,row=3)


window.mainloop()