# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中k近邻算法
"""
import cv2,glob
import numpy as np
from matplotlib import pyplot as plt


# Feature:设置为25行2列的包含（x,y)的已知的训练数据
trainData = np.random.randint(0, 100, (100, 2)).astype(np.float32)
# print(trainData)
# labels:设置为0:代表Red， 1：代表Blue
labels = np.random.randint(0, 2, (100, 1)).astype(np.float32)
# print(labels)
 
# 找出红色并绘制
# print(labels.ravel())
red = trainData[labels.ravel() == 0]    # ravel()降维
plt.scatter(red[:, 0], red[:, 1], 80, 'r', '^')  # 绘制三角散点图
# 找出蓝色并绘制
blue = trainData[labels.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 's')
 
 
# 测试数据被标记为绿色
'''
返回值包括：
1、由KNN算法计算得到的测试数据的类别标志0或1，
如果想要使用最近邻算法，只需将k置为1。
2、k个最近邻居的类别标志。
3、每个最近邻居到测试数据的距离
'''
newcomer = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(newcomer[:, 0], newcomer[:, 1], 80, 'g', 'o')
knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, labels)
 
ret, results, neighbours, dist = knn.findNearest(newcomer, 100)
 
print("result: ", results, "\n")
print("neighbours: ", neighbours, "\n")
print("distance: ", dist)
plt.show()



