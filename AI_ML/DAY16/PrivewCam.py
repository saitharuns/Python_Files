import cv2

var=cv2.VideoCapture(0)



global count
count=1

if not var.isOpened():
    print("unable to open camera")
else:
    while True:
        ret,frame = var.read()
        if not ret:
            print("frame detect agthailla maga")
        else:
            cv2.imshow('press "q" to capture or "c" to cancel ',frame)
            key=cv2.waitKey(1)

            if key==ord('q'):
                fname=str(count)+'.jpg'
                cv2.imwrite(fname,frame)
                cv2.imshow(fname,frame)
                print("image captureed successfully")
                #this wait key is used to hold the preview
                #cv2.waitKey(0)
                count+=1
            elif key==ord('c'):
                print("Image capture canceled...")
                break
    
var.release()
