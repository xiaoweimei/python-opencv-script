# -*- coding:utf-8 -*-
"""
@author:mww
"""

import numpy as np
import cv2

#cv2.setUseOptimized(False)#关闭优化
img1=cv2.imread("12.png")

#cv2.getTickCount函数返回参考点到这个函数被执行的时钟数
e1=cv2.getTickCount()
#your code execution
for i in range(5,200,2):
    img1=cv2.medianBlur(img1,i)#中值滤波
e2=cv2.getTickCount()
#cv2.getTickFrequency返回时钟频率
time=(e2-e1)/cv2.getTickFrequency()
#time即为程序运行的时间，为多少多少秒
print(time)
print(cv2.useOptimized())#查看函数优化是否被开启
