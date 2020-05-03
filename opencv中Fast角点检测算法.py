# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中Fast角点检测算法
5. 关键点匹配
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg',0)

#initiate fast object with default values
fast=cv2.FastFeatureDetector_create(threshold=40,nonmaxSuppression=False,type=cv2.FAST_FEATURE_DETECTOR_TYPE_9_16)#获取FAST角点探测器


kp=fast.detect(img,None)#描述符

img = cv2.drawKeypoints(img,kp,img,color=(255,0,0))#画到img上面

print ("Threshold: ", fast.getThreshold())#输出阈值
print ("nonmaxSuppression: ", fast.getNonmaxSuppression())#是否使用非极大值抑制
print ("Total Keypoints with nonmaxSuppression: ", len(kp))#特征点个数

plt.imshow(img)
plt.show()
