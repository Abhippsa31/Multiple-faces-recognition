import cv2
import numpy as np
face=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('haarcascade_eye.xml')

def face_detection(image):
    
    
    if ret is True:
        gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        
        faces=face.detectMultiScale(gray,1.6,7)
        
        for(x,y,w,h) in faces:
        
          cv2.rectangle(image,(x,y),(x+w,y+h),(127,0,255),3)
        
          roi_color=image[y:y+h,x:x+w]
          roi_gray= gray[y:y+h,x:x+w]
        
          eyes=eye.detectMultiScale(roi_gray)
        
          for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,255,0),3)
    return image
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow('face_detection',face_detection(frame))
    
    if cv2.waitKey(1)==13:
        break
cap.release()
cv2.destroyAllWindows()
    
        
                   
            
        