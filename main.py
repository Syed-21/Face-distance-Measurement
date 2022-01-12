import cv2
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from pygame import mixer
import time
# cap=cv2.VideoCapture("http://192.168.10.4:4747/video")
cap=cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=2)
mixer.init()
mixer.music.load('sound.mp3')
while True:
    sucess , img = cap.read()
    img,faces=detector.findFaceMesh(img)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
        # cv2.circle(img,pointLeft,5,(255,0,255),cv2.FILLED)
        # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
        w,_ = detector.findDistance(pointLeft,pointRight)
        W=6.3
        f = 840
        d=(W*f)/w
        # print(d)
        cvzone.putTextRect(img,f'Distance:{int(d)}cm',(face[10][0]-75,face[10][1]-50),scale = 2  )
        if d < 50:
            mixer.music.play(start=6)
            time.sleep(0.2)
        else:
            mixer.music.stop()

    cv2.imshow("frame",img)
    cv2.waitKey(1)
