import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img=cv2.imread(r"C:\Users\root\Desktop\opencv\123.jpg",1)

cv2.imshow('image',img)


k=cv2.waitKey(0)&0xFF
if k==ord('q'):
    cv2.destroyAllWindows()
else:
    cv2.imwrite('123.png',img)
    cv2.destroyAllWindows()
