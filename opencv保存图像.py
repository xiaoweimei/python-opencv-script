import numpy as np
import cv2

cv2.namedWindow('image',cv2.WINDOW_NORMAL)
img=cv2.imread(r"C:\Users\root\Desktop\opencv\123.jpg",1)

cv2.imshow('image',img)
cv2.imwrite('123.png',img)
