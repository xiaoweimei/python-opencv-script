# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像直方图
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('10.png',0)
#简单法绘制直方图
#使用Numpy统计直方图，Numpy中的函数np.histogram()也可以帮我们统计直方图
#hist,bins=np.histogram(img.ravel(),256,[0,256])
#plt.subplot(121)
#plt.hist(img.ravel(),256,[0,256])
#复杂法绘制直方图
img=cv2.imread('10.png')
color=('b','g','r')
#对一个列表或数组既要遍历索引又要遍历元素时
#使用内置enumerrate函数会有更加直接，优美的做法
#enumerate会将数组或列表组成一个索引序列
#使我们再获取索引和索引内容的时候更加方便
for i,col in enumerate(color):
    histr=cv2.calcHist([img],[i],None,[256],[0,256])
    #plt.subplot(122)
    plt.plot(histr,color=col)
    plt.xlim([0,256])
plt.show()

