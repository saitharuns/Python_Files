from tkinter import*

window=Tk()
window.geometry('600x600')



def opn():
    print()
def save():
    print()
def newf():
    print()
    

menubar=Menu(window)
window.config(menu=menubar)
file_menu=Menu(menubar,tearoff=0)
edit_menu=Menu(menubar,tearoff=0)
select_menu=Menu(menubar,tearoff=0)

menubar.add_cascade(label='File',menu=file_menu)
menubar.add_cascade(label='Edit',menu=edit_menu)


file_menu.add_cascade(label='Open',command=opn)
file_menu.add_cascade(label='New',command=newf)
file_menu.add_cascade(label='Save',command=save)
file_menu.add_separator()
file_menu.add_cascade(label='Save All')

window.mainloop()