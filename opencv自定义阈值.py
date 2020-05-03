# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv自定义阈值
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("123.jpg",0)

#中值滤波
img=cv2.medianBlur(img,5)
ret,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
#11为Block size,2 为常数C值

th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

th3=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)


titles=['original image','global thresholding(v=127)',
        'adaptive mean thresholding','adaptive gaussian thresholding']
images=[img,th1,th2,th3]

for i in range(4):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
