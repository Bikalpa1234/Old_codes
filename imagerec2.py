#Contour Detection
import cv2
import numpy as np


def getcontour(img):
    contours,hierarchy=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(imgContour,cnt,-1,(255,0,0),3)
            peri=cv2.arcLength(cnt,True)
            print(peri)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            print(len(approx))
            objCor=len(approx)
            x,y,w,h=cv2.boundingRect(approx)
            if objCor==3 : objectType="Tri"
            else:objectType="None"
            

            cv2.rectangle(imgContour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgContour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,100,255),2)





shapes=cv2.imread('C:\\Users\\DELL\\OneDrive\\Desktop\\Code\\shapes.png')
imgContour=shapes.copy()

#converting it to gray scale
imgGray=cv2.cvtColor(shapes,cv2.COLOR_BGR2GRAY)
imgBlur= cv2.GaussianBlur(imgGray,(7,7),2)

#Detection of the edges
imgCany= cv2.Canny(imgBlur,50,50)
getcontour(imgCany)
imgBlank= np.zeros_like(shapes)

cv2.imshow("Shapes",shapes)
cv2.imshow("Grey",imgGray)
cv2.imshow("Blur",imgBlur)
cv2.imshow("Cany",imgCany)
cv2.imshow("Blank",imgBlank)
cv2.imshow("Img-Contour",imgContour)
cv2.waitKey(0)
