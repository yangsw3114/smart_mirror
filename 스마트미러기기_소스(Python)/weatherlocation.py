import sys
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
from time import sleep

import re
import mysql.connector


class weatherlocation(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#c4e1ef;")
        self.setupUi(self)
        self.X = None
        self.Y = None
        self.location = None
        #타이틀바삭제 + 창테두리삭제
        #self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
    def setupUi(self, weatherlocationUI):
        weatherlocationUI.setObjectName("weatherlocationUI")
        weatherlocationUI.resize(646, 361)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(weatherlocationUI)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(weatherlocationUI)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout.addWidget(self.widget_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(weatherlocationUI)
        self.widget.setMaximumSize(QtCore.QSize(20, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(weatherlocationUI)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        
        #확인버튼###########################################################
        self.setButton = QtWidgets.QPushButton(self.groupBox)
        self.setButton.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.setButton.setFont(font)
        self.setButton.setObjectName("setButton")
        self.gridLayout.addWidget(self.setButton, 0, 3, 2, 1)
        #버튼이벤트연결#########################################################
        self.setButton.clicked.connect(self.check_location)
        ###################################################################
        self.third = QtWidgets.QComboBox(self.groupBox)
        self.third.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.third.setFont(font)
        self.third.setObjectName("third")
        #Third콤보박스
        self.third.currentTextChanged.connect(self.onThirdChange)
        
        
        self.gridLayout.addWidget(self.third, 0, 2, 1, 1)
        self.second = QtWidgets.QComboBox(self.groupBox)
        self.second.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.second.setFont(font)
        self.second.setObjectName("second")        
        #Second콤보박스
        self.second.currentTextChanged.connect(self.onSecondChange)
        
        
        
        self.gridLayout.addWidget(self.second, 0, 1, 1, 1)
        self.first = QtWidgets.QComboBox(self.groupBox)
        self.first.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.first.setFont(font)
        self.first.setObjectName("first")        
        #First콤보박스
        self.first.currentTextChanged.connect(self.onFirstChange)
        
        
        self.gridLayout.addWidget(self.first, 0, 0, 1, 1)
        self.past = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.past.setFont(font)
        self.past.setAlignment(QtCore.Qt.AlignCenter)
        self.past.setObjectName("past")
        self.gridLayout.addWidget(self.past, 2, 0, 1, 4)
        self.total = QtWidgets.QLineEdit(self.groupBox)
        self.total.setMinimumSize(QtCore.QSize(0, 30))
        #확인버튼###########################################################
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(11)
        self.total.setFont(font)
        self.total.setObjectName("total")
        self.gridLayout.addWidget(self.total, 1, 0, 1, 3)
        self.cancleButton = QtWidgets.QPushButton(self.groupBox)
        self.cancleButton.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancleButton.setFont(font)
        self.cancleButton.setObjectName("cancleButton")
        #버튼이벤트연결#####################################################
        self.cancleButton.clicked.connect(self.Cancel)
        ####################################################################
        self.gridLayout.addWidget(self.cancleButton, 3, 0, 1, 4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.widget_2 = QtWidgets.QWidget(weatherlocationUI)
        self.widget_2.setMaximumSize(QtCore.QSize(20, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.widget_4 = QtWidgets.QWidget(weatherlocationUI)
        self.widget_4.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout.addWidget(self.widget_4)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(weatherlocationUI)
        QtCore.QMetaObject.connectSlotsByName(weatherlocationUI)

    def retranslateUi(self, weatherlocationUI):
        _translate = QtCore.QCoreApplication.translate
        weatherlocationUI.setWindowTitle(_translate("weatherlocationUI", "상세 날씨"))
        self.setButton.setText(_translate("weatherlocationUI", "설정"))
        self.past.setText(_translate("weatherlocationUI", self.parent().loc))
        self.cancleButton.setText(_translate("weatherlocationUI", "취소"))

        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
        curs=conn.cursor(dictionary=True)
        sql = "select first from gps where second is null and third is null"
        curs.execute(sql)
            
        for row in curs:
            self.first.addItem(row["first"])
            
        curs.close()
        conn.close()
    #버튼이벤트함수##############################################################
    def onFirstChange(self):
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")

        curs=conn.cursor(dictionary=True)

        self.second.clear()
        sql = "select distinct second from gps where first = '" + self.first.currentText() + "' and second is not null"
        
        curs.execute(sql)
        for row in curs:
            self.second.addItem(row["second"])
        
        curs.close()
        conn.close()
        
        self.total.setText(self.first.currentText())
    def onSecondChange(self): 
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")

        curs=conn.cursor(dictionary=True)
        
        self.third.clear()
        sql = "select distinct third from gps where first = '" + self.first.currentText() + "' and second = '" + self.second.currentText() + "' and third is not null"
            
        curs.execute(sql)
        
        for row in curs:
            self.third.addItem(row["third"])
        
        curs.close()
        conn.close()
        
        self.total.setText(self.first.currentText() + " " + self.second.currentText())
        
    def onThirdChange(self):
        self.total.setText(self.first.currentText() + " " + self.second.currentText() + " " + self.third.currentText())
                
    def check_location(self):
        try:
            TEXT = list()
            
            if self.first.currentText() != "":
                TEXT.append(self.first.currentText())
            if self.second.currentText() != "":
                TEXT.append(self.second.currentText())
            if self.third.currentText() != "":
                TEXT.append(self.third.currentText())
                        
            conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")

            curs=conn.cursor(dictionary=True)
            
            if len(TEXT) == 1:
                sql = "select first, pointX, pointY from gps where first = '" + TEXT[0] + "' and second is null and third is null"
                
                curs.execute(sql)
                
                for row in curs:
                    self.location = row["first"]
                    self.X = row["pointX"]
                    self.Y = row["pointY"]
                
            elif len(TEXT) == 2:
                sql = "select first, second, pointX, pointY from gps where first = '" + TEXT[0] + "' and second = '" + TEXT[1] + "' and third is null"
                
                curs.execute(sql)
                
                for row in curs:
                    self.location = row["first"] + row["second"]
                    self.X = row["pointX"]
                    self.Y = row["pointY"]
                
            elif len(TEXT) == 3:
                sql = "select first, second, third, pointX, pointY from gps where first = '" + TEXT[0] + "' and second = '" + TEXT[1] + "' and third = '" + TEXT[2] + "'"
                
                curs.execute(sql)
                
                for row in curs:
                    self.location = row["first"] + " " + row["second"] + " " + row["third"]
                    self.X = row["pointX"]
                    self.Y = row["pointY"]
          
            curs.close()
            conn.close()
            
            self.parent().loc = self.location
            self.parent().nx = self.X
            self.parent().ny = self.X
            self.parent().location.setText(self.location)
            
            self.close()
        except Exception as ex:
            print(ex)
            
    def Cancel(self):
        self.close()
    ###################################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weatherlocationUI = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(weatherlocationUI)
    weatherlocationUI.show()
    sys.exit(app.exec_())
