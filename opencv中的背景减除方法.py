# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中的背景减除方法
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

cap=cv2.VideoCapture(0)

fgbg=cv2.createBackgroundSubtractorMOG2()

while(1):
    ret,frame=cap.read()
    fgmask=fgbg.apply(frame)

    cv2.imshow('frame',fgmask)

    k=cv2.waitKey(30)&0xff
    if k==27:
        break


cap.release()
cv2.destroyAllWindows()

