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




def Submit():
    name_e.insert(END,'SAI')

    #lbl['text']=name_e.get(),age_e.get(),dob_e.get()
    #name_e.delete(0,END)
    
  


name_e= Entry(window,font=('Impact',20),justify='center',fg='navyblue',bg='white',width=20)
name_e.grid(column=1,row=0,padx=2,pady=2)



btn4=Button(window,text='SUBMIT',width=20,font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Submit)
btn4.grid(column=1,row=3)

lbl= Label(window,text="",font=('Impact',20),justify='center',fg='navyblue',bg='skyblue')
lbl.grid(column=1,row=4)

window.mainloop()