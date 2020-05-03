# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中Shi-Tomasi 焦点检测
重要函数：cv2.goodFeatureTOtrack()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,1000,0.01,10)
#返回的结果是[[311.,250.]]两层括号的数组
corners=np.int0(corners)

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),3,255,-1)

plt.imshow(img),plt.show()
#cv2.imshow('dst',img)

