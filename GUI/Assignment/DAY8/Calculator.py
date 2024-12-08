from tkinter import *

w=Tk()
w.geometry('400x670+430+0')
w.config(bg='#7c99a6')
w.overrideredirect(1)


def closewin():
    w.destroy()


def button_action(val):
    dis.insert(END,val)
     

def bclear():
    value=dis.get()
    l=len(value)
    dis.delete(l-1,END)

def baclear():
    dis.delete(0,END)

def bequal():
    try:
        value=dis.get()
        res=eval(value)
        dis.delete(0,END)
        dis.insert(0,res)
    except Exception as e:
        dis.delete(0,END)
        dis.insert(0,'ERROR')


ltitle=Label(w,text="product of",bg='#7c99a6',fg='#132e1a',font=('Impact',13)).place(x=10,y=25)
ltitle=Label(w,text="TONI TECH",bg='#7c99a6',fg='#132e1a',font=('Impact',25)).place(x=10,y=50)

bclose=Button(w,text='X',border=3,width=4,height=1,font=('Impact',15),fg='white',bg='red',command=closewin).place(x=340,y=10)

dis=Entry(w,width=12,font=('Tomorrow',34),border=5,bg='#8b9e77',justify='right')
dis.place(x=13,y=100)


b7=Button(w,text='7',command=lambda: button_action(7),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=10,y=300)
b8=Button(w,text='8',command=lambda: button_action(8),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=110,y=300)
b9=Button(w,text='9',command=lambda: button_action(9),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=210,y=300)
bplus=Button(w,text='+',command=lambda: button_action('+'),border=3,width=5,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=310,y=300)

b4=Button(w,text='4',command=lambda: button_action(4),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=10,y=400)
b5=Button(w,text='5',command=lambda: button_action(5),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=110,y=400)
b6=Button(w,text='6',command=lambda: button_action(6),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=210,y=400)
bminus=Button(w,text='-',command=lambda: button_action('-'),border=3,width=5,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=310,y=400)

b1=Button(w,text='1',command= lambda: button_action(1),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=10,y=500)
b2=Button(w,text='2',command=lambda: button_action(2),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=110,y=500)
b3=Button(w,text='3',command=lambda: button_action(3),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=210,y=500)
bdiv=Button(w,text='/',command=lambda: button_action('/'),border=3,width=5,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=310,y=500)

b0=Button(w,text='0',command=lambda: button_action(0),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=10,y=600)
bd=Button(w,text='.',command=lambda: button_action('.'),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=110,y=600)
beq=Button(w,text='=',command=bequal,border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=210,y=600)
bmul=Button(w,text='X',command=lambda: button_action('*'),border=3,width=5,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=310,y=600)

bclr=Button(w,text='C',command=bclear,border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=10,y=200)
baclr=Button(w,text='AC',command=baclear,border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=110,y=200)
bbo=Button(w,text='(',command=lambda: button_action('('),border=3,width=4,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=210,y=200)
bbc=Button(w,text=')',command=lambda: button_action(')'),border=3,width=5,height=1,font=('Impact',20),fg='white',bg='#0b222b').place(x=310,y=200)

w.mainloop()




















#use before the buttons
'''def button_action(num):
    dis.insert(END,num)

#change command of symbol buttons with the below function
    
def sbutton_action(sym):
    dis.insert(END,sym)   ''' 

#insert the below function above the mainloop

'''def on_key(event):
    """Key event handler to trigger the corresponding button's action."""
    if event.char.isdigit():  # Check if the key is a digit (0-9)
        number = int(event.char)
        button_action(number)
    elif event.char.isalpha():
        None
    else:
        sym=event.char
        sbutton_action(sym)

# Bind number keys (0-9) to corresponding button actions
w.bind("<Key>", on_key)'''
