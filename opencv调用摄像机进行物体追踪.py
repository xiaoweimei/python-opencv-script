# -*- coding:utf-8 -*-
"""
@author:mww
content:opencv使用摄像头进行物体跟踪
"""

import numpy as np
import cv2

cap=cv2.VideoCapture(0)

while(1):
    #获取每一帧
    ret,frame=cap.read()

    #转换到HSV
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #设定蓝色的阈值
    lower_blue=np.array([100,43,46])
    upper_blue=np.array([124,255,255])

    #根据阈值构建掩膜
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    #cv2.inRange函数会将位于两个区域内的值置为255,位于区间外的值置于0

    #对原图像和掩膜进行位运算
    res=cv2.bitwise_and(frame,frame,mask=mask)

    #显示图像
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k=cv2.waitKey(5)&0xFF#cv2.waitKey()接收时间参数毫秒数，在5毫秒内轮询用户键盘输入
    if k==27: #27对应ascill码的esc
        break
#关闭窗口
cap.release()
cv2.destroyAllWindows()

