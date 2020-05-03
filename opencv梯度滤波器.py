# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv梯度滤波器
用来突出图像边界的有力工具
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg',0)


#cv2.CV_64F输出图像的深度(数据模型)，可以使用-1，与原图像保持一致np.uint8
laplacian=cv2.Laplacian(img,cv2.CV_64F)
#参数1，0为旨在x方向求一阶导数，最大可以求2阶导数
sobelx=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
#参数0，1为只在y方向求一阶导数，最大可以求2阶导数
sobely=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)

plt.subplot(2,2,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap='gray')
plt.title('Laplacian'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx,cmap='gray')
plt.title('Sobel X'),plt.xticks([]),plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobely,cmap='gray')
plt.title('Sobel Y'),plt.xticks([]),plt.yticks([])


plt.show()
