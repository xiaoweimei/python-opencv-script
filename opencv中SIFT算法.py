# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中SIFT算法
重要特征：harris焦点检测的旋转不变特性，此次介绍的是
SIFT尺度不变特征变换
SIFT算法主要由四步构成，
1. 尺度空间极值检测
2. 关键点(极值点)定位
3. 为关键点(极值点)指定方向参数
4. 关键点描述符
5. 关键点匹配
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

sift=cv2.xfeatures2d.SIFT_create()
kp=sift.detect(gray,None)

img=cv2.drawKeypoints(gray,kp)

cv2.imshow('111',img)


