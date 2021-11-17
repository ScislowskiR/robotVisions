import mediapipe as mp
from computerVision.modules import \
    HandTrackingModule,\
    FaceMeshModule,\
    FaceDetectionModule,\
    PoseModule

import cv2
import time
import numpy as np
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import serial

import sys
import socket
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk
import serial.tools.list_ports


class TrackingClass:
    def __init__(self,n_camera,track_option):
        self.wCam,self.hCam=640,480
        self.midWCam,self.midHCam=320,240
        self.cap=cv2.VideoCapture(n_camera)
        self.face_detector=FaceMeshModule.FaceMeshDetector(maxFaces=1)
        self.hand_detector = HandTrackingModule.handDetector(maxHands=1)
        self.pose_detector = PoseModule.poseDetector()
        self.pTime=0
        self.cTime=0
        self.track_option=track_option
    def recoring(self,option=''):
        while True:
            success, img=self.cap.read()
            if option=='hand':
                img=self.hand_detector.findHands(img,draw=True)
                lmList=self.hand_detector.findPosition(img,draw=True)
                if len(lmList)!=0:
                    print(lmList[4])
            elif option=='pose':
                img=self.pose_detector.findPose(img,draw=True)
                lmList=self.pose_detector.findPosition(img,draw=True)
                if len(lmList)!=0:
                    print(lmList[14])
            elif option=='face':
                img, faces = self.face_detector.findFaceMesh( img )
                if len( faces ) != 0:
                    print( faces[0] )
            else:
                pass
            self.cTime=time.time()
            fps=1/(self.cTime-self.pTime)
            self.pTime=self.cTime
            cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,
                    3, (0, 255, 0), 3)
            cv2.imshow("RoboVision",img)
            cv2.waitKey(1)

tracking=TrackingClass(1,None)
tracking.recoring('hand')
