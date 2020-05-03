# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv霍夫变换查找圆形(环)
学习如何在一张图片中检测到圆
主要函数cv2.HoughCircles()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('yuan.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,300,
param1=100,param2=60,minRadius=0,maxRadius=0)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
# draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

