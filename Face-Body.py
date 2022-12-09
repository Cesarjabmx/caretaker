import cv2
import serial,time
import numpy as np
import mediapipe as mp
from cvzone.PoseModule import PoseDetector
from cvzone.FaceDetectionModule import FaceDetector
detector1 = FaceDetector()
detector = PoseDetector()
face_cascade= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

#fourcc= cv2.VideoWriter_fourcc(*'XVID')
ArduinoSerial=serial.Serial('/dev/cu.usbmodem14401',9600,timeout=0.1)
#out= cv2.VideoWriter('face detection4.avi',fourcc,20.0,(640,480))
time.sleep(1)


while cap.isOpened():

    #######################Deteccion de ROSTRO con haarcascade
    ret, frame= cap.read()
    frame=cv2.flip(frame,1)  #mirror the image
    #print(frame.shape)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces= face_cascade.detectMultiScale(gray,1.1,6)  #detect the face

    for x,y,w,h in faces:
        #sending coordinates to Arduino
        string='X{0:d}Y{1:d}'.format((x+w//2),(y+h//2))
        print(string)
        ArduinoSerial.write(string.encode('utf-8'))
        #plot the center of the face
        cv2.circle(frame,(x+w//2,y+h//2),2,(0,255,0),2)
        #plot the roi
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #plot the squared region in the center of the screen
    cv2.rectangle(frame,(640//2-30,480//2-30),
                 (640//2+30,480//2+30),
                  (255,255,255),3)

    #######################--------------------------------------

    #######################Deteccion de CUERPO con CVZONE
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist,bbox = detector.findPosition(img)
    #######################--------------------------------------


    #######################Deteccion de ROSTRO con CVZONE
    success1, img1 = cap.read()
    img1, bboxs = detector1.findFaces(img1)

    if bboxs:
        # bboxInfo - "id","bbox","score","center"
        center = bboxs[0]["center"]
        cv2.circle(img1, center, 5, (255, 0, 255), cv2.FILLED)

    #######################--------------------------------------

    contcat = np.concatenate((frame, img,img1), axis=0)

    #out.write(frame)
    cv2.imshow('Face-Body',contcat)

    #cv2.imwrite('output_img.jpg',frame)

    # press q to Quit
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()