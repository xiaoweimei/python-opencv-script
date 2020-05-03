# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中使用KNN对英文字母OCR
"""
import cv2,glob
import numpy as np
from matplotlib import pyplot as plt


data=np.loadtxt('letter-recognition.data',dtype='float32',delimiter=',',
                converters={0:lambda ch: ord(ch)-ord('A')})

#split the data to two,10000 each for train and test
train,test=np.vsplit(data,2)
#split trainData and testData to features and responses
responses,trainData=np.hsplit(train,[1])
labels,testData=np.hsplit(test,[1])

#initiate the KNN, classify,measure accuracy

knn = cv2.ml.KNearest_create()
knn.train(trainData,cv2.ml.ROW_SAMPLE,responses)
ret,result,neighbours,dist=knn.findNearest(testData,k=21)

correct=np.count_nonzero(result==labels)
accuracy=correct*100.0/10000
print(accuracy)
