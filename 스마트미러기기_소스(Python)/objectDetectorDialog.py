import sys
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QMovie
           
class objectDetectorDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#c4e1ef;")
        self.setupUi(self)
        
        #타이틀바삭제 + 창테두리삭제
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
    def setupUi(self, objectDetectorDialog):
        objectDetectorDialog.setObjectName("objectDetectorDialog")
        objectDetectorDialog.resize(200, 270)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(objectDetectorDialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gifImage = QtWidgets.QLabel(objectDetectorDialog)
        self.gifImage.setAlignment(QtCore.Qt.AlignCenter)
        self.gifImage.setObjectName("gifImage")
        self.verticalLayout.addWidget(self.gifImage)
        
        self.stateLabel = QtWidgets.QLabel(objectDetectorDialog)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(30)
        font.setStrikeOut(False)
        self.stateLabel.setFont(font)
        self.stateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.stateLabel.setObjectName("stateLabel")
        self.verticalLayout.addWidget(self.stateLabel)
        
        self.blank = QtWidgets.QWidget(objectDetectorDialog)
        self.blank.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blank.setObjectName("blank")
        self.verticalLayout.addWidget(self.blank)
                
        
        #음성인식호출버튼#########################################################
        self.cancleButton = QtWidgets.QPushButton(objectDetectorDialog)
        self.cancleButton.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.cancleButton.setFont(font)
        self.cancleButton.setObjectName("cancleButton")
        #버튼이벤트연결###########################################################
        self.cancleButton.clicked.connect(self.callSttExit)
        ####################################################################
        
        self.verticalLayout.addWidget(self.cancleButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(objectDetectorDialog)
        QtCore.QMetaObject.connectSlotsByName(objectDetectorDialog)

    def retranslateUi(self, objectDetectorDialog):
        _translate = QtCore.QCoreApplication.translate
        objectDetectorDialog.setWindowTitle(_translate("objectDetectorDialog", "Dialog"))
        self.gifImage.setText(_translate("objectDetectorDialog", "TextLabel"))
        self.stateLabel.setText(_translate("objectDetectorDialog", "Loading..."))
        self.cancleButton.setText(_translate("objectDetectorDialog", "확인취소"))
        self.icon = QMovie("/home/pi/exe/mirror/system_Icon/search.gif")
        self.gifImage.setMovie(self.icon)
        self.icon.start()

    #버튼이벤트함수###########################################################
    def callSttExit(self):
        self.parent().OThread = False
        self.reject()
    ####################################################################

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = objectDetectorDialog()
    sys.exit(app.exec_())

