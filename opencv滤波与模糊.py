# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv平均滤波器
#使用cv.filter2D()对一幅图像进行卷积操作
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg')
kernel=np.ones((10,10),np.float32)/100
#cv.Filter2D(src,dst,kernel,anchor=(-1,-1))
#depth -desired depth of the destination image
#if it is negative,it will be the same as src.depth()
#the following combinations of src.depth() and ddepth are supported
#src.depth()=CV_8U,ddepth=-1/CV_165/CV_32F/CV_64F
#src.depth()=CV_16U/CV_16S, ddepth=-1/CV_32F/CV_64F
#src.depth()=CV_32S, ddepth=-1/CV_32F/CV_64F
#src.depth()=CV_64F, ddepth=-1/CV_64F
#when ddepth=-1, the output image will have the same depth as the source
dst=cv2.filter2D(img,-1,kernel)

plt.subplot(231),plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]]))
plt.title("Original"),plt.xticks([]),plt.yticks([])
plt.subplot(232),plt.imshow(cv2.merge([dst[:,:,2],dst[:,:,1],dst[:,:,0]]))
plt.title("Average"),plt.xticks([]),plt.yticks([])

#平均模糊
blur=cv2.blur(img,(20,20))
plt.subplot(233),plt.imshow(cv2.merge([blur[:,:,2],blur[:,:,1],blur[:,:,0]]))
plt.title("Average big"),plt.xticks([]),plt.yticks([])
#高斯模糊
blurgass=cv2.GaussianBlur(img,(11,11),0)
plt.subplot(234),plt.imshow(cv2.merge([blurgass[:,:,2],blurgass[:,:,1],blurgass[:,:,0]]))
plt.title("Gaussian filter"),plt.xticks([]),plt.yticks([])
#中值模糊
blurmedian=cv2.medianBlur(img,31)
plt.subplot(235),plt.imshow(cv2.merge([blurmedian[:,:,2],blurmedian[:,:,1],blurmedian[:,:,0]]))
plt.title("median filter"),plt.xticks([]),plt.yticks([])
#双边模糊,保留边界
#9 邻域直径，两个75分别是空间高斯函数标准差，灰度值相似性高斯函数标准差
blurtwo=cv2.bilateralFilter(img,9,150,15)
plt.subplot(236),plt.imshow(cv2.merge([blurtwo[:,:,2],blurtwo[:,:,1],blurtwo[:,:,0]]))
plt.title("shuangbian filter"),plt.xticks([]),plt.yticks([])
plt.show()
