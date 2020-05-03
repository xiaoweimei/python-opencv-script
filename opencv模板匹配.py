# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv模板匹配
使用模板匹配在一幅图像中查找目标
两个主要函数cv2.matchTemplate(),cv2.minMaxLoc()
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('123.jpg',0)
img2=img.copy()
template=cv2.imread('1234.png',0)
w,h=template.shape[::-1]

#all the methods for comparison in a list
methods=['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED','cv2.TM_CCORR',
         'cv2.TM_CCORR_NORMED','cv2.TM_SQDIFF','cv2.TM_SQDIFF_NORMED']
for meth in methods:
    img=img2.copy()

#exec语句用来执行存储在字符串或文件中的python语句，
#例如，我们可以在运行时生成一个包含Python代码的字符串，然后使用exec语句执行这些语句
#eval语句用来计算存储在字符串中的有效python表达式
    method=eval(meth)
    #apply template matching
    res=cv2.matchTemplate(img,template,method)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    #使用不同的比较方法，对结果的解释不通
    #if the method is TM_SQDIFF or TM_SQDIFF_NORMED,take minium
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left=min_loc
    else:
        top_left=max_loc
    bottom_right=(top_left[0]+w,top_left[1]+h)

    cv2.rectangle(img,top_left,bottom_right,255,2)
    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.title('Matching Result'),plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img,cmap='gray')
    plt.title('detected point'),plt.xticks([]),plt.yticks([])
    plt.suptitle(meth)

    plt.show()
