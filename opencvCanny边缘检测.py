# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencvCanny边缘检测
用来突出图像边界的有力工具
步骤
1. 噪声去除
2. 计算图像梯度
3. 非极大值抑制
4. 滞后阈值
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg',0)

#下面的100和200分别为minVal和maxVal的值
#高于maxVal的边界点会被保留，低于minVal的点会被抛弃
#如果是在minVal和maxVal之间的点。会判断是否和真正的边界点相连
#相连的会被保留，反之则被丢弃，第三个参数为卷积核的大小，不填默认为3
#最后一个参数为L2gradient,可以用来设求梯度大小的方程，不写默认为False
edges=cv2.Canny(img,100,200)

plt.subplot(121),plt.imshow(img,cmap='gray')
plt.title(''),plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap='gray')
plt.title('Edge Image'),plt.xticks([]),plt.yticks([])

plt.show()
