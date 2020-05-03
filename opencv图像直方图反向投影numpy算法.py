# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像直方图反向投影numpy算法
可以用于图像分割，在图像中寻找我们感兴趣的部分
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
roi=cv2.imread('12.jpg')#这个是需要查找的部分，不要和下面的大图整反了
hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target=cv2.imread('123.jpg')#这个是大图，在这个图中找上面小图的部分
hsvt=cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

#find the histograms using calcHist.can be done with np.histogram2d also
M=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
I=cv2.calcHist([hsvt],[0,1],None,[180,256],[0,180,0,256])
h,s,v=cv2.split(hsvt)

print(11111111)
print(I)
R=M/I

B=R[h.ravel(),s.ravel()]
B=np.minimum(B,1)
B=B.reshape(hsvt.shape[:2])
#现在使用一个圆盘算子做卷积，B=D*B,其中D为卷积核
disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
B=cv2.filter2D(B,-1,disc)
B=np.uint8(B)
cv2.normalize(B,B,0,255,cv2.NORM_MINMAX)

ret,thresh=cv2.threshold(B,50,255,0)
cv2.imshow('123.jpg',roi)
cv2.imshow('1234.png',target)
cv2.imshow('123jpg',thresh)
