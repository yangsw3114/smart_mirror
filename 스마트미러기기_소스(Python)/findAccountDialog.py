from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QMessageBox
from PyQt5.QtCore import QCoreApplication

import sys

class findAccount:
    def dbIdRead(self, inputName, inputTel):
        outId = None
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
        curs=conn.cursor(dictionary=True)
        sql = "select id from MirrorUser where name = '" + inputName + "'" + " and tel = '" + inputTel + "'"
        curs.execute(sql)
        
        for row in curs:
            outId = row["id"]
            
        curs.close()
        conn.close()
        
        return outId
            
    def dbPwRead(self, inputId):
        outPw = None
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
        curs=conn.cursor(dictionary=True)
        sql = "select pw from MirrorUser where id = '" + inputId  + "'" 
        curs.execute(sql)
                
        for row in curs:
            outPw = row["pw"]
            
        curs.close()
        conn.close()
        
        return outPw


class findAccountDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#c4e1ef;")
        self.findAccountFuc = findAccount()
        self.setupUi(self)
        
    def setupUi(self, findIdPw):
        findIdPw.setObjectName("findIdPw")
        findIdPw.resize(427, 319)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(findIdPw)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.widget_11 = QtWidgets.QWidget(findIdPw)
        self.widget_11.setObjectName("widget_11")
        self.verticalLayout_7.addWidget(self.widget_11)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget_9 = QtWidgets.QWidget(findIdPw)
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout_3.addWidget(self.widget_9)
        self.tabWidget = QtWidgets.QTabWidget(findIdPw)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(9)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_3.addWidget(self.widget_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setMaximumSize(QtCore.QSize(300, 100))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        
        #아이디찾기버튼####################################################################
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 60))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 2, 2, 1)        
        #버튼이벤트연결####################################################################
        self.pushButton.clicked.connect(self.findIdActive)
        #############################################################################
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout.addWidget(self.groupBox)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3.addWidget(self.widget_4)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget_5 = QtWidgets.QWidget(self.tab_2)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_5.addWidget(self.widget_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.tab_2)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setMaximumSize(QtCore.QSize(300, 100))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        #비밀번호조회버튼##################################################################
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 20))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 2, 2, 1)
        #비밀번호조회버튼##################################################################
        self.pushButton_2.clicked.connect(self.findPwActive)
        #############################################################################
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_2.addWidget(self.lineEdit_3, 0, 1, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 2, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout_2.addWidget(self.groupBox_2)
        self.widget_7 = QtWidgets.QWidget(self.tab_2)
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout_2.addWidget(self.widget_7)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.widget_8 = QtWidgets.QWidget(self.tab_2)
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_5.addWidget(self.widget_8)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        self.horizontalLayout_3.addWidget(self.tabWidget)
        self.widget_10 = QtWidgets.QWidget(findIdPw)
        self.widget_10.setObjectName("widget_10")
        self.horizontalLayout_3.addWidget(self.widget_10)
        self.verticalLayout_7.addLayout(self.horizontalLayout_3)
        self.widget_12 = QtWidgets.QWidget(findIdPw)
        self.widget_12.setObjectName("widget_12")
        self.verticalLayout_7.addWidget(self.widget_12)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)

        self.retranslateUi(findIdPw)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(findIdPw)

    def retranslateUi(self, findIdPw):
        _translate = QtCore.QCoreApplication.translate
        findIdPw.setWindowTitle(_translate("findIdPw", "아이디 비밀번호 찾기"))
        self.label.setText(_translate("findIdPw", "이  름"))
        self.pushButton.setText(_translate("findIdPw", "찾기"))
        self.label_2.setText(_translate("findIdPw", "전화번호"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("findIdPw", "아이디찾기"))
        self.pushButton_2.setText(_translate("findIdPw", "조회"))
        self.label_3.setText(_translate("findIdPw", "아이디"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("findIdPw", "비밀번호찾기"))
    
    def findIdActive(self):
        
    
        #아이디받아서 다이얼로그띄우기
        outId = self.findAccountFuc.dbIdRead(self.lineEdit.text(), self.lineEdit_2.text())    #이름, 전화번호
                
        if outId == None:
            outId = "일치하는 아이디가 없습니다."
        else:
            outId = "일치하는 아이디는 '" + outId + "' 입니다."
        
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('아이디 찾기')
        self.msg.setText(outId)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
    
    def findPwActive(self):
        #비밀번호받아서 다이얼로그띄우기
        outPw = self.findAccountFuc.dbPwRead(self.lineEdit_3.text())    #Id
        
        if outPw == None:
            outPw = "일치하는 비밀번호가 없습니다."
        else:
            outPw = "일치하는 비밀번호는 '" + outPw + "' 입니다."
        
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.Information)
        self.msg.setWindowTitle('비밀번호 찾기')
        self.msg.setText(outPw)
        self.msg.setStandardButtons(QMessageBox.Ok)
        self.msg.exec_()
        
        self.lineEdit_3.setText("")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = findAccountDialog()
    sys.exit(app.exec_())
