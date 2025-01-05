from tkinter import*

window=Tk()
window.geometry('600x600')


def opn():
    top=Toplevel()  
    top.config(bg='red')



menubar=Menu(window)
window.config(menu=menubar)
file_menu=Menu(menubar,tearoff=0)
edit_menu=Menu(menubar,tearoff=0)
select_menu=Menu(menubar,tearoff=0)

menubar.add_cascade(label='File',menu=file_menu)
menubar.add_cascade(label='Edit',menu=edit_menu)


file_menu.add_command(label='Open',command=opn)

window.mainloop()