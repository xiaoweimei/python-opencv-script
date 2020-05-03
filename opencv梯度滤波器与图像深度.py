# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv梯度滤波器与图像深度
用来突出图像边界的有力工具
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg',0)

#Output dtype=cv2.CV_8U
sobelx8u=cv2.Sobel(img,cv2.CV_8U,1,0,ksize=5)
#也可以将参数设为-1
#sobelx8u=cv2.Sobel(img,-1,1,0,ksize=5)

# Output dtype=cv2.CV_64F. Then take its absolute and convert to cv2.CV_8U
sobelx64f=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
abs_sobel64f=np.absolute(sobelx64f)
sobel_8u=np.uint(abs_sobel64f)



plt.subplot(1,3,1),plt.imshow(img,cmap='gray')
plt.title('Original'),plt.xticks([]),plt.yticks([])
plt.subplot(1,3,2),plt.imshow(sobelx8u,cmap='gray')
plt.title('Sobel CV_8U'),plt.xticks([]),plt.yticks([])
plt.subplot(1,3,3),plt.imshow(sobel_8u,cmap='gray')
plt.title('Sobel abs(CV_64F)'),plt.xticks([]),plt.yticks([])



plt.show()
