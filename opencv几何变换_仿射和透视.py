# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv几何变换_仿射和透视
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg')
rows,cols,ch=img.shape
#仿射变换
pts1=np.float32([[50,50],[200,50],[50,200]])#选中的三个基准点
pts2=np.float32([[10,100],[200,50],[100,250]])#拉伸到指定区域即为仿射

M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(cols,rows))

#透视变换
pts3=np.float32([[40,40],[250,40],[40,373],[250,373]])#选中的四个基准点
pts4=np.float32([[0,0],[cols,0],[0,rows],[cols*2,rows]])#拉伸到指定区域即为透视
MM=cv2.getPerspectiveTransform(pts3,pts4)
dstt=cv2.warpPerspective(img,MM,(cols,rows))

plt.subplot(221),plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]])),plt.title("Input image")
plt.subplot(222),plt.imshow(cv2.merge([dst[:,:,2],dst[:,:,1],dst[:,:,0]])),plt.title("Output image")
plt.subplot(223),plt.imshow(cv2.merge([dstt[:,:,2],dstt[:,:,1],dstt[:,:,0]])),plt.title("Inpt image")

plt.show()
