# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv霍夫变换直线检测
学习如何在一张图片中检测到直线
两个主要函数cv2.HoughLines(),cv2.HoughLinesP()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('12.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)

lines=cv2.HoughLines(edges,1,np.pi/180,90)
print(lines)
for i in range(len(lines)):
    for rho,theta in lines[i]:
        a=np.cos(theta)
        b=np.sin(theta)
        x0=a*rho
        y0=b*rho
        x1=int(x0+1000*(-b))
        y1=int(y0+1000*(a))
        x2=int(x0-1000*(-b))
        y2=int(y0-1000*(a))

        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.imshow('img',img)
cv2.imshow('img1',edges)

