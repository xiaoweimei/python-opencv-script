# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencvGrabCut算法提取图像前景
创建一个交互是程序完成前景提取
GrabCut算法原理，主要函数cv2.grabCit()
参数：1.输入图像 2.掩膜图像 3.包含前景的背景 4.算法内部使用的数组
5.算法的迭代次数 6. 确定我们进行修改的方式，矩形模式还是掩膜模式
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('messi.jpeg')
mask=np.zeros(img.shape[:2],np.uint8)
newmask=cv2.imread('messi_mask.jpg',0)
mask[newmask==0]==0
mask[newmask==255]=1

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)

rect=(100,20,450,350)
#函数的返回值是更新的mask,bgdModel,fgdModel
mask,bgdModel,fgdModel=cv2.grabCut(img,mask,None,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_MASK)

mask=np.where((mask==2)|(mask==0),0,1).astype('uint8')

img=img*mask[:,:,np.newaxis]

cv2.imshow('mask',mask)
plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]]))
plt.show()

