# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv直方图均衡化
#在训练分类器前，训练集的所有图片都要先进行直方图均衡化从而使它达到相同的亮度条件
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('junheng.png',0)
print(img)

#flatten()将数组变成一维
#hist,bins=np.histogram(img.flatten(),256,[0,256])
#计算累积分布图
#cdf=hist.cumsum()
#cdf_normalized=cdf*hist.max()/cdf.max()
#plt.subplot(121)
#plt.plot(cdf_normalized,color='b')
#plt.hist(img.flatten(),256,[0,256],color='r')
#plt.xlim([0,256])
#plt.legend(('cdf','histogram'),loc='upper left')

#equ=cv2.equalizeHist(img)
#res=np.hstack((img,equ))
#stacking images side-by-side
#plt.subplot(122)
#plt.imshow(res)
#cv2.imwrite('res.png',res)
# 自适应直方图均衡
# create a CLAHE object (Arguments are optional).
# 不知道为什么我没好到createCLAHE 这个模块
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
cv2.imwrite('clahe_2.jpg',cl1)

