# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中ORB算法
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg',0)


# Initiate STAR detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img,kp,img,color=(0,255,0), flags=0)
plt.imshow(img2),plt.show()
