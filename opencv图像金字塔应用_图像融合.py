# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 20:34:30 2020
@author: mww
content:opencv图像金字塔应用_图像融合
可用于图像融合
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

A=cv2.imread('123.jpg')
B=cv2.imread('321.jpg')

def sameSize(img1, img2):
    """
    使得img1的大小与img2相同
    """
    rows1, cols1, dpt1 = img1.shape
    rows2, cols2, dpt2 = img2.shape
    dst = img1[:min(rows1,rows2),:min(cols1,cols2)]
    return dst

#generate Gaussian pyramid for A
G=A.copy()
gpA=[G]
for i in range(6):
    G=cv2.pyrDown(G)
    gpA.append(G)

#generate Gaussian pyramid for B
G=B.copy()
gpB=[G]
for i in range(6):
    G=cv2.pyrDown(G)
    gpB.append(G)

#generate Laplacian pyramid for A
lpA=[gpA[5]]
gpC=[G]
for i in range(5,0,-1):
    GE=cv2.pyrUp(gpA[i])
    L=cv2.subtract(sameSize(gpA[i-1],GE),sameSize(GE,gpA[i-1]))
    print(222222)
    lpA.append(L)

#generate Laplacian pyramid for B
lpB=[gpB[5]]
gpC=[G]
for i in range(5,0,-1):
    GE=cv2.pyrUp(gpB[i])
    L=cv2.subtract(sameSize(gpB[i-1],GE),sameSize(GE,gpB[i-1]))
    lpB.append(L)

#Now add left and right halves of images in each level
#numpy.hstack(up)
#Take a sequency of arrays and stack them horizontally
#to make a single array
LS=[]
for la,lb in zip(lpA,lpB):
    rows,cols,dpt=la.shape
    ls=np.hstack((la[:,:cols//2],lb[:,cols//2:]))
    LS.append(ls)
#now reconstruct
ls_=LS[0]
for i in range(1,6):
    ls_=cv2.pyrUp(ls_)
    print(ls_.shape,LS[i].shape)
    ls_=cv2.add(sameSize(ls_,LS[i]),sameSize(LS[i],ls_))
# image with direct connecting each half

real=np.hstack((A[:,:cols//2],B[:,cols//2:]))


plt.subplot(121),plt.imshow(cv2.merge([ls_[:,:,2],ls_[:,:,1],ls_[:,:,0]]))
plt.subplot(122),plt.imshow(cv2.merge([real[:,:,2],real[:,:,1],real[:,:,0]]))

plt.show()
