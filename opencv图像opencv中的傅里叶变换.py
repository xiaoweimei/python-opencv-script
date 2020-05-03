# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像opencv中的傅里叶变换
opencv中相应的函数是cv2.dft()和cv2.idft(),都是双通道的。
第一个通道是结果的实数部分，第二个通道是结果的虚数部分
输入图像要首先转换成np.float32格式
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

#roi is the object or region of object we need to find
img=cv2.imread('123.jpg',0)
dft=cv2.dft(np.float32(img),flags=cv2.DFT_COMPLEX_OUTPUT)
dft_shift=np.fft.fftshift(dft)

magnitude_spectrum=20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

rows,cols=img.shape
crow,ccol=rows//2,cols//2

#create a mask firs,center square is 1,remaining all zeros
mask=np.zeros((rows,cols,2),np.uint8)
mask[crow-30:crow+30,ccol-30:ccol+30]=1
#apply mask and inverse DFT
fshift=dft_shift*mask
f_ishift=np.fft.ifftshift(fshift)
img_back=cv2.idft(f_ishift)
img_back=cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(221),plt.imshow(img,cmap='gray')
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(magnitude_spectrum)
plt.title('magnitude spectrum'),plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(img,cmap='gray')
plt.title('input image'),plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(img_back,cmap='gray')
plt.title('magnitude spectrum'),plt.xticks([]),plt.yticks([])
plt.show()
