# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv几何变换
"""
import cv2
import numpy as np
#opencv提供两个变换函数，cv2.wrapAffine和cv2.wrapPerspective，使用这两个函数
#你可以实现所有类型的变换，cv2.wrapAffine接收的参数是2*3的变换矩阵，
#cv2.wrapPerspective接收的参数是3*3的变换矩阵

img=cv2.imread('123.jpg')
#下面的None本应该是输出图像的尺寸，但是因为后边我们设置了缩放因子，因此这里为None
#这里呢，我们直接设置输出图像的尺寸，所以不用设置缩放因子
height,width=img.shape[:2]
bigres=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_LINEAR)
smallres=cv2.resize(img,(width//2,height//2),interpolation=cv2.INTER_AREA)
#缩放因子，缩放时推荐cv2.INTER_AREA,扩展时推荐cv2.INTER_CUBIC(慢)和cv2.INTER_LINEAR(快)
#默认情况下改变图像尺寸大小的插值方法均为cv2.INTER_LINEAR
cv2.imshow('img',img)
cv2.imshow('big',bigres)
cv2.imshow('small',smallres)
cv2.imwrite('smallimg.jpg',smallres)

#cv2.destroyAllWindows()
