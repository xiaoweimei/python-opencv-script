"""
Created on Thu Apr 29 2020
@author:mww
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE=[255,255,255]
img1=cv2.imread('123.png')
img2=cv2.imread('12.png')

#cv2.add图像相加
#cv2.add必须保证输入的两张图片大小相同，图片类型相同，否则会报错
img3=cv2.add(img1,img2)

img4=cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()
