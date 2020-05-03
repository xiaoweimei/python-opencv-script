# -*- coding:utf-8 -*-
"""
@author:mww
content:opencv颜色空间转换
"""

import numpy as np
import cv2

flags=[i for i in dir(cv2) if i.startswith('COLOR_')]
print(flags)
#cv2.cvtColor(input_image,flag),打印出所有可用的flag
