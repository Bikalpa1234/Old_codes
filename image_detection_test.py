import cv2
import numpy as np


frameWidth =640
frameHeight=480

cap=cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,130)    #Brightness -130


myColor =[[108,130,225,255,128,255]] 

#Input colors in the format of BGR
myColorValues=[[51,153,255],[255,0,255],[0,255,0]]



def findColor(img, myColor):
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    for color in myColor:
        lower=np.array(color[0:3])
        upper=np.array(color[3:6]) 
        mask=cv2.inRange(imgHSV,lower,upper)
        cv2.imshow("img",mask)
        x,y=getcontour(mask)
        cv2.circle(iamgeResult,(x,y),10,(255,0,0),cv2.FILLED)



def getcontour(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            #cv2.drawContours(iamgeResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            x,y,w,h=cv2.boundingRect(approx)
    return x+w//2,y        


def drawCanvas(myPoints,myColorValues):
    for point in myPoints:
        cv2.circle(iamgeResult,(point[0],point[1]),10,(255,0,0),cv2.FILLED)




while True:
    success,img =cap.read()
    iamgeResult= img.copy()
    newPoints= findColor(img,myColor)
    cv2.imshow("Result",iamgeResult)
    if cv2.waitKey(1)&0xff == ord('q'):
        break
