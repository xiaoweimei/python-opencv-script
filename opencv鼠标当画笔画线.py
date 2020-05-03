"""
@author:mww
"""
import cv2
import numpy as np
# mouse callback function

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)#打印出来所有事件

drawing=False
mode=True
ix,iy=-1,-1
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode
    #当按下左键是返回起始位置坐标
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    #当鼠标左键按下并移动绘制图形，event可以查看移动，flag查看是否按下
    elif event==cv2.EVENT_MOUSEMOVE and flags==cv2.EVENT_FLAG_LBUTTON:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                #绘制圆圈，小圆点连在一起就成了线，3代表了笔画的粗细
                cv2.circle(img,(x,y),3,(0,0,255),-1)
                #下面注释掉的代码是起始点为圆心，起点到终点为半径的圆
                #r=int(np.sqrt((x-ix)**2+(y-iy)**2))
                #cv2.circle(img,(x,y),r,(0,0,255),-1)
    #当鼠标松开停止绘画
    elif event==cv2.EVENT_LBUTTONUP:
        drawing==False

#创建图像与窗口并将窗口与回调函数绑定

img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    k=cv2.waitKey(20)&0xFF#按q键退出ord('q')=113
    if k==ord('m'):#更改模式，画线画矩形模式
        mode=not mode
    elif k==113:
        break
cv2.destroyAllWindows()

