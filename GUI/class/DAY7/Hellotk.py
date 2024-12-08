from tkinter import *




window=Tk()
window.geometry("420x480")
window.title("TONI BANK")
window.config(background="skyblue")
'''mb1=Label(window,text="File",font=('Impact',16),fg='black',bg='grey')
mb1.grid(column=0,row=0)

mb2=Label(window,text="Edit",font=('Impact',16),fg='black',bg='grey')
mb2.grid(column=1,row=0)
mb3=Label(window,text="Seletion",font=('Impact',16),fg='black',bg='grey')
mb3.grid(column=2,row=0)'''






lbl= Label(window,text="SAI THARUN S\nTHALAPATHY\nVIJAY\nTONI",font=('Impact',20),justify='left',fg='navyblue',bg='skyblue')
lbl.pack(expand=True)

def Click():
    
    print("clicked..........")

btn=Button(window,text='HELLO',font=('Impact',20,'italic'),justify='right',fg='navyblue',bg='khaki',command=Click)
btn.pack(side='top')

window.mainloop()
