# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像轮廓凸缺陷_不同形状的匹配
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

hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)

for i in range(defects.shape[0]):
    s,e,f,d=defects[i,0]
    start=tuple(cnt[s][0])
    end=tuple(cnt[e][0])
    far=tuple(cnt[f][0])
    cv2.line(img,start,end,[0,255,0],2)
    cv2.circle(img,far,2,[0,0,255],-1)
plt.imshow(img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
#求解图像中一点到对象轮廓的最短距离，以(50，50)为例,返回值为正则在轮廓内，负在外，0在上面
#第三个参数为True时，还会计算出最短距离，为False时，只会判断点和轮廓的位置关系
dist=cv2.pointPolygonTest(cnt,(100,100),True)
print(dist)
#形状匹配
img1=cv2.imread('123.jpg',0)
img2=cv2.imread('12.png',0)
ret,thresh=cv2.threshold(img1,127,255,0)
ret,thresh2=cv2.threshold(img2,127,255,0)
contours,hierarchy=cv2.findContours(thresh,2,1)
cnt1=contours[0]
contours,hierarchy=cv2.findContours(thresh2,2,1)
cnt2=contours[0]
ret=cv2.matchShapes(cnt1,cnt2,1,0.0)
print(ret)

