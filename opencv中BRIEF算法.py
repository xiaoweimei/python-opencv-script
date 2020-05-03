# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中BRIEF算法
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('123.jpg')


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Initiate FAST detector
star = cv2.xfeatures2d.StarDetector_create()
# Initiate BRIEF extractor
biref = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = star.detect(gray, None)
kp, des = biref.compute(gray, kp)
print(biref.descriptorSize())
print(des.shape)

cv2.namedWindow('img',cv2.WINDOW_AUTOSIZE)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
