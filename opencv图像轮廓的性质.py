# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像轮廓的性质
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('1.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
#cv2.findContours三个参数，输入图像、轮廓检索模式和轮廓近似方法
#返回值有两个，第一个是轮廓，第二个是轮廓的层析结构
contours, hierarchy=cv2.findContours(thresh,1,2)
cnt=contours[0]
M=cv2.moments(cnt)
x,y,w,h=cv2.boundingRect(cnt)
#边界矩形的宽高比
aspect_ration=float(w)/h
print(aspect_ration)
#轮廓面积与边界矩形面积的比
area=cv2.contourArea(cnt)
rect_area=w*h
extent=float(area)/rect_area
print(extent)
#轮廓面积与凸包面积的比
hull=cv2.convexHull(cnt)
hull_area=cv2.contourArea(hull)
solidity=float(area)/hull_area
print(solidity)
#与轮廓面积相等的圆形的直径
equi_diameter=np.sqrt(4*area/np.pi)
print(equi_diameter)
#对象的方向，下面的方法返回长轴和短轴的长度
(dx,dy),(Ma,ma),angle=cv2.fitEllipse(cnt)
print(dx,dy)
print(Ma,ma)
print(angle)
#掩模和像素点
mask=np.zeros(imgray.shape,np.uint8)
#这里一定要使用参数-1，绘制填充的轮廓
im=cv2.drawContours(mask,[cnt],0,255,-1)
#最大值和最小值及它们的位置
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray,mask = mask)
print(min_val, max_val, min_loc, max_loc)
#平均颜色及平均灰度
mean_val = cv2.mean(imgray,mask = mask)
print(mean_val)
#对象最上面，最下面，最左边，最右边的点
leftmost = tuple(cnt[cnt[:,:,0].argmin()][0])
rightmost = tuple(cnt[cnt[:,:,0].argmax()][0])
topmost = tuple(cnt[cnt[:,:,1].argmin()][0])
bottommost = tuple(cnt[cnt[:,:,1].argmax()][0])
print(leftmost,rightmost,topmost,bottommost)


img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
plt.subplot(121),plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]]))
plt.subplot(122),plt.imshow(im)

plt.show()
