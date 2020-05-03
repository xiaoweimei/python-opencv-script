# -*- coding:utf-8 -*-
"""
@author:mww
"""

import numpy as np
import cv2

# Create a black image
img=np.zeros((512,512,3),np.uint8)

# Draw a diagonal blue line with thickness of 5px
cv2.line(img,(0,0),(511,511),(255,0,0),5)#画线
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)#画矩形
cv2.circle(img,(447,63),63,(0,0,255),-1)#画圆,-1是填充圆，1是只有边界
cv2.ellipse(img,(256,256),(100,50),0,0,270,255,-1)#画椭圆

pts=np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)#画多边形
pts=pts.reshape((-1,1,2))
#这里reshape的第一个参数为-1，表名这一维的长度是根据后面的维度的计算粗来的

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV',(10,450),font,4,(200,5,255),5)

winname='example'
cv2.namedWindow(winname)
cv2.imshow(winname,img)
cv2.waitKey(0)
cv2.destroyWindow(winname)
