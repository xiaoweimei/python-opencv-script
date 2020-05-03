# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中harris角点检测
重要函数：cv2.cornerHarris(),参数如下
img-数据类型为float32的输入图像
blockSize-角点检测中要考虑的邻域大小
ksize-Sobel求导中使用的窗口大小
k-Harris角点检测方程中的自由参数，取值参数为[0.04,0.06]
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg')
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.float32(img_gray)
#输入图像必须是float32,最后一个参数在0.04到005之间
dst=cv2.cornerHarris(gray,2,3,0.04)

#result is dilated for marking the corners,not important
dst=cv2.dilate(dst,None)

ret,dst=cv2.threshold(dst,0.01*dst.max(),255,0)
dst=np.uint8(dst)

ret,labels,stats,centroids=cv2.connectedComponentsWithStats(dst)
criteria=(cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER,100,0.001)
#返回值由角点坐标组成的一个数组(而非图像)
corners=cv2.cornerSubPix(gray,np.float32(centroids),(5,5),(-1,-1),criteria)

#Now draw them
res=np.hstack((centroids,corners))
#np.int0可以用来省略小数点后面的数字(非四舍五入)

res=np.int0(res)
img[res[:,1],res[:,0]]=[0,0,255]
img[res[:,3],res[:,2]]=[0,255,0]
#threshold for an optimal value,it may vary depending on the image

cv2.imshow('dst',img)

