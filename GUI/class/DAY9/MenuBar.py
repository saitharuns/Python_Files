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


file_menu.add_command(label='Open',command=opn)
file_menu.add_command(label='New',command=newf)
file_menu.add_command(label='Save',command=save)
file_menu.add_separator()
file_menu.add_command(label='Exit',command=window.destroy)

edit_menu.add_command(label='Undo')
edit_menu.add_command(label='Redo')
edit_menu.add_command(label='Cut')
edit_menu.add_command(label='Copy')
edit_menu.add_command(label='Paste')
edit_menu.add_separator()
edit_menu.add_command(label='Find and Replace')







window.mainloop()