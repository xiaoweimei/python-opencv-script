# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像直方图反向投影opencv算法
可以用于图像分割，在图像中寻找我们感兴趣的部分
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
roi=cv2.imread('12.jpg')#这个是需要查找的部分，不要和下面的大图整反了
hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

#target is the image we search in
target=cv2.imread('123.jpg')#这个是大图，在这个图中找上面小图的部分
hsvt=cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

#find the histograms using calcHist.can be done with np.histogram2d also
roihist=cv2.calcHist([hsv],[0,1],None,[180,256],[0,180,0,256])

#normalize histogram and apply backprojection
#归一化：原始图像，结果图像，映射到结果图像中的最小值，最大值，归一化类型
#cv2.NORM_MINMAX对数组的所有值进行转化，使它们线性映射到最小值和最大值之间
#归一化之后的直方图便于显示，归一化之后就成了0到255之间的数了
cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
dst=cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)
#now convolute with circular disc
disc=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
dst=cv2.filter2D(dst,-1,disc)
#threshold and binary AND
ret,thresh=cv2.threshold(dst,50,255,0)
#别忘了是三通道图像，因此这里使用merge变成了3通道
thresh=cv2.merge((thresh,thresh,thresh))
thresh_env=cv2.bitwise_not(thresh)#取反向
#thresh_env=cv2.merge((thresh_env,thresh_env,thresh_env))
#按位操作
res=cv2.bitwise_and(target,thresh)
res_env=cv2.bitwise_and(target,thresh_env)

res=np.hstack((target,thresh,res))
res_env=np.hstack((target,thresh_env,res_env))
cv2.imwrite('res.jpg',res)

cv2.imshow('123jpg',res_env)
