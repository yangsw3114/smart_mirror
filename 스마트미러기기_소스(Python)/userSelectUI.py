import sys
from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QPixmap

class userSelectUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)

    def setupUi(self, userSelect):
        _translate = QtCore.QCoreApplication.translate
        userSelect.setObjectName("userSelect")
        userSelect.resize(1280, 800)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(userSelect)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blankTop = QtWidgets.QWidget(userSelect)
        self.blankTop.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blankTop.setObjectName("blankTop")
        self.verticalLayout.addWidget(self.blankTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blankLeft = QtWidgets.QWidget(userSelect)
        self.blankLeft.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankLeft.setObjectName("blankLeft")
        self.horizontalLayout.addWidget(self.blankLeft)
        self.userList = QtWidgets.QGridLayout()
        self.userList.setObjectName("userList")
        
        #Grid Layout배치를 위한 카운트 변수
        lineCount = -1      #세로
        Count = 0           #가로
        
        for i in range(len(self.parent().userList)):        
            accessUserGroupbox_2 = QtWidgets.QGroupBox(userSelect)
            accessUserGroupbox_2.setMinimumSize(QtCore.QSize(0, 0))
            accessUserGroupbox_2.setMaximumSize(QtCore.QSize(500, 120))
            accessUserGroupbox_2.setTitle("")
            accessUserGroupbox_2.setCheckable(False)
            accessUserGroupbox_2.setObjectName("accessUserGroupbox_2")
            
            layoutWidget = QtWidgets.QWidget(accessUserGroupbox_2)
            layoutWidget.setGeometry(QtCore.QRect(10, 10, 481, 92))
            layoutWidget.setObjectName("layoutWidget")
            
            horizontalLayout_3 = QtWidgets.QHBoxLayout(layoutWidget)
            horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
            horizontalLayout_3.setObjectName("horizontalLayout_3")
            userPicture_2 = QtWidgets.QLabel(layoutWidget)
            userPicture_2.setMinimumSize(QtCore.QSize(0, 80))
            userPicture_2.setMaximumSize(QtCore.QSize(80, 16777215))
            userPicture_2.setFrameShape(QtWidgets.QFrame.Box)
            userPicture_2.setFrameShadow(QtWidgets.QFrame.Raised)
            userPicture_2.setObjectName("userPicture_2")
            userPicture_2.setText(_translate("userSelect", "Image"))
            
            if self.parent().userList[i].picture != None:
                userPicture_2.setPixmap(QPixmap(self.parent().userList[i].picture))
            
            horizontalLayout_3.addWidget(userPicture_2)
            userName_2 = QtWidgets.QLabel(layoutWidget)
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(20)
            font.setBold(False)
            font.setItalic(False)
            font.setUnderline(False)
            font.setWeight(50)
            font.setStrikeOut(False)
            font.setKerning(True)
            userName_2.setFont(font)
            userName_2.setLayoutDirection(QtCore.Qt.LeftToRight)
            userName_2.setFrameShape(QtWidgets.QFrame.NoFrame)
            userName_2.setFrameShadow(QtWidgets.QFrame.Plain)
            userName_2.setTextFormat(QtCore.Qt.PlainText)
            userName_2.setAlignment(QtCore.Qt.AlignCenter)
            userName_2.setWordWrap(False)
            userName_2.setIndent(-1)
            userName_2.setObjectName("userName_2")
            userName_2.setText(_translate("userSelect", self.parent().userList[i].name))
            horizontalLayout_3.addWidget(userName_2)
            #접속버튼#######################################################
            accessButton = QtWidgets.QPushButton(layoutWidget)
            accessButton.setMinimumSize(QtCore.QSize(0, 90))
            accessButton.setMaximumSize(QtCore.QSize(90, 16777215))
            #클릭이벤트연결####################################################
            accessButton.clicked.connect(self.faceIdActive)
            #############################################################
            
            font = QtGui.QFont()
            font.setFamily("맑은 고딕")
            font.setPointSize(14)
            font.setBold(False)
            font.setWeight(50)
            accessButton.setFont(font)
            accessButton.setObjectName(str(i))
            accessButton.setText(_translate("userSelect", "접속"))
            horizontalLayout_3.addWidget(accessButton)
            
            if i % 5 == 0:
                lineCount = lineCount + 1
                Count = 0
            self.userList.addWidget(accessUserGroupbox_2, Count, lineCount, 1, 1)
            
            Count = Count + 1
        
        self.horizontalLayout.addLayout(self.userList)
        self.blankRight = QtWidgets.QWidget(userSelect)
        self.blankRight.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankRight.setObjectName("blankRight")
        self.horizontalLayout.addWidget(self.blankRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.blankBottom = QtWidgets.QWidget(userSelect)
        self.blankBottom.setMaximumSize(QtCore.QSize(16777215, 20))
        self.blankBottom.setObjectName("blankBottom")
        self.verticalLayout.addWidget(self.blankBottom)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(userSelect)
        QtCore.QMetaObject.connectSlotsByName(userSelect)

    def retranslateUi(self, userSelect):
        _translate = QtCore.QCoreApplication.translate
        userSelect.setWindowTitle(_translate("userSelect", "Form"))
           
    #버튼이벤트함수###########################################################
    def faceIdActive(self):
        btn = self.sender()     
        self.parent().accessUser = self.parent().userList[int(btn.objectName())]
        
        self.parent().clearUI(1)        
        self.parent().stack.itemAt(1).widget().cameraLiveStart()
        self.parent().stack.setCurrentIndex(1)
    ####################################################################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = userSelectUI()
    sys.exit(app.exec_())
