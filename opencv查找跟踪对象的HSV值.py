# -*- coding:utf-8 -*-
"""
@author:mww
content:opencv查找跟踪对象的HSV值
"""

import numpy as np
import cv2

green=np.uint8([[[255,0,0]]])
hsv_green=cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
print(hsv_green)
#同时互联网上也提供了BGR在HSV中的各个区间，可以搜索查看

