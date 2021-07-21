from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

from findAccountDialog import *
from entity import *

import sys
import mysql.connector

class login:
    def __init__(self, accessUser=None):
        self.accessUser = accessUser
    
    def dbIdPwCheck(self, pw):
        dbPw = None
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
        cursor = conn.cursor(dictionary=True)
        sql = "select pw from mirroruser where id = '" + self.accessUser.id  + "'" 
        cursor.execute(sql)
        
        for row in cursor:
            dbPw = row["pw"]
            
        cursor.close()
        conn.close()
                
        if dbPw == pw:
            return True
        else:
            return False

class loginUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.loginFuc = login(self.parent().accessUser)
        self.dialog = None
        self.setupUi(self)
        
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(1280, 800)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(login)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blankTop = QtWidgets.QWidget(login)
        self.blankTop.setObjectName("blankTop")
        self.verticalLayout.addWidget(self.blankTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blankLeft = QtWidgets.QWidget(login)
        self.blankLeft.setMinimumSize(QtCore.QSize(0, 0))
        self.blankLeft.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.blankLeft.setObjectName("blankLeft")
        self.horizontalLayout.addWidget(self.blankLeft)
        self.loginGroupbox = QtWidgets.QGroupBox(login)
        self.loginGroupbox.setMinimumSize(QtCore.QSize(565, 257))
        self.loginGroupbox.setFlat(False)
        self.loginGroupbox.setCheckable(False)
        self.loginGroupbox.setObjectName("loginGroupbox")
        self.layoutWidget = QtWidgets.QWidget(self.loginGroupbox)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 501, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(self.layoutWidget)
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 10))
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 2, 0, 1, 4)
        self.loginButton = QtWidgets.QPushButton(self.layoutWidget)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 85))
        #로그인버튼########################################################
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.loginButton.setFont(font)
        self.loginButton.setObjectName("loginButton")
        self.gridLayout.addWidget(self.loginButton, 0, 3, 2, 1)        
        self.userNameLabel = QtWidgets.QLabel(self.layoutWidget)
        #버튼이벤트연결######################################################
        self.loginButton.clicked.connect(self.userCheck)
        #################################################################
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.userNameLabel.setFont(font)
        self.userNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userNameLabel.setObjectName("userNameLabel")
        self.gridLayout.addWidget(self.userNameLabel, 0, 0, 1, 1)
        self.userNameEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.userNameEdit.setText(self.parent().accessUser.name)
        self.userNameEdit.setReadOnly(True)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.userNameEdit.setFont(font)
        self.userNameEdit.setObjectName("userNameEdit")
        self.gridLayout.addWidget(self.userNameEdit, 0, 1, 1, 2)
        self.userPasswordLabel = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.userPasswordLabel.setFont(font)
        self.userPasswordLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.userPasswordLabel.setObjectName("userPasswordLabel")
        self.gridLayout.addWidget(self.userPasswordLabel, 1, 0, 1, 1)
        self.userPasswordEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        self.userPasswordEdit.setFont(font)
        self.userPasswordEdit.setText("")
        self.userPasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.userPasswordEdit.setDragEnabled(False)
        self.userPasswordEdit.setClearButtonEnabled(True)
        self.userPasswordEdit.setObjectName("userPasswordEdit")
        self.gridLayout.addWidget(self.userPasswordEdit, 1, 1, 1, 2)
        self.mainMenuButton = QtWidgets.QPushButton(self.layoutWidget)
        self.mainMenuButton.setMinimumSize(QtCore.QSize(0, 20))
        self.faceIdResetCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.faceIdResetCheckBox.setMinimumSize(QtCore.QSize(0, 20))
        #FACEID데이터파일초기화 버튼###############################################
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.faceIdResetCheckBox.setFont(font)
        self.faceIdResetCheckBox.setObjectName("faceIdButton")
        
        if self.loginFuc.accessUser.trainCount == -1:
            self.faceIdResetCheckBox.setEnabled(False)
        
        self.gridLayout.addWidget(self.faceIdResetCheckBox, 3, 3, 1, 1)
        #####################################################################
        #메인메뉴로 버튼#########################################################
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.mainMenuButton.setFont(font)
        self.mainMenuButton.setObjectName("mainMenuButton")
        self.gridLayout.addWidget(self.mainMenuButton, 3, 1, 1, 2)
        #버튼이벤트연결##########################################################
        self.mainMenuButton.clicked.connect(self.userSelectActive)
        #####################################################################
        #비밀번호찾기 버튼########################################################
        self.findPasswordButton = QtWidgets.QPushButton(self.layoutWidget)
        self.findPasswordButton.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(10)
        self.findPasswordButton.setFont(font)
        self.findPasswordButton.setObjectName("findPasswordButton")
        self.gridLayout.addWidget(self.findPasswordButton, 3, 0, 1, 1)
        #버튼이벤트연결##########################################################
        self.findPasswordButton.clicked.connect(self.findAccountActive)
        #####################################################################
        self.horizontalLayout.addWidget(self.loginGroupbox)
        self.blankRight = QtWidgets.QWidget(login)
        self.blankRight.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.blankRight.setObjectName("blankRight")
        self.horizontalLayout.addWidget(self.blankRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget = QtWidgets.QWidget(login)
        self.widget.setMinimumSize(QtCore.QSize(500, 0))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(login)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_2.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_3.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 0, 2, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_4.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_5.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 1, 1, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_6.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_6.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_2.addWidget(self.pushButton_6, 1, 2, 1, 2)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_7.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_2.addWidget(self.pushButton_7, 2, 0, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_8.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_2.addWidget(self.pushButton_8, 2, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_9.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_9.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_2.addWidget(self.pushButton_9, 2, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_10.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_10.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_2.addWidget(self.pushButton_10, 3, 0, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_11.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_11.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_2.addWidget(self.pushButton_11, 3, 1, 1, 2)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_12.setMinimumSize(QtCore.QSize(75, 75))
        self.pushButton_12.clicked.connect(self.keyboardActive)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_2.addWidget(self.pushButton_12, 3, 3, 1, 1)
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.widget_3 = QtWidgets.QWidget(login)
        self.widget_3.setMinimumSize(QtCore.QSize(500, 0))
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
                
        self.blankBottom = QtWidgets.QWidget(login)
        self.blankBottom.setObjectName("blankBottom")
        self.verticalLayout.addWidget(self.blankBottom)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Form"))
        self.loginButton.setText(_translate("login", "로 그 인"))
        self.userNameLabel.setText(_translate("login", "사용자"))
        self.userPasswordLabel.setText(_translate("login", "암  호"))
        self.mainMenuButton.setText(_translate("login", "시작화면으로"))
        self.faceIdResetCheckBox.setText(_translate("login", "FaceId 초기화"))
        self.findPasswordButton.setText(_translate("login", "비밀번호찾기"))
        self.pushButton.setText(_translate("login", "1"))
        self.pushButton_2.setText(_translate("login", "2"))
        self.pushButton_3.setText(_translate("login", "3"))
        self.pushButton_4.setText(_translate("login", "4"))
        self.pushButton_5.setText(_translate("login", "5"))
        self.pushButton_6.setText(_translate("login", "6"))
        self.pushButton_7.setText(_translate("login", "7"))
        self.pushButton_8.setText(_translate("login", "8"))
        self.pushButton_9.setText(_translate("login", "9"))
        self.pushButton_10.setText(_translate("login", "*"))
        self.pushButton_11.setText(_translate("login", "0"))
        self.pushButton_12.setText(_translate("login", "#"))

    #버튼이벤트함수################################################################
    def userCheck(self):
        #로그인정보확인 함수호출        
        if self.loginFuc.dbIdPwCheck(self.userPasswordEdit.text()) == True:
            #FaceID 처음사용자
            if self.loginFuc.accessUser.trainCount == -1 and len(self.parent().faceIdFuc.picture) > 0:
                 reply = QMessageBox.question(self, 'FaceID 가입', 'FaceID를 사용하시겠습니까? (' + str(len(self.parent().faceIdFuc.picture)) + '장 학습)', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
                 
                 if reply == QMessageBox.Yes:
                    self.parent().faceIdFuc.trainFirstStart()
                 else:
                    pass
            else:    
                if self.faceIdResetCheckBox.isChecked() == True:
                    QMessageBox.information(self, 'FaceId 초기화', "FaceID가 초기화 되었습니다. (재등록 후 사용가능)", QMessageBox.Ok)
                    self.parent().faceIdFuc.trainCountInsert(-1);
                    
                #FaceId 사용자 -> 최대학습횟수확인 후 학습 여부결정
                elif self.parent().faceIdFuc.maxTrainCount > self.loginFuc.accessUser.trainCount:
                    self.parent().faceIdFuc.trainStart()  
            self.parent().stack.setCurrentIndex(3)
        else:
            QMessageBox.critical(self, '로그인 오류', "아이디 또는 비밀번호가 맞지 않습니다", QMessageBox.Ok)
            self.userPasswordEdit.clear()
                        
    def userSelectActive(self):
        #아이디비밀번호찾기다이얼로그 닫기
        if self.dialog != None:
            self.dialog.close()
            
        self.parent().clearUI()
        self.parent().stack.setCurrentIndex(0)

    def findAccountActive(self):
        self.dialog = findAccountDialog()
        self.dialog.show()
    
    def keyboardActive(self):
        btn = self.sender()  
        self.userPasswordEdit.setText(self.userPasswordEdit.text() + btn.text())
        print(self.userPasswordEdit.text())
    ##########################################################################
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = loginUI()
    sys.exit(app.exec_())
