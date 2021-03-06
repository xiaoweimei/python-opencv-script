# -*- coding: utf-8 -*-
"""
Created on Sun Jan 5 20:34:30 2014
@author: duan
"""
import cv2
import numpy as np
# 加载图像
img1 = cv2.imread('12.png')
img2 = cv2.imread('321.jpg')
# I want to put logo on top-left corner, So I create a ROI
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)#彩色图片转灰度
ret,mask = cv2.threshold(img2gray, 175, 255, cv2.THRESH_BINARY)#图片二值化阈值处理
mask_inv = cv2.bitwise_not(mask)#取反向
# Now black-out the area of logo in ROI
# 取roi 中与mask 中不为零的值对应的像素的值，其他值为0
# 注意这里必须有mask=mask 或者mask=mask_inv, 其中的mask= 不能忽略
img1_bg = cv2.bitwise_and(roi,img2,mask = mask)
# 取roi 中与mask_inv 中不为零的值对应的像素的值，其他值为0。
# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask_inv)
# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('123.png',img1)
cv2.imshow('12.png',img2)
cv2.imshow('res0',mask)
cv2.imshow('res1',mask_inv)
cv2.imshow('res2',img1_bg)
cv2.imshow('res3',img2_fg)
cv2.waitKey(0)
cv2.destroyAllWindows()
