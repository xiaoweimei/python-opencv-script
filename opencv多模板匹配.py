# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv多模板匹配
使用模板匹配在一幅图像中查找多个目标
两个主要函数cv2.matchTemplate(),cv2.minMaxLoc()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb=cv2.imread('more_coin.png')
img_gray=cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template=cv2.imread('single_coin.png',0)
w,h=template.shape[::-1]

res=cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold=0.8

#umpy.where(condition[,x,y])
#Return elements,either from x or y,depending on condition.
#If only condition is given,return condition.nonzero().
loc=np.where(res>=threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
cv2.imwrite('res1.png',img_rgb)
