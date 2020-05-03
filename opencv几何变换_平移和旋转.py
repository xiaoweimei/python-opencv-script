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
img=cv2.imread('123.jpg',0)


rows,cols=img.shape

#定义平移矩阵
M=np.float32([[1,0,88],[0,1,88]])
#M=[[1,0,88
    #[0,1,88]]
#指向x正方向移动88个像素点，向y正方向移动88个像素点
m_dst=cv2.warpAffine(img,M,(cols*2,rows*2))
#这里的第一个参数为旋转中心，第二个为旋转角度，第三个为旋转后的缩放因子
#这里可以通过设置旋转中心，缩放因子，以及窗口大小来防止旋转后超出边界的问题

R=cv2.getRotationMatrix2D((cols/2,rows/2),10,0.8)#定义旋转矩阵
print(M,R)

#第三个参数是输出图像的尺寸中心
r_dst=cv2.warpAffine(img,R,(cols,rows))

cv2.imshow('img',img)
cv2.imshow('m_dst',m_dst)
cv2.imshow('r_dst',r_dst)
#cv2.imshow('small',smallres)
#cv2.imwrite('smallimg.jpg',smallres)

#cv2.destroyAllWindows()
