# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像numpy中的傅里叶变换
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
img=cv2.imread('123.jpg',0)
f=np.fft.fft2(img)
fshift=np.fft.fftshift(f)
ffshift=np.fft.fftshift(f)
#这里构建振幅图的公式没学过
magnitude_spectrum=20*np.log(np.abs(fshift))

rows,cols=img.shape
crow,ccol=rows//2,cols//2
ffshift[crow-30:crow+30,ccol-30:ccol+30]=0
f_ishift=np.fft.ifftshift(ffshift)
img_back=np.fft.ifft2(f_ishift)
#取绝对值
img_back=np.abs(img_back)

plt.subplot(221),plt.imshow(img,cmap='gray')
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum,cmap='gray')
plt.title('magnitude_spectrum'),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(img_back,cmap='gray')
plt.title('image after HPF'),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(img_back)
plt.title('Result in JET'),plt.xticks([]),plt.yticks([])
plt.show()
