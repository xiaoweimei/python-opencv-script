# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像轮廓层次结构
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('1.jpg')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
#cv2.findContours三个参数，输入图像、轮廓检索模式和轮廓近似方法
#返回值有两个，第一个是轮廓，第二个是轮廓的层析结构

#四种轮廓层次结构
#cv2.RETR_LIST,提取所有轮廓，而不去创建任何父子关系，人人平等，属于同一级组织轮廓
#cv2.RETR_TREE,只返回最外边的轮廓，所有的子轮廓均会被忽略掉
#cv2.RETR_CCOMP,返回所有的轮廓并将轮廓分为两级组织结构
#cv2.RETR_EXTERNAL返回所有轮廓，并且创建一个完整的组织结构列表
contours, hierarchy=cv2.findContours(thresh,1,2)
cnt=contours[0]
print(hierarchy)

hull=cv2.convexHull(cnt,returnPoints=False)
defects=cv2.convexityDefects(cnt,hull)

print(ret)

