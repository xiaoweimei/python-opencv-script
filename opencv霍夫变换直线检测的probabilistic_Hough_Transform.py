# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv霍夫变换直线检测的probabilistic_Hough_Transform
学习如何在一张图片中检测到直线
两个主要函数cv2.HoughLines(),cv2.HoughLinesP()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('12.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,50,150,apertureSize=3)
minLineLength=3000#线的最小长度
maxLineGap=100#两条线之间的最大间隔，小于10将会被当一条线处理

lines=cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
print(lines)
for i in range(len(lines)):
    for x1,y1,x2,y2 in lines[i]:
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.imshow('img',img)
cv2.imshow('img1',edges)

