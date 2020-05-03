# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv存储轮廓与绘制轮廓
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg')
img1=cv2.imread('1.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
#cv2.findContours三个参数，输入图像、轮廓检索模式和轮廓近似方法
#返回值有两个，第一个是轮廓，第二个是轮廓的层析结构
contours, hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(contours)
print(hierarchy)
#img=cv2.drawContours(img,contours,-1,(0,255,0),3)
img=cv2.drawContours(img1,contours,-1,(0,0,255),1)
cv2.imshow('lunkuo',img)
