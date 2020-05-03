# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像金字塔
可用于图像融合
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg')
#函数cv2.pyrDown() 从一个高分辨率大尺寸的图像向上构建一个金子塔(尺寸变小，分辨率降低)。
lower_reso=cv2.pyrDown(cv2.pyrDown(cv2.pyrDown(img)))
#函数cv2.pyrUp() 从一个低分辨率小尺寸的图像向下构建一个金子塔(尺寸变大，但分辨率不会增加)。
higher_reso2=cv2.pyrUp(cv2.pyrUp(cv2.pyrUp(lower_reso)))

plt.subplot(221),plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]]))
plt.subplot(222),plt.imshow(cv2.merge([lower_reso[:,:,2],lower_reso[:,:,1],lower_reso[:,:,0]]))
plt.subplot(223),plt.imshow(cv2.merge([higher_reso2[:,:,2],higher_reso2[:,:,1],higher_reso2[:,:,0]]))
cv2.imwrite('222.png',lower_reso)
cv2.imwrite('2222.png',higher_reso2)
plt.show()
