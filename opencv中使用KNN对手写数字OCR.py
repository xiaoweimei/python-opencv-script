# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:37:28 2020
@author: mww
content:opencv中使用KNN对手写数字OCR
"""
import cv2,glob
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('shuzisample.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Now wo split the image to 5000 cells,each 20*20 size

cells=[np.hsplit(row,100) for row in np.vsplit(gray,50)]

#Make it into a Numpy array.It size will be (50,100,20,20)
x=np.array(cells)

#now we prepare train_data and test_data
train=x[:,:50].reshape(-1,400).astype(np.float32)
test=x[:,50:100].reshape(-1,400).astype(np.float32)

#create labels for train and test data
k=np.arange(10)
train_labels=np.repeat(k,250)[:,np.newaxis]
test_labels=train_labels.copy()

knn = cv2.ml.KNearest_create()
knn.train(train,cv2.ml.ROW_SAMPLE,train_labels)
ret,result,neighbours,dist = knn.findNearest(test,k=5)
# Now we check the accuracy of classification
# For that, compare the result with test_labels and check which are wrong
matches = result==test_labels
correct = np.count_nonzero(matches)
accuracy = correct*100.0/result.size
print (accuracy)
np.savez('knn_data.npz',train=train, train_labels=train_labels)#将结果数据保存起来

