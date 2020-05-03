"""
Created on Thu Apr 29 2020
@author:mww
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE=[255,255,255]
img1=cv2.imread('123.png')

replicate=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

#matplotlib是rgb空间，opencv是bgr空间
plt.subplot(231),plt.imshow(cv2.merge([img1[:,:,2],img1[:,:,1],img1[:,:,0]]),'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(cv2.merge([constant[:,:,2],constant[:,:,1],constant[:,:,0]]),'gray'),plt.title('CONSTANT')

plt.show()
