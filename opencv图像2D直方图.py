# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像2D直方图
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('10.png')
hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#opencv方法计算2D直方图
hsv1=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])
#numpy方法计算2D直方图
#h=hsv[:,:,0]
#s=hsv[:,:,1]

#hist,xbins,ybins=np.histogram2d(h.ravel(),s.ravel(),[180,256],[0,180],[0,256])
plt.subplot(121),plt.imshow(hsv,interpolation='nearest')
plt.subplot(122),plt.imshow(hsv1,interpolation='nearest')
#plt.subplot(122),plt.imshow(hist)
plt.show()
