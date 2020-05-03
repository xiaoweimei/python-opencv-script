# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv分水岭图像分割
使用分水岭算法基于掩膜的图像分割
主要函数cv2.watershed()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('yingbi.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)

#noise removal
kernel=np.ones((3,3),np.uint8)
opening=cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)

#sure background area
sure_bg=cv2.dilate(opening,kernel,iterations=3)
# Finding sure foreground area
# 距离变换的基本含义是计算一个图像中非零像素点到最近的零像素点的距离，也就是到零像素点的最短距离
# 个最常见的距离变换算法就是通过连续的腐蚀操作来实现，腐蚀操作的停止条件是所有前景像素都被完全
# 腐蚀。这样根据腐蚀的先后顺序，我们就得到各个前景像素点到前景中心􅑗􂅥像素点的
# 距离。根据各个像素点的距离值，设置为不同的灰度值。这样就完成了二值图像的距离变换
#cv2.distanceTransform(src, distanceType, maskSize)
# 第二个参数0,1,2 分别表示CV_DIST_L1, CV_DIST_L2 , CV_DIST_C
dist_transform = cv2.distanceTransform(opening,1,5)
ret, sure_fg = cv2.threshold(dist_transform,0.7*dist_transform.max(),255,0)
# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg,sure_fg)
# Marker labelling
ret, markers1 = cv2.connectedComponents(sure_fg)
# Add one to all labels so that sure background is not 0, but 1
markers = markers1+1
# Now, mark the region of unknown with zero
markers[unknown==255] = 0
markers3 = cv2.watershed(img,markers)
img[markers3 == -1] = [255,0,0]

cv2.imshow('thresh',img)





kernel=np.ones((20,20),np.uint8)
#kernel作为核函数，在这里他是方形的，有时我们需要构建椭圆形/圆形的核，
#opencv函数cv2.getStructuringElement()可以实现核的形状和大小

erosion=cv2.erode(thresh,kernel,iterations=1)
plt.imshow(erosion)
plt.title("fushi"),plt.xticks([]),plt.yticks([])

plt.show()

