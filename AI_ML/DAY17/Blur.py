import cv2

img=cv2.imread('4.jpg',cv2.IMREAD_COLOR)
#img.shape(3000,4000,3)


blur=cv2.GaussianBlur(img,(15,15),0)


cv2.imshow('image',blur)
cv2.waitKey(0)



cv2.destroyAllWindows()