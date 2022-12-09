import cv2
import mediapipe as mp
from cvzone.PoseModule import PoseDetector
detector = PoseDetector()
cap = cv2.VideoCapture(0)
while True:
	success, img = cap.read()
	img = detector.findPose(img)
	lmlist,bbox = detector.findPosition(img)
	cv2. imshow("Full Body",img)
	#cv2.waitKey(1)
	#Modificación para terminar el programa #
	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break
