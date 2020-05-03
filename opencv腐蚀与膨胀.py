# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv腐蚀与膨胀
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg')


#腐蚀
kernel=np.ones((5,5),np.uint8)
#kernel作为核函数，在这里他是方形的，有时我们需要构建椭圆形/圆形的核，
#opencv函数cv2.getStructuringElement()可以实现核的形状和大小

erosion=cv2.erode(img,kernel,iterations=1)
plt.subplot(331),plt.imshow(cv2.merge([erosion[:,:,2],erosion[:,:,1],erosion[:,:,0]]))
plt.title("fushi"),plt.xticks([]),plt.yticks([])

#膨胀，与腐蚀相反
dilation=cv2.dilate(img,kernel,iterations=1)
plt.subplot(332),plt.imshow(cv2.merge([dilation[:,:,2],dilation[:,:,1],dilation[:,:,0]]))

#plt.subplot(332),plt.imshow(cv2.merge([dilation[:,:,2],dilation[:,:,1],dilation[:,:,0]]))
plt.title("pengzhang"),plt.xticks([]),plt.yticks([])
#开运算，先腐蚀后膨胀,一般用来去噪
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
plt.subplot(333),plt.imshow(cv2.merge([opening[:,:,2],opening[:,:,1],opening[:,:,0]]))
plt.title("opening"),plt.xticks([]),plt.yticks([])
#闭运算，先膨胀再腐蚀，经常用来填充前景物体中的小洞，或者前景物体上的小黑点
closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
plt.subplot(334),plt.imshow(cv2.merge([closing[:,:,2],closing[:,:,1],closing[:,:,0]]))
plt.title("closing"),plt.xticks([]),plt.yticks([])
#形态学梯度，就是图像膨胀和腐蚀的差别，看上去就像前景物体的轮廓
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
plt.subplot(335),plt.imshow(cv2.merge([gradient[:,:,2],gradient[:,:,1],gradient[:,:,0]]))
plt.title("gradient"),plt.xticks([]),plt.yticks([])
#礼帽，原始图像与进行开运算之后得到的图像的差
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
plt.subplot(336),plt.imshow(cv2.merge([tophat[:,:,2],tophat[:,:,1],tophat[:,:,0]]))
plt.title("tophat"),plt.xticks([]),plt.yticks([])

#黑帽，进行闭运算之后得到的图像与原始图像的差
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)
plt.subplot(337),plt.imshow(cv2.merge([blackhat[:,:,2],blackhat[:,:,1],blackhat[:,:,0]]))
plt.title("blackhat"),plt.xticks([]),plt.yticks([])

plt.show()
