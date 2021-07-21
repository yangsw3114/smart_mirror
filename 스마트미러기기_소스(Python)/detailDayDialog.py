from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QListWidgetItem
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap

from entity import *
from objectDetectorDialog import *
from google.cloud import translate_v2 as translate

import os
import sys
import requests
import cv2
import threading
import time
import json

class detailDayDialog(QtWidgets.QDialog):
    def __init__(self, today=None, accessUser=None, parent=None):
        super().__init__(parent=parent)
        self.accessUser = accessUser
        self.dialog = None
        
        self.cycleCount = 3
        self.pic_item = list()
        self.cur_pic_item = list()
        self.readyItem = list()
        self.listWidgetData = list()
           
        self.OThread = False
        self.DThread = False
          
        self.today = today
        self.setupUi(self)
           
        #상태바 + 창 테두리삭제
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
          
        #다이얼로그 색 넣기
        #self.setStyleSheet('[틀래스이름(실행되는객체)]{background-color: [배경색];border: [테두리굵기]px solid [테두리색상];}')
        #self.setStyleSheet('detailDayDialog{background-color: yellow;border: 1px solid black;}')
        self.setStyleSheet("background-color:#c4e1ef;")
        
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(663, 442)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.dateEdit = QtWidgets.QDateEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        
        #날짜표시########################################################################
        self.dateEdit.setFont(font)
        self.dateEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.dateEdit.setReadOnly(True)
        self.dateEdit.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.dateEdit.setCorrectionMode(QtWidgets.QAbstractSpinBox.CorrectToNearestValue)
        self.dateEdit.setKeyboardTracking(False)
        self.dateEdit.setCalendarPopup(False)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 0, 1, 1)
        ##############################################################################
        
        self.widget_2 = QtWidgets.QWidget(self.groupBox)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 0, 1, 1, 3)
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.treeWidget.setFont(font)
        self.treeWidget.setColumnCount(3)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.headerItem().setText(2, "3")
        self.treeWidget.itemClicked.connect(self.onItemClicked)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 3)

        
        self.objectLabel2 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.objectLabel2.setFont(font)
        self.objectLabel2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.objectLabel2.setObjectName("objectLabel2")
        self.gridLayout.addWidget(self.objectLabel2, 0, 3, 1, 1)


        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.listWidget2 = QtWidgets.QListWidget(self.groupBox)
        self.listWidget2.setFont(font)
        self.listWidget2.setObjectName("listWidget2")
        self.gridLayout.addWidget(self.listWidget2, 1, 3, 1, 1)
        
        
        self.memoLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.memoLabel.setFont(font)
        self.memoLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.memoLabel.setObjectName("memoLabel")
        self.gridLayout.addWidget(self.memoLabel, 2, 0, 1, 2)
        self.objectLabel = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.objectLabel.setFont(font)
        self.objectLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.objectLabel.setObjectName("objectLabel")
        self.gridLayout.addWidget(self.objectLabel, 2, 2, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.textEdit.setFont(font)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 3, 0, 1, 2)       
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 3, 2, 1, 2)
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 4, 0, 1, 2)

        #준비물확인버튼#####################################################################
        self.checkObjectButton = QtWidgets.QPushButton(self.groupBox)
        self.checkObjectButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.checkObjectButton.setFont(font)
        self.checkObjectButton.setObjectName("checkObjectButton")
        self.gridLayout.addWidget(self.checkObjectButton, 4, 3, 1, 1)
        self.checkObjectButton.setEnabled(False)
        #버튼이벤트연결#####################################################################
        self.checkObjectButton.clicked.connect(self.ThreadStart)
        ##############################################################################
        
        #닫기버튼########################################################################
        self.cancleDetailButton = QtWidgets.QPushButton(self.groupBox)
        self.cancleDetailButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.cancleDetailButton.setFont(font)
        self.cancleDetailButton.setObjectName("cancleDetailButton")
        self.gridLayout.addWidget(self.cancleDetailButton, 4, 2, 1, 1)        
        #버튼이벤트연결#####################################################################
        self.cancleDetailButton.clicked.connect(self.detailDayExit)
        ##############################################################################
        
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
                
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "상세 일정"))
        
        self.treeWidget.headerItem().setText(0, "시작시간")
        self.treeWidget.headerItem().setText(1, "계획")
        self.treeWidget.headerItem().setText(2, "준비물")
        
        self.memoLabel.setText(_translate("Dialog", "메모"))
        self.objectLabel.setText(_translate("Dialog", "챙기지 않은 준비물"))
        self.objectLabel2.setText(_translate("Dialog", "챙긴 준비물"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Memo"))
        self.checkObjectButton.setText(_translate("Dialog", "준비물확인"))
        self.cancleDetailButton.setText(_translate("Dialog", "닫기"))
        self.dateEdit.setDate(self.today.date)
        self.parent().pr.dateEdit.setDate(self.today.date)
                
        for i in range(len(self.accessUser.detailDayList)):
            if self.accessUser.detailDayList[i].date.strftime('%Y%m%d') == self.today.date.toString('yyyyMMdd'):
                item = QTreeWidgetItem(self.treeWidget)
               
                item.setText(0, str(self.accessUser.detailDayList[i].date.strftime('%H : %M')))
                item.setText(1, str(self.accessUser.detailDayList[i].plan))
                item.setText(2, str(self.accessUser.detailDayList[i].item))
                
                item2 = QTreeWidgetItem(self.parent().pr.treeWidget)
               
                item2.setText(0, str(self.accessUser.detailDayList[i].date.strftime('%H : %M')))
                item2.setText(1, str(self.accessUser.detailDayList[i].plan))
                item2.setText(2, str(self.accessUser.detailDayList[i].item))
    
    #버튼이벤트함수###########################################################
    def onItemClicked(self, it, col):
        self.textEdit.setText(it.text(1))
        self.parent().pr.textEdit.setText(it.text(1))
        
        self.listWidgetData = list()
        self.listWidget.clear()
        self.listWidget2.clear()
        
        self.parent().pr.listWidget.clear()
        self.parent().pr.listWidget_2.clear()
        
        temp = it.text(2).split(',')
        for i in range(len(temp)):
            item = QListWidgetItem(self.listWidget)
            self.listWidgetData.append(temp[i].strip())
            item.setText(temp[i].strip())
            
            item2 = QListWidgetItem(self.parent().pr.listWidget)
            item2.setText(temp[i].strip())
            
        if len(temp) > 0:
            self.checkObjectButton.setEnabled(True)
    
    def ThreadStop(self):
        self.checkObjectButton.setEnabled(False)
        self.listWidget.clear()
        self.listWidget2.clear()
        
        self.parent().pr.listWidget.clear()
        self.parent().pr.listWidget_2.clear()
        
        self.dialog.close()
            
        for i in range(0,len(self.readyItem)):
            item = QtWidgets.QListWidgetItem(self.listWidget2)
            item.setText(self.readyItem[i])
            
            item2 = QtWidgets.QListWidgetItem(self.parent().pr.listWidget_2)
            item2.setText(self.readyItem[i])
            
        for i in range(0,len(self.listWidgetData)):
            item = QtWidgets.QListWidgetItem(self.listWidget)
            item.setText(self.listWidgetData[i])      

            item2 = QtWidgets.QListWidgetItem(self.parent().pr.listWidget)
            item2.setText(self.listWidgetData[i])   
            
    def ThreadStart(self):
        try:
            self.dialog = objectDetectorDialog(self)
            self.dialog.show()
            
            self.DThread = True
            self.thread4 = threading.Thread(target=self.objectCheckActiveThread)
            
            self.thread4.start()
        
            self.OThread = True
            self.thread3 = threading.Thread(target=self.showObjectDialogThread)
            
            self.thread3.start()
            
        except Exception as ex: # 에러 종류
            print(ex)
    
    def showObjectDialogThread(self):###################
        while self.DThread:
            if self.OThread == False:
                self.ThreadStop()
                break
                
        self.DThread = False
        
    def objectCheckActiveThread(self):#############
        import cv2
        for cycle in range(self.cycleCount):
            self.pic_item = list()
            self.cur_pic_item = list()
            self.readyItem = list()
            try: 
                try:
                    os.environ [ "GOOGLE_APPLICATION_CREDENTIALS"] = "/home/pi/exe/mirror/still-sensor-291807-41c4d1a0abf1.json"
                    client = translate.Client()
                    for i in range(len(self.listWidgetData)):
                        value = client.translate(self.listWidgetData[i], target_language='en')
                        
                        if value['translatedText'].replace(" ", "") == "tumbler":
                            self.cur_pic_item.append("bottle")
                        else:
                            self.cur_pic_item.append(value['translatedText'].replace(" ", ""))
                        
                
                    camera = cv2.VideoCapture(0)
                    
                    startTime = time.time()
                    
                    while True:
                        ret, frame = camera.read()
                        
                        if time.time() - startTime > 3:
                            break;
                    
                    
                    camera.release()                          
                    url = 'http://113.198.233.248/upload.php'
                    content = cv2.imencode('.PNG', frame)[1].tobytes()

                    files = {'myfile': content}
                    
                    response = requests.post(url, files=files)
                    json_data = json.loads(response.text)
                    
                    
                    
                    for i in range(len(json_data['detect'])):
                        self.pic_item.append(json_data['detect'][i]['item'])
                        
                        if json_data['detect'][i]['item'] in self.cur_pic_item:
                            x = int(json_data['detect'][i]['left_x'].replace(" ", ""))
                            y = int(json_data['detect'][i]['top_y'].replace(" ", ""))
                            w = int(json_data['detect'][i]['width'].replace(" ", ""))
                            h = int(json_data['detect'][i]['height'].replace(" ", ""))
                            
                            frame = cv2.rectangle(frame, (x, y), (x + h, y + w), (255, 0, 0), 2)
                                                        
                            cv2.putText(frame, json_data['detect'][i]['item'], (x+10, y+15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
                    
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    frame = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
                    h,w,c = frame.shape
                    printout = QtGui.QPixmap.fromImage(QtGui.QImage(frame.data, w, h, w*c, QtGui.QImage.Format_RGB888))
                    self.parent().pr.imagebox.setPixmap(QPixmap(printout))
                except Exception as ex:
                    print(ex)
                    self.dialog.stateLabel.setText("번역실패! 재시도중...")
                    continue
                    
                try:
                    for i in range(0, len(self.cur_pic_item)):
                        dataEn = self.cur_pic_item.pop(0)
                        dataKo = self.listWidgetData.pop(0)
                        
                        if dataEn in self.pic_item:
                            self.readyItem.append(dataKo)
                        else:
                            self.cur_pic_item.append(dataEn)
                            self.listWidgetData.append(dataKo)
                            
                    break
                    
                except Exception as ex:
                    self.dialog.stateLabel.setText("분류실패! 재시도중...")
                    continue
                    
            except Exception as ex: # 에러 종류
                print(ex)
                
        if len(self.cur_pic_item) == 0:
            self.dialog.stateLabel.setText("시도횟수 초과!")
             
        self.OThread = False
                    
        time.sleep(5)
                            
    def detailDayExit(self):
        self.parent().ui.close()
        self.close()
    ####################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = detailDayDialog()
    sys.exit(app.exec_())

