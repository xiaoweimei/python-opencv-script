# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv获取图像轮廓的矩
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
img=cv2.drawContours(img,contours,-1,(0,0,255),3)
cnt=contours[0]
M=cv2.moments(cnt)
#M即为图像的矩，根据矩，我们可以计算出图像的重心坐标
cx=int(M['m10']/M['m00'])
cy=int(M['m01']/M['m00'])
print(cnt,M)#打印出图像的矩
print(cx,cy)#打印出图像的重心坐标
area=cv2.contourArea(cnt)#计算轮廓面积
print(M['m00'])#打印出图像的轮廓面积
print(area)#打印出图像的轮廓面积
perimeter=cv2.arcLength(cnt,True)#轮廓的弧长，True代表形状是闭合的，False代表形状是打开的
k=cv2.isContourConvex(cnt)#检测轮廓曲线是不是凸的，只返回True或者False
print(k)
print(perimeter)
x,y,w,h = cv2.boundingRect(cnt)#边界矩形
img1 = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
plt.subplot(231),plt.imshow(cv2.merge([img[:,:,2],img[:,:,1],img[:,:,0]]))
plt.subplot(232),plt.imshow(img1)
(x,y),radius = cv2.minEnclosingCircle(cnt)
#最小外接圆
center = (int(x),int(y))
radius = int(radius)
img2 = cv2.circle(img,center,radius,(0,255,0),2)
plt.subplot(233),plt.imshow(img2)
#椭圆拟合
ellipse = cv2.fitEllipse(cnt)
img3= cv2.ellipse(img,ellipse,(0,255,0),2)
plt.subplot(234),plt.imshow(img3)
#直线拟合
rows,cols = img.shape[:2]
[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img4 = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)
plt.subplot(235),plt.imshow(img4)
plt.show()
