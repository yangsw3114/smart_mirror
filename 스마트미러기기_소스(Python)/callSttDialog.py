from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QMovie
import time

import sys

class callStt:
    def __init__(self):
        pass
        

class callSttDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#c4e1ef;")
        self.setupUi(self)
        
        #타이틀바삭제 + 창테두리삭제
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
    def setupUi(self, callSttUI):
        callSttUI.setObjectName("callSttUI")
        callSttUI.resize(200, 270)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(callSttUI)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gifImage = QtWidgets.QLabel(callSttUI)
        self.gifImage.setAlignment(QtCore.Qt.AlignCenter)
        self.gifImage.setObjectName("gifImage")
        
        self.verticalLayout.addWidget(self.gifImage)
        self.blank = QtWidgets.QWidget(callSttUI)
        self.blank.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blank.setObjectName("blank")
        self.verticalLayout.addWidget(self.blank)
        
        
        self.listenLabel = QtWidgets.QLabel(callSttUI)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.listenLabel.setFont(font)
        self.listenLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.listenLabel.setObjectName("listenLabel")
        self.verticalLayout.addWidget(self.listenLabel)
        
        self.blank2 = QtWidgets.QWidget(callSttUI)
        self.blank2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blank2.setObjectName("blank")
        self.verticalLayout.addWidget(self.blank2)
        
        #음성인식호출버튼#########################################################
        self.cancleButton = QtWidgets.QPushButton(callSttUI)
        self.cancleButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.cancleButton.setFont(font)
        self.cancleButton.setObjectName("cancleButton")
        #버튼이벤트연결###########################################################
        self.cancleButton.clicked.connect(self.CancleButton)
        ####################################################################
        
        self.verticalLayout.addWidget(self.cancleButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(callSttUI)
        QtCore.QMetaObject.connectSlotsByName(callSttUI)

    def retranslateUi(self, callSttUI):
        _translate = QtCore.QCoreApplication.translate
        callSttUI.setWindowTitle(_translate("callSttUI", "Dialog"))
        self.gifImage.setText(_translate("callSttUI", "TextLabel"))
        self.listenLabel.setText(_translate("callSttUI", ""))
        self.cancleButton.setText(_translate("callSttUI", "호출취소"))
        self.icon = QMovie("/home/pi/exe/mirror/system_Icon/stt.gif")
        self.gifImage.setMovie(self.icon)
        self.icon.start()

    #버튼이벤트함수###########################################################
    def CancleButton(self):
        self.parent().stop = False
        self.parent().DThread = False
        self.parent().OThread = False
                
        self.close()
    ####################################################################
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = callSttDialog()
    sys.exit(app.exec_())

