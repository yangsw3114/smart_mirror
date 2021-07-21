from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QFrame
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QPixmap

from entity import *

import sys
import cv2
import numpy as np
import timeit
import time
import os
import copy
import threading
import mysql.connector


class faceId:
    #생성자-변수초기화
    def __init__(self, accessUser=None):
        self.accountCheck = False
        self.accessUser = accessUser
        #캠해상도
        self.cam_width = 640
        self.cam_height = 480
        #faceId_대기시간
        self.wait_time = 10
        #인식률
        self.unlockPersent = 85
        #사진촬영횟수 (장)
        self.capture_count = 100
        #사진을 저장할 공간
        self.picture = list()
        #최대 학습횟수
        self.maxTrainCount = 100
        
        self.face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            
    def faceDetector(self, frame):
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray,1.3,5)

        if faces is():
            return None
            
        for(x,y,w,h) in faces:
            cropped_face = gray[y:y+h, x:x+w]
                
        return cropped_face

    def takePicture(self, frame):
        model = cv2.face.LBPHFaceRecognizer_create()
        
        if frame is None:
            return False
        else:
            if self.faceDetector(frame) is not None:
                face = cv2.resize(self.faceDetector(frame),(200,200))
                
                if len(self.picture) < self.capture_count:
                    self.picture.append(face)
                
                try:
                    model.read("/home/pi/exe/mirror/faceIdData/" + str(self.accessUser.id) + ".yml")
                    
                except:
                    pass
                try:
                    result = model.predict(face)
                    if result[1] < 500:
                        confidence = int(100*(1-(result[1])/300))                        
                    if confidence > self.unlockPersent:
                        return True
                    else:
                        return False
                except:
                    return False
            else:
                return False
            
    def trainStart(self):
        model = cv2.face.LBPHFaceRecognizer_create()
        count = self.accessUser.trainCount
        Training_Data, Labels = [], []
        
        try:
            model.read("/home/pi/exe/mirror/faceIdData/" + str(self.accessUser.id) + ".yml")
                        
            for i, source in enumerate(self.picture):
                Training_Data.append(np.asarray(self.picture[i], dtype=np.uint8))
                Labels.append(count)
                count += 1
            
            Labels = np.asarray(Labels, dtype=np.int32)
            model.update(np.asarray(Training_Data), np.asarray(Labels))
            model.save("/home/pi/exe/mirror/faceIdData/" + self.accessUser.id + ".yml")
            
            self.trainCountInsert(count)
        except:
            return False
            
        finally:
            return True
    
    def trainFirstStart(self):
        model = cv2.face.LBPHFaceRecognizer_create()
        count = 0
        Training_Data, Labels = [], []
        
        try:                        
            for i, source in enumerate(self.picture):
                Training_Data.append(np.asarray(self.picture[i], dtype=np.uint8))
                Labels.append(count)
                count += 1
            
            Labels = np.asarray(Labels, dtype=np.int32)
            model.update(np.asarray(Training_Data), np.asarray(Labels))
            model.save("/home/pi/exe/mirror/faceIdData/" + self.accessUser.id + ".yml")
                        
            self.trainCountInsert(count)
        except:
            print("error")
            return False            
        finally:
            return True
    
    def trainCountInsert(self, count):
        if count == -1:
            os.remove("/home/pi/exe/mirror/faceIdData/" + self.accessUser.id + ".yml")
            
        conn = mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
        cursor = conn.cursor(dictionary=True)
        sql = "update mirroruser set traincount = " + str(count) + " where id = '" + self.accessUser.id + "'"
        cursor.execute(sql)
        cursor.close()
        conn.commit()
        conn.close()
    
    def cameraLiveThread(self):
        startTime = time.time()
        while self.parent().bThread:
            ret, self.parent().frame = self.camera.parent().read()
            
            if ret:
                rgb = cv2.cvtColor(self.parent().frame, cv2.COLOR_BGR2RGB)
                h, w, ch = rgb.shape
                bytesPerLine = ch * w
                img = QtGui.QImage(rgb.data, w, h, bytesPerLine, QtGui.QImage.Format_RGB888)
                resizedImg = img.scaled(self.cam_width, self.cam_height, Qt.KeepAspectRatio)
                self.parent().camlive.setPixmap(QtGui.QPixmap.fromImage(resizedImg))
            else:
                return False
                
            if time.time() - startTime >= self.parent().faceIdFuc.wait_time:
                self.parent().cameraLiveStop()
                break;  
            time.sleep(0.01)
            
    def cameraCaptureThread(self):
        while self.parent().pThread:
            check = self.takePicture(self.parent().frame)
            if check == True:
                font = QtGui.QFont()
                font.setFamily("맑은 고딕")
                font.setPointSize(20)
                font.setBold(True)
                font.setItalic(False)
                font.setUnderline(True)
                font.setWeight(50)
                font.setStrikeOut(False)
                font.setKerning(True)
                
                self.parent().loginButton.setFont(font)
                self.parent().loginButton.setText("접속하기")
                self.accountCheck = True
                self.parent().cameraLiveStop()
                break;
class faceIdUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.faceIdFuc = faceId(self.parent().accessUser)   
        self.setupUi(self)
        self.frame = None
        
    def setupUi(self, faceId):
        _translate = QtCore.QCoreApplication.translate
        
        faceId.setObjectName("faceId")
        faceId.resize(1280, 800)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(faceId)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blankTop = QtWidgets.QWidget(faceId)
        self.blankTop.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blankTop.setObjectName("blankTop")
        self.verticalLayout.addWidget(self.blankTop)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.blankLeft = QtWidgets.QWidget(faceId)
        self.blankLeft.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankLeft.setObjectName("blankLeft")
        self.horizontalLayout_2.addWidget(self.blankLeft)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.accessUserGroupbox = QtWidgets.QGroupBox(faceId)
        self.accessUserGroupbox.setMinimumSize(QtCore.QSize(350, 130))
        self.accessUserGroupbox.setMaximumSize(QtCore.QSize(450, 130))
        self.accessUserGroupbox.setTitle("")
        self.accessUserGroupbox.setCheckable(False)
        self.accessUserGroupbox.setObjectName("accessUserGroupbox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.accessUserGroupbox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.userPicture = QtWidgets.QLabel(self.accessUserGroupbox)
        self.userPicture.setMinimumSize(QtCore.QSize(0, 80))
        self.userPicture.setMaximumSize(QtCore.QSize(80, 16777215))
        self.userPicture.setFrameShape(QtWidgets.QFrame.Box)
        self.userPicture.setFrameShadow(QtWidgets.QFrame.Raised)
        self.userPicture.setObjectName("userPicture")
        self.horizontalLayout.addWidget(self.userPicture)
        
        self.userName = QtWidgets.QLabel(self.accessUserGroupbox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(100)
        font.setStrikeOut(False)
        font.setKerning(True)
        
        #사용자이름라벨#########################################################
        self.userName.setFont(font)
        self.userName.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.userName.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.userName.setFrameShadow(QtWidgets.QFrame.Plain)
        self.userName.setTextFormat(QtCore.Qt.PlainText)
        self.userName.setAlignment(QtCore.Qt.AlignCenter)
        self.userName.setWordWrap(False)
        self.userName.setIndent(-1)
        self.userName.setObjectName("userName")
        self.userName.setText(_translate("faceId",  self.parent().accessUser.name))
        self.horizontalLayout.addWidget(self.userName)
        ####################################################################
                
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.accessUserGroupbox, 0, 0, 1, 1)
        self.camliveGroupbox = QtWidgets.QGroupBox(faceId)
        self.camliveGroupbox.setMaximumSize(QtCore.QSize(395, 16777215))
        self.camliveGroupbox.setTitle("")
        self.camliveGroupbox.setObjectName("camliveGroupbox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.camliveGroupbox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 371, 571))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.camlive = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.camlive.setFrameShape(QFrame.Panel)
        self.camlive.setAlignment(QtCore.Qt.AlignCenter)
        self.camlive.setObjectName("camlive")
        self.verticalLayout_2.addWidget(self.camlive)
        
        #비밀번호로 로그인버튼###################################################
        self.loginButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 40))        
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.loginButton.setEnabled(False)
        self.verticalLayout_2.addWidget(self.loginButton)
        #버튼이벤트연결##########################################################
        self.loginButton.clicked.connect(self.loginActive)
        #########################################################################

        #뒤로가기버튼############################################################
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        #버튼이벤트연결##########################################################
        self.backButton.clicked.connect(self.userSelectActive)
        #########################################################################
        
        self.verticalLayout_2.addWidget(self.backButton)
        self.gridLayout.addWidget(self.camliveGroupbox, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.blankRight = QtWidgets.QWidget(faceId)
        self.blankRight.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankRight.setObjectName("blankRight")
        self.horizontalLayout_2.addWidget(self.blankRight)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.blankBottom = QtWidgets.QWidget(faceId)
        self.blankBottom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blankBottom.setObjectName("blankBottom")
        self.verticalLayout.addWidget(self.blankBottom)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(faceId)
        QtCore.QMetaObject.connectSlotsByName(faceId)

    def retranslateUi(self, faceId):
        _translate = QtCore.QCoreApplication.translate
        faceId.setWindowTitle(_translate("faceId", "Form"))
        self.userPicture.setText(_translate("faceId", "TextLabel"))
        self.camlive.setText(_translate("faceId", "Image"))
        self.loginButton.setText(_translate("faceId", "비밀번호로 로그인"))
        self.backButton.setText(_translate("faceId", "뒤로가기"))
        
        if self.parent().accessUser.picture != None:
            self.userPicture.setPixmap(QPixmap(self.parent().accessUser.picture))
        
    #캠라이브#############################################################
            
    def cameraLiveStart(self):
        self.camera = cv2.VideoCapture(0)
        
        if self.camera.isOpened() is False:
            return False
        else:
            self.bThread = True
            self.thread = threading.Thread(target=self.faceIdFuc.cameraLiveThread)
            
            self.pThread = True
            self.thread2 = threading.Thread(target=self.faceIdFuc.cameraCaptureThread)
            
            self.thread.start()
            self.thread2.start()
            
    def cameraLiveStop(self):        
        self.bThread = False
        self.pThread = False
        
        self.camera.release()
        
        self.loginButton.setEnabled(True)
        
    
    ###################################################################
     
    #버튼이벤트함수##########################################################    
    def loginActive(self):
        #faceid로그인실패
        if self.faceIdFuc.accountCheck == False:
            self.parent().faceIdFuc = self.faceIdFuc
            self.parent().clearUI(2)
            self.parent().stack.setCurrentIndex(2)
            
        #faceid로그인성공
        else:
            self.parent().faceIdFuc.picture.clear()
            self.parent().clearUI(3)
            self.parent().stack.setCurrentIndex(3)
        
    def userSelectActive(self):
        self.cameraLiveStop()
        self.parent().clearUI()
        self.parent().stack.setCurrentIndex(0)    
    ###################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = faceIdUI()
    sys.exit(app.exec_())    

