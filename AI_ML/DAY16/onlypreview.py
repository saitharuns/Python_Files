import cv2

img=cv2.imread('D:/LOGINWARE/AI_ML/DAY16/3.jpg',cv2.IMREAD_COLOR)
#img.shape(3000,4000,3)
h,w=img.shape[:2]

max_w=1024
max_h=720
scale=min(max_w/w,max_h/h)
new_w=int(w*scale)
new_h=int(h*scale)

resimg=cv2.resize(img,(new_w,new_h))

cv2.imshow('image',img)
cv2.waitKey(0)



cv2.destroyAllWindows()