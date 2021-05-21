import cv2
from tkinter import*
import winsound

cam= cv2.VideoCapture(0)

while cam.isOpened():
    ret,frame1 = cam.read()
    ret,frame2 = cam.read()
    diff =cv2.absdiff(frame1,frame2)

    gray= cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)

    blur=cv2.GaussianBlur(gray,(5,5),cv2.BORDER_DEFAULT)

    _, thresh = cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

    dilate = cv2.dilate(thresh,(7,7),iterations=3)

    contours , _ =  cv2.findContours(dilate ,cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    #cv2.drawContours(frame1 ,contours , -1, (0, 255, 0), 1)
    for c in contours:
        if cv2.contourArea(c) < 4000 :
            continue
        x,y,w,h,=cv2.boundingRect(c)
        cv2.rectangle(frame1,(x,y),(x+w , y+h),(0 ,255 ,0),2)
        winsound.Beep(700,200)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Motion Detector', frame1)
    



