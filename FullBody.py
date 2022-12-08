import cv2
body_classifire=cv2.CascadeClassifier("haarcascade-fullbody.xml")
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()
    gray =cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    bodies=body_classifire.detectMultiScale(gray,1.1,3)

    for (x,y,w,h) in bodies:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow("Body detection", frame)

    cv2. imshow( "body detection", frame)
    if cv2.waitKey(10)&0xFF== ord('q'):
        break
cap.release()
cv2. destroyAllWindows()