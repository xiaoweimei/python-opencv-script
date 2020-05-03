import numpy as np
import cv2

img=cv2.imread(r"C:\Users\root\Desktop\opencv\123.jpg",1)
print(img.shape)#获取图像尺寸信息
print(img.item(10,10,2))
print(img.size)#返回像素总数
print(img.dtype)#返回图像的数据类型
face=img[100:200,100:290]

zeros=np.zeros(img.shape[:2],dtype="uint8")
cv2.imshow('face',face)#切割图片并显示
img.itemset((10,10,2),100)
print(img.item(10,10,2))
#cv2.split() 是一个比较耗时的操作。只有真正需要时才用它，能用Numpy 索引就尽量用。
b,g,r=cv2.split(img)
#cv2.imshow('b',b)#图片单通道显示
#cv2.imshow('g',g)#图片单通道显示
#cv2.imshow('r',r)#图片单通道显示

blueimg=cv2.merge([b,zeros,zeros])#opencv中的通道顺序为bgr,无论如何不能记错
greenimg=cv2.merge([zeros,g,zeros])
redimg=cv2.merge([zeros,zeros,r])

cv2.imshow('b',blueimg)#图片单通道显示
cv2.imshow('g',greenimg)#图片单通道显示
cv2.imshow('r',redimg)#图片单通道显示

bgrimg=cv2.merge([b,g,r])
cv2.imshow('bgr',bgrimg)#图片三通道合并，展示原图

img[:,:,2]=255#将红通道变为0
img[:,:,1]=0#将绿通道变为0
#img[:,:,0]=0

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
