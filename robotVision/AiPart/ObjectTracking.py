from collections import OrderedDict

import mediapipe as mp
from computerVision.modules import \
    HandTrackingModule,\
    FaceMeshModule,\
    FaceDetectionModule,\
    PoseModule
#from computerVision.robotVision.ComponentsPart import RoboServo1
#MyServo=RoboServo1.MyServo
#from computerVision.robotVision.ComponentsPart import ServoMotor
import cv2
import numpy as np
"""
Another code for disease detection here:
https://www.kaggle.com/medicalmlprogramming/leaf-detection-using-opencv/edit
"""
import pyfirmata
import time
print("test1")
board = pyfirmata.Arduino('COM3')
print("test2")
class TrackingClass:
    def __init__(self,n_camera):
        self.wCam,self.hCam=640,480
        self.midWCam,self.midHCam=320,240
        self.cap=cv2.VideoCapture(n_camera)
        self.face_detector=FaceMeshModule.FaceMeshDetector(maxFaces=1)
        self.hand_detector = HandTrackingModule.handDetector(maxHands=1)
        self.pose_detector = PoseModule.poseDetector()
        self.pTime=0
        self.cTime=0
    def recoring(self,option=''):
        verti_save=90
        hori_save=90
        angle_verti=90
        angle_hori=90
        servo=0
        while True:
            servo+=10
            if angle_verti<=1:
                angle_verti=1
            if angle_verti>=180:
                angle_verti=180
            if angle_hori<=1:
                angle_hori=1
            if angle_hori>=180:
                angle_hori=180
            print(int(servo/10))
            success, img=self.cap.read()
            if option=='face':
                img, object = self.face_detector.findFaceMesh( img )
                #middle=object[31]
                if len( object ) != 0:
                    hori=(np.mean([i[0] for i in object[0]]))
                    verti=np.mean([i[1] for i in object[0]])
                    hori_save=hori
                    verti_save=verti
                if len(object) == 0:
                    hori=hori_save
                    verti=verti_save
            elif option=='hand':
                img=self.hand_detector.findHands(img,draw=True)
                object=self.hand_detector.findPosition(img,draw=True)
                if len( object ) != 0:
                    hori=(np.mean([i[1] for i in object]))
                    verti=np.mean([i[2] for i in object])
                    hori_save=hori
                    verti_save=verti
                if len(object) == 0:
                    hori=hori_save
                    verti=verti_save
            if option=='pose':
                img=self.pose_detector.findPose(img,draw=True)
                object=self.pose_detector.findPosition(img,draw=True)
                if len( object ) != 0:
                    hori=(np.mean([i[1] for i in object]))
                    verti=np.mean([i[2] for i in object])
                    hori_save=hori
                    verti_save=verti
                if len(object) == 0:
                    hori=hori_save
                    verti=verti_save
            else:
                pass
            self.cTime=time.time()
            fps=1/(self.cTime-self.pTime)
            self.pTime=self.cTime
            cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
            cv2.circle(img, (self.midWCam,self.midHCam), radius=10, color=(255, 0, 0), thickness=-1)
            cv2.rectangle(img, (self.midWCam-100,self.midHCam-100), (self.midWCam+100,self.midHCam+100), color=(255, 0, 0), thickness=4)

            cv2.circle(img, (int(hori),int(verti)), radius=10, color=(255, 0, 0), thickness=-1)
            cv2.line( img, (int(hori), int(verti)), (int(self.midWCam), int(self.midHCam)), (255, 0, 0), thickness=4 )

            cv2.imshow("RoboVision",img)
            """if np.abs(hori-self.midWCam) > 100 or np.abs(verti-self.midHCam)>100:
                board.digital[13].write( 1 )
            else:
                board.digital[13].write( 0 )"""

            board.digital[10].write( 0 )
            #board.digital[8].write( 0 )
            board.digital[11].write( 0 )
            #board.digital[9].write( 0 )
            if len( object ) != 0:
                if verti>340:
                    if servo%30==0:
                        board.digital[10].write( 1 )
                        #board.digital[8].write( 0 )
                        angle_verti+=1
                        setAngle( board, 12, angle_verti )
                elif verti<140:
                    if servo%30==0:
                        board.digital[11].write( 1 )
                        #board.digital[9].write( 0 )
                        angle_verti-=1
                        setAngle( board, 12, angle_verti )

                if hori>420:
                    if servo%10==0:
                        angle_hori-=1
                        setAngle( board, 13, angle_hori )
                elif hori<220:
                    if servo%10==0:
                        angle_hori+=1
                        setAngle( board, 13, angle_hori )

            #if verti>340:

            cv2.waitKey(1)
def setAngle(board,pin,angle):
    board.digital[pin].write(angle)
    #time.sleep(0.005)#0.015
#angle=0

#Horizontal SERVO
board.digital[13].mode=pyfirmata.SERVO
setAngle( board, 13, 90 )

#Vertical SERVO
board.digital[12].mode=pyfirmata.SERVO
setAngle( board, 12, 90 )

#Vertical STEPPER
board.digital[11].mode=pyfirmata.OUTPUT
#board.digital[9].mode=pyfirmata.OUTPUT
#board.digital[8].mode=pyfirmata.OUTPUT
board.digital[10].mode=pyfirmata.OUTPUT
"""while True:
    for i in range(0, 180):
        setAngle(board,6,i)
    for i in range(0, 180,-1):
        setAngle(board,6,i)"""

tracking=TrackingClass(2)
tracking.recoring('hand')

