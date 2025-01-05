import cv2
import time
from gtts import gTTS
import os

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    print("Unable to open the camera")
else:
    fourcc=cv2.VideoWriter_fourcc(*'mp4v')
    out=cv2.VideoWriter('captured_Video.mp4',fourcc,30.0,(640,480))

    while True:
        ret,frame=cap.read()

        if not ret:
            print("Frame not detected.")
            break
        
        tm='SAI THARUN S'
        tts=gTTS(text=tm,lang='en')
        tts.save("op.mp3")
        os.system("start op.mp3")          
        cv2.putText(frame,text=tm,fontFace=1,org=(400,430),fontScale=1.1,color=(0,255,255))
        cv2.imshow('Video Capture',frame)
        out.write(frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    out.release()

cap.release()
cv2.destroyAllWindows()

    
            