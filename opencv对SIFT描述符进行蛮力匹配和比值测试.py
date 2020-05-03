# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv对SIFT描述符进行蛮力匹配和比值测试
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


queryImage=cv2.imread('123.jpg',0)
trainingImage=cv2.imread('me.jpg',0)


# 只使用SIFT 或 SURF 检测角点
sift = cv2.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)
# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)
# Apply ratio test
# 比值测试，首先获取与A 距离最近的点B（最近）和C（次近），只有当B/C
# 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为0
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])
# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good[:10],flags=2)
plt.imshow(img3),plt.show()
