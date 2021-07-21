from PyQt5 import QtWidgets
import os
import mysql.connector

from userSelectUI import *
from faceIdUI import *
from loginUI import *
from mainUI import *
from entity import *
from Print import *
from screeninfo import get_monitors

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = QtWidgets.QWidget()
        self.pr = Ui_Dialog()
        self.pr.setupUi(self.ui)

        display_monitor = 0
        monitor = QDesktopWidget().screenGeometry(display_monitor)
        self.move(monitor.left(), monitor.top())
    
        display_monitor = 1
        monitor = QDesktopWidget().screenGeometry(display_monitor)
        self.ui.move(monitor.left(), monitor.top())
        self.ui.showFullScreen()
                
        self.ui.show()
        
        self.setStyleSheet("background-color:#98cde4;")
        #모든사용자 목록
        self.userList = list()

        #접속시도 중인 사용자
        self.accessUser = user()

        #데이터베이스 어드레스
        self.dbAddress = "SmartMirror/smartiot@doran2322.iptime.org:12511/xe"

        #학습데이터정리
        self.faceIdFuc = faceId()

        self.initUI()
        self.stack = QtWidgets.QStackedLayout(self)
        self.clearUI()
        self.show();

    def initUI(self):
        self.setWindowTitle("MainWindow")
        self.setFixedSize(1280, 800)

        #상태바 + 창 테두리삭제
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
        #전체화면
        self.showFullScreen ()

    #UI스택이 비었으면 stack채우고 비어있지않으면 스택Clear후 채움
    def clearUI(self, index=None):         
        #매개변수가없으면 모든 UI일괄삭제하고 재생성
        
        if index == None:
            if self.stack.isEmpty() == False:
                for i in reversed (range(self.stack.count())):
                    self.stack.itemAt(i).widget().close()
                    self.stack.takeAt(i)
                                
            self.userListRead()
            self.stack1 = userSelectUI(self)
            self.stack2 = faceIdUI(self)
            self.stack3 = loginUI(self)
            self.stack4 = mainUI(self)
                
            self.stack.addWidget(self.stack1)
            self.stack.addWidget(self.stack2)
            self.stack.addWidget(self.stack3)
            self.stack.addWidget(self.stack4)

        #매개변수가있으면 지정된 index의 UI만 삭제하고 재생성
        else:
            self.stack.itemAt(index).widget().close()
            self.stack.takeAt(index)

            if index == 0:
                self.userListRead()
                self.stackTemp = userSelectUI(self)
                    
            elif index == 1:
                self.stackTemp = faceIdUI(self)
                    
            elif index == 2:
                self.stackTemp = loginUI(self)
                    
            elif index == 3:
                self.stackTemp = mainUI(self)

            self.stack.insertWidget(index, self.stackTemp)

    #DB에서 모든사용자를 조회하여 저장
    def userListRead(self):
        self.accessUser = user()
        self.userList = list()
        conn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")

        curs=conn.cursor(dictionary=True)

        sql = "select * from mirroruser"
        
        curs.execute(sql)
        
        for row in curs:
            temp = user(row["id"], row["name"], row["tel"], row["traincount"], self.detailDayListRead(row["id"]))

            if os.path.exists("/home/pi/exe/mirror/faceIdData/" + temp.id + ".jpg"):
                pictureTemp = cv2.imread("/home/pi/exe/mirror/faceIdData/" + temp.id + ".jpg")
                pictureTemp = cv2.cvtColor(pictureTemp, cv2.COLOR_BGR2RGB)
                pictureTemp = cv2.resize(pictureTemp, dsize=(80, 80), interpolation=cv2.INTER_AREA)
                h,w,c = pictureTemp.shape
                temp.picture = QtGui.QPixmap.fromImage(QtGui.QImage(pictureTemp.data, w, h, w*c, QtGui.QImage.Format_RGB888))

            self.userList.append(temp)
        curs.close()
        conn.close()
        
    def detailDayListRead(self, id):
        Dconn= mysql.connector.connect(host="doran2322.iptime.org",port="60336",database="smartmirror",user= "smartmirror",password="smartiot")
   
    
        Dcursor = Dconn.cursor(dictionary=True)
        
        Dsql = "select * from detailday where id = '" + id + "'"
        Dcursor.execute(Dsql)
        
        #일정정보 목록
        detailDayList = list()
        
        for row in Dcursor:
            detailDayList.append(detailDayInfo(row["time"], row["plan"], row["item"]))
        Dcursor.close()
        Dconn.close()
        
        return detailDayList
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    main = MainWindow()
    
    app.exec()
