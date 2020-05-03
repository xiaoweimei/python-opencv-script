# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv掩膜构建局部区域直方图
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('10.png',0)

mask=np.zeros(img.shape[:2],np.uint8)
mask[500:2000,500:1000]=255
masked_img=cv2.bitwise_and(img,img,mask=mask)

#Calculate histogram with mask and without mask
#Check third argument for mask
hist_full=cv2.calcHist([img],[0],None,[256],[0,256])
hist_mask=cv2.calcHist([img],[0],mask,[256],[0,256])

plt.subplot(221),plt.imshow(img,'gray')
plt.subplot(222),plt.imshow(mask,'gray')
plt.subplot(223),plt.imshow(masked_img,'gray')
plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)

plt.show()

