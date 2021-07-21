from PyQt5 import  QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt5.QtCore import QCoreApplication, QDate, Qt
from PyQt5.QtGui import QPixmap, QImage

from weatherDialog import *
from callSttDialog import *
from detailDayDialog import *
from weatherlocation import *
from entity import *
from Print2 import *

from time import sleep
from urllib.parse import urlencode, unquote
from threading import Thread
import sys
import datetime
import requests
import json
import speech_recognition as sr
import serial



class mainUI(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#6db6d9;")
        self.dialog = None
        self.ui = None
        self.pr = None
        self.ActiveFlag = None
        
        self.setupUi(self)
        self.time_start(self)
        self.weather_start(self)
        
        self.queryURL = None
        self.nx=97
        self.ny=75
        self.loc="부산광역시 부산진구 개금제1동"
        
        self.location.setText(self.loc)
        
        self.stop = False
        self.OThread = False
        self.DThread = False
        
        self.r = sr.Recognizer()
        self.m = sr.Microphone()
            
        self.chart.setPixmap(QtGui.QPixmap("system_Icon/main.jpg"))

    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(1280, 800)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(main)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.blankTop = QtWidgets.QWidget(main)
        self.blankTop.setMinimumSize(QtCore.QSize(0, 20))
        self.blankTop.setObjectName("blankTop")
        self.verticalLayout.addWidget(self.blankTop)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.blankLeft = QtWidgets.QWidget(main)
        self.blankLeft.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankLeft.setObjectName("blankLeft")
        self.horizontalLayout.addWidget(self.blankLeft)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.calendarWidget = QtWidgets.QCalendarWidget(main)
        self.calendarWidget.setVerticalHeaderFormat(0)
        self.calendarWidget.setEnabled(True)
        self.calendarWidget.setMaximumSize(QtCore.QSize(16777215, 400))
        self.calendarWidget.setSizeIncrement(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        #일정표#############################################################
        self.calendarWidget.setFont(font)
        self.calendarWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.calendarWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setInputMethodHints(QtCore.Qt.ImhNone)
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setDateEditAcceptDelay(1500)
        self.calendarWidget.setObjectName("calendarWidget")
        self.gridLayout.addWidget(self.calendarWidget, 0, 0, 1, 3)
        #일정표클릭이벤트연결#######################################################
        self.calendarWidget.clicked.connect(self.detailDayActive)
        ####################################################################
        self.blank = QtWidgets.QWidget(main)
        self.blank.setMinimumSize(QtCore.QSize(0, 0))
        self.blank.setMaximumSize(QtCore.QSize(16777215, 10))
        self.blank.setObjectName("blank")
        self.gridLayout.addWidget(self.blank, 1, 0, 1, 3)
        self.chart = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        self.chart.setFont(font)
        self.chart.setAlignment(QtCore.Qt.AlignCenter)
        self.chart.setObjectName("chart")
        self.gridLayout.addWidget(self.chart, 2, 1, 1, 1)
        ##날씨###############################################
        self.weatherPicture = QtWidgets.QLabel(main)
        self.weatherPicture.setAlignment(QtCore.Qt.AlignCenter)
        self.weatherPicture.setObjectName("weatherPicture")
        ######날씨 사진 클릭 이벤트##############################
        self.weatherPicture.mousePressEvent = self.WeatherLocation
        ####################################################
        self.gridLayout.addWidget(self.weatherPicture, 2, 0, 1, 1)
        self.dateText = QtWidgets.QLabel(main)
        self.dateText.setMinimumSize(QtCore.QSize(550, 0))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.dateText.setFont(font)
        self.dateText.setAlignment(QtCore.Qt.AlignCenter)
        self.dateText.setObjectName("dateText")
        self.gridLayout.addWidget(self.dateText, 3, 1, 1, 1)
        
        #음성인식호출버튼#########################################################
        self.callSttButton = QtWidgets.QPushButton(main)
        self.callSttButton.setMinimumSize(QtCore.QSize(0, 150))
        self.callSttButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.callSttButton.setFont(font)
        self.callSttButton.setObjectName("callSttButton")
        self.gridLayout.addWidget(self.callSttButton, 2, 2, 1, 1)
        #버튼이벤트연결###########################################################
        self.callSttButton.clicked.connect(self.callSttActive)
        ####################################################################
        
        self.location = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(50)
        self.location.setFont(font)
        self.location.setAlignment(QtCore.Qt.AlignCenter)
        self.location.setObjectName("location")
        self.gridLayout.addWidget(self.location, 3, 0, 1, 1)
                
        self.timeText = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.timeText.setFont(font)
        self.timeText.setAlignment(QtCore.Qt.AlignCenter)
        self.timeText.setObjectName("timeText")
        self.gridLayout.addWidget(self.timeText, 4, 1, 1, 1)
        self.temperatureText = QtWidgets.QLabel(main)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.temperatureText.setFont(font)
        self.temperatureText.setAlignment(QtCore.Qt.AlignCenter)
        self.temperatureText.setObjectName("temperatureText")
        self.gridLayout.addWidget(self.temperatureText, 4, 0, 1, 1)
        
        #로그아웃버튼###########################################################
        self.logoutButton = QtWidgets.QPushButton(main)
        self.logoutButton.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.logoutButton.setFont(font)
        self.logoutButton.setObjectName("logoutButton")
        self.gridLayout.addWidget(self.logoutButton, 3, 2, 2, 1)
        #버튼이벤트연결###########################################################
        self.logoutButton.clicked.connect(self.userSelectActive)        
        ####################################################################
        
        self.horizontalLayout.addLayout(self.gridLayout)
        self.blankRight = QtWidgets.QWidget(main)
        self.blankRight.setMaximumSize(QtCore.QSize(20, 16777215))
        self.blankRight.setBaseSize(QtCore.QSize(0, 0))
        self.blankRight.setObjectName("blankRight")
        self.horizontalLayout.addWidget(self.blankRight)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.blankBottom = QtWidgets.QWidget(main)
        self.blankBottom.setMinimumSize(QtCore.QSize(0, 20))
        self.blankBottom.setObjectName("blankBottom")
        self.verticalLayout.addWidget(self.blankBottom)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Form"))
        self.weatherPicture.setText(_translate("main", "Loading"))
        self.chart.setText(_translate("main", "Chart"))
        self.dateText.setText(_translate("main", "Loading"))
        self.callSttButton.setText(_translate("main", "음성인식호출"))
        self.timeText.setText(_translate("main", "Loading"))
        self.temperatureText.setText(_translate("main", "Loading"))
        self.logoutButton.setText(_translate("main", "로그아웃"))
               
    #버튼이벤트함수###########################################################
    def detailDayActive(self):
        self.ui = QtWidgets.QWidget()
        self.pr = Ui_Dialog(self)
        self.pr.setupUi(self.ui)
        
        info = detailDayInfo(self.calendarWidget.selectedDate())
        self.dialog = detailDayDialog(info, self.parent().accessUser, self)
        self.dialog.setWindowModality(Qt.ApplicationModal)
        self.dialog.show()
        
        display_monitor = 1
        monitor = QDesktopWidget().screenGeometry(display_monitor)
        self.ui.move(monitor.left(), monitor.top())
        self.ui.showFullScreen()
        self.ui.show()
        
    def userSelectActive(self):
        if self.dialog != None:
            self.dialog.close()
        self.parent().clearUI()
        self.parent().stack.setCurrentIndex(0)
        
    def WeatherLocation(self, event):
        try:
            self.dialog = weatherlocation(self)
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.exec_()
            
            if self.dialog.X == None:
                print("변경없음")
            else:
                self.nx = self.dialog.X
                self.ny = self.dialog.Y
                self.loc = self.dialog.location
        except Exception as ex:
            print(ex)
    ####################################################################
    
    #음성인식버튼이벤트#########################################################
    def callSttActive(self):
        try:
            
            try:
                with self.m as source: self.r.adjust_for_ambient_noise(source) 
            except Exception as ex:
                print(ex)
            
            self.dialog = callSttDialog(self)            
            self.dialog.setWindowModality(Qt.ApplicationModal)
            self.dialog.show()
            
            self.DThread = True
            self.thread4 = threading.Thread(target=self.CallSTTDIALOG)
            
            self.OThread = True
            self.thread3 = threading.Thread(target=self.CallSTTActiveThread)
            
            self.thread4.start()
            self.thread3.start()
                       
            self.dialog.exec()
             
            if self.ActiveFlag == "일정":
                self.ActiveFlag = None
                now=datetime.datetime.now()
                
                self.ui = QtWidgets.QWidget()
                self.pr = Ui_Dialog(self)
                self.pr.setupUi(self.ui)
                                
                info = detailDayInfo(QDate(now.year,now.month,now.day))
                self.dialog = detailDayDialog(info, self.parent().accessUser, self)
                self.dialog.show()  
                
                display_monitor = 1
                monitor = QDesktopWidget().screenGeometry(display_monitor)
                self.ui.move(monitor.left(), monitor.top())
                self.ui.showFullScreen()
                self.ui.show()
                
            if self.ActiveFlag == "날씨":
                self.ActiveFlag = None
                if self.queryURL != None:
                    self.dialog = weatherDialog(self)
                    self.dialog.show()  
                elif self.queryURL == None:
                    QMessageBox.information(self, '통신오류', "기상청 통신오류", QMessageBox.Ok)

            if self.ActiveFlag == "ON":
                self.ActiveFlag = None
                ser = serial.Serial('/dev/ttyACM0', 9600)
                text = "1"
                text = text.encode('utf-8')
                ser.write(text)
            if self.ActiveFlag == "OFF":
                self.ActiveFlag = None
                ser = serial.Serial('/dev/ttyACM0', 9600)
                text = "0"
                text = text.encode('utf-8')
                ser.write(text)

            self.stop = False
        except Exception as ex: # 에러 종류
            print(ex)
            
    def CallSTTDIALOG(self):
        while self.DThread:
            if self.OThread == False:
                self.DThread = False
                self.dialog.close()
    
    #음성인식쓰레드#########################################################
    def CallSTTActiveThread(self):#
        try:
            stop_listening = self.r.listen_in_background(self.m, self.callback)

            while self.OThread:
                if self.stop:
                    stop_listening(wait_for_stop=False)
                    self.OThread = False
                    break
                time.sleep(1)
                
        except Exception as e:
            print(e)        
        
        time.sleep(0.1)
            
    def callback(self, recognizer, audio):#
        
        try:
            text = self.r.recognize_google(audio, language='ko')
            
            self.dialog.listenLabel.setText(text)
            
            if (text.replace(" ", "") == "종료" or text.replace(" ", "") == "끝"):
                self.ActiveFlag = None
                self.stop = True
            if (text.replace(" ", "") == "오늘일정" or text.replace(" ", "") == "일정" or text.replace(" ", "") == "일정보여줘"):
                self.ActiveFlag = "일정"
                self.stop = True
            if (text.replace(" ", "") == "오늘날씨" or text.replace(" ", "") == "날씨" or text.replace(" ", "") == "날씨어때"):
                self.ActiveFlag = "날씨"
                self.stop = True
            if (text.replace(" ", "") == "불켜" or text.replace(" ", "") == "불켜줘" or text.replace(" ", "") == "불켜라" or text.replace(" ", "") == "이기야"):
                self.ActiveFlag = "ON"
                self.stop = True
            if (text.replace(" ", "") == "불꺼" or text.replace(" ", "") == "불꺼줘" or text.replace(" ", "") == "불꺼라"):
                self.ActiveFlag = "OFF"
                self.stop = True
                
        except sr.UnknownValueError:
            
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))    
               
    #시간라벨출력 쓰레드 시작함수#################################################
    def time_start(self,main):
        thread=threading.Thread(target=self.set_time,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()
        
    #날씨라벨출력 쓰레드 시작함수
    def weather_start(self,main):
        self.WThread = True
    
        thread=threading.Thread(target=self.weather_icon,args=(self,))
        thread.daemon=True #프로그램 종료시 프로세스도 함께 종료 (백그라운드 재생 X)
        thread.start()
    
    #################################################################
    #시간라벨->시간설정쓰레드 실행함수
    def set_time(self,main):
        EvenOrAfter = "오전"
        while True:
            now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
            hour=now.hour

            if(now.hour>=12):
                EvenOrAfter="오후"
                hour=now.hour%12

                if(now.hour==12):
                    hour=12

            else:
                EvenOrAfter="오전"

            self.dateText.setText("%s년 %s월 %s일"%(now.year,now.month,now.day))
            self.timeText.setText(EvenOrAfter+" %s시 %s분" %(hour,now.minute))

            self.parent().pr.date.setText("%s년 %s월 %s일"%(now.year,now.month,now.day))
            self.parent().pr.time.setText(EvenOrAfter+" %s시 %s분" %(hour,now.minute))
            
            sleep(1)
           
    ##################################################################           
    #날씨라벨->API통신을 위한 시간초기화함수 (in 쓰레드)
    def get_api_date(self): 
        time_H = datetime.datetime.now().strftime('%H')
        time_M = datetime.datetime.now().strftime('%M')
        
        if int(time_M) < 30:   #매시의 30분에 값이 발표됨(ex..16시30분)    
            check_time = int(time_H) - 1
            day_calibrate = 0
            if check_time < 0:
                day_calibrate = 1
                check_time = 23
        else:
            check_time = int(time_H)
            day_calibrate = 0


        if check_time < 10:
            check_time = str(check_time).zfill(2) #한자리 숫자의 앞에 0을 채움

            
        date_now = datetime.datetime.now().strftime('%Y%m%d')
        check_date = int(date_now) - day_calibrate

        return (str(check_date), (str(check_time) + '00'))

    ##################################################################
    #날씨라벨->날씨API연결 및 아이콘 실행함수
    def weather_icon(self,main):
        while True:
            try:
                now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
                hour=now.hour
                cur_date, cur_hour = main.get_api_date()
                
                url = "http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst"
                queryString = "?" + urlencode(
                {
                  "ServiceKey": unquote("YbBDMYffomfa4gOajgKgE5Ji6sEBYVNzYwK6bYyQcSGEtM3OFF56rJ2%2BWp7yNQqUiyO75RkLOm1TVXA1uDQUAA%3D%3D"),
                  "base_date": cur_date, #최근 24시간 데이터만 제공
                  "base_time": cur_hour, #2, 5, 8, 11, 14, 17, 20, 23시에 발표 
                  "nx": self.nx, 
                  "ny": self.ny,
                  "numOfRows": "100", #페이지 결과값 
                  "pageNo": 1,
                  "dataType": "JSON"
                }
                )
                self.queryURL = url + queryString
                response = requests.get(self.queryURL)

                r_dict = json.loads(response.text)
                r_response = r_dict.get("response")
                r_body = r_response.get("body")
                r_items = r_body.get("items")
                r_item = r_items.get("item")

                result = {}
                for item in r_item:
                    if(item.get("category") == "T1H"): #온도
                        result = item
                        break
                for item in r_item:
                    if(item.get("category") == "SKY"): #하늘상태: 맑음(1) 구름많음(3) 흐름(4)
                        result2 = item
                        break
                for item in r_item:
                    if(item.get("category") == "PTY"):#강수형태: 없음(0) 비(1) 비+눈(2) 눈(3) 소나기(4)
                        result3 = item
                        break
                for item in r_item:
                    if(item.get("category") == "WSD"):#풍속 10이상
                        result4 = item
                        break
                for item in r_item:
                    if(item.get("category") == "LGT"):#낙뢰 확률없음(0) 낮음(1) 보통(2) 높음(3)
                        result5 = item
                        break
                            
                self.temperatureText.setText("[ %.1f ℃ ]" %(float(result.get("fcstValue"))))
                self.parent().pr.temper.setText("[ %.1f ℃ ]" %(float(result.get("fcstValue"))))

                if hour > 5 and hour < 19: #낮시간대 
                    if result2.get("fcstValue") == "1": #맑음
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/sun.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/sun.png"))
                    elif result2.get("fcstValue") == "3": #구름많음
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/cloudy_day.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/cloudy_day.png"))
                    elif result2.get("fcstValue") == "4": #흐림
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                elif result3.get("fcstValue") == "1" or result3.get("fcstValue") == "4": #비
                    self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/drop.png"))
                    self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/drop.png"))
                elif result3.get("fcstValue") == "2" or result3.get("fcstValue") == "3": #눈
                    self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/snowflake.png"))
                    self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/snowflake.png"))
                elif float(result4.get("fcstValue")) >= 8: #풍속
                    self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/wind.png"))
                    self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/wind.png"))
                elif result5.get("fcstValue") == 3: #낙뢰
                    self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/bolt.png"))
                    self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/bolt.png"))
                else:  #저녁 시간대 -> 밤
                    if result2.get("fcstValue") == "1": #맑음
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/moon.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/moon.png"))
                    elif result2.get("fcstValue") == "3": #구름많음
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/cloudy_night.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/cloudy_night.png"))
                    elif result2.get("fcstValue") == "4": #흐림
                        self.weatherPicture.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                        self.parent().pr.weatherImage.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                self.parent().pr.address.setText(self.loc)            
            except Exception as ex:
                print("weatherAPI Connect Unstable")
            time.sleep(3)
                
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = mainUI()
    sys.exit(app.exec_())
