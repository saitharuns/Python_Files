import cv2
from tkinter import*

var=cv2.VideoCapture(0)


root=Tk()
root.geometry('500x500')



def camera():

    if not var.isOpened():
        print("unable to open camera")
    else:
        ret,frame = var.read()
        if not ret:
            print("frame detect agthailla maga")
        else:
            
            cv2.imwrite('mypic.jpg',frame)
            print("image captureed successfully")
    var.release()

ret,frame=var.read()
capture=Button(root,text='CAPTURE',command=camera).pack()
cancel=Button(root,text='CANCEL',command=root.destroy)
cancel.pack()

root.mainloop()