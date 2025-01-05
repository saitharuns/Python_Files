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
                print("image captureed successfully")
                count+=1
                if(count==6):
                    print("five pics captured")
                    break
            elif key==ord('c'):
                print("Image capture canceled...")
                break
    
var.release()
