import cv2
import cv2.data
import time

var=cv2.VideoCapture(0)

#loads pre trained face detector
fc=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')

if not var.isOpened():
    print("unable to open camera")
else:
    while True:
        ret,frame = var.read()
        if not ret:
            print("frame detect agthailla maga")
        else:
            #convert frame to grayscale
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                                     # Scale factor is used for accuracy i.e. the distance of the detection
                                     #minNeighbours is total number of faces in the frame
                                     #minSize is the size for the minimum size
            face=fc.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
            tm=time.strftime('%H:%M:%S Date- %y/%m/%d')
            cv2.putText(frame,text=tm,fontFace=1,org=(400,430),fontScale=1.1,color=(0,255,255))

            #used for the movements of the detection rectangle
            for(x,y,w,h) in face:
                #(x,y) used for setting x and y axis (x+w,y+h) used for setting width
                #(0,255,255) used to declare the color code in (rgb) ,2
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
                cv2.putText(frame,text='SAI THARUN',fontFace=2,org=(x,y-10),fontScale=1.1,color=(0,255,255))
                cv2.putText(frame,text='Face Detected',fontFace=2,org=(30,30),fontScale=1.1,color=(0,255,255))

            cv2.imshow('press "q" to capture or "c" to cancel ',frame)
            key=cv2.waitKey(1)


            if key==ord('q'):
                
                cv2.imwrite('recog.jpg',frame)
                print("image captureed successfully")

                break
            elif key==ord('c'):
                print("Image capture canceled...")
                break
var.release()
