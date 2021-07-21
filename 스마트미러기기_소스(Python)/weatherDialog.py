from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
import datetime
from urllib.parse import urlencode, unquote
import requests
import json

class weatherDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setStyleSheet("background-color:#c4e1ef;")
        self.setupUi(self)
        
        #타이틀바삭제 + 창테두리삭제
        #self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.FramelessWindowHint)
        
    def setupUi(self, weatherInfo):
        weatherInfo.setObjectName("weatherInfo")
        weatherInfo.resize(560, 400)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(weatherInfo)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(weatherInfo)
        self.widget.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget.setObjectName("widget")
        self.horizontalLayout.addWidget(self.widget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.locationtext = QtWidgets.QLabel(weatherInfo)
        self.locationtext.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.locationtext.setFont(font)
        self.locationtext.setAlignment(QtCore.Qt.AlignCenter)
        self.locationtext.setObjectName("locationtext")
        self.verticalLayout.addWidget(self.locationtext)
        self.todayImage = QtWidgets.QLabel(weatherInfo)
        self.todayImage.setAlignment(QtCore.Qt.AlignCenter)
        self.todayImage.setObjectName("todayImage")
        self.verticalLayout.addWidget(self.todayImage)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.widget_2 = QtWidgets.QWidget(weatherInfo)
        self.widget_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout.addWidget(self.widget_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.waterImage = QtWidgets.QLabel(weatherInfo)
        self.waterImage.setAlignment(QtCore.Qt.AlignCenter)
        self.waterImage.setObjectName("waterImage")
        self.verticalLayout_2.addWidget(self.waterImage)
        
        self.water = QtWidgets.QLabel(weatherInfo)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.water.setFont(font)
        self.water.setAlignment(QtCore.Qt.AlignCenter)
        self.water.setObjectName("water")
        self.verticalLayout_2.addWidget(self.water)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.weathercondition = QtWidgets.QLabel(weatherInfo)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.weathercondition.setFont(font)
        self.weathercondition.setAlignment(QtCore.Qt.AlignCenter)
        self.weathercondition.setObjectName("weathercondition")
        self.verticalLayout_3.addWidget(self.weathercondition)
        self.tem = QtWidgets.QLabel(weatherInfo)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.tem.setFont(font)
        self.tem.setAlignment(QtCore.Qt.AlignCenter)
        self.tem.setObjectName("tem")
        self.verticalLayout_3.addWidget(self.tem)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.windImage = QtWidgets.QLabel(weatherInfo)
        self.windImage.setAlignment(QtCore.Qt.AlignCenter)
        self.windImage.setObjectName("windImage")
        self.verticalLayout_4.addWidget(self.windImage)
        
        self.wind = QtWidgets.QLabel(weatherInfo)
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(16)
        self.wind.setFont(font)
        self.wind.setAlignment(QtCore.Qt.AlignCenter)
        self.wind.setObjectName("wind")
        self.verticalLayout_4.addWidget(self.wind)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.pushButton = QtWidgets.QPushButton(weatherInfo)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(50)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton.clicked.connect(self.closeButtonClicked)
        self.verticalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.retranslateUi(weatherInfo)
        QtCore.QMetaObject.connectSlotsByName(weatherInfo)

        self.weather(self)
               
    def retranslateUi(self, weatherInfo):
        _translate = QtCore.QCoreApplication.translate
        weatherInfo.setWindowTitle(_translate("weatherInfo", "오늘 날씨"))
        self.locationtext.setText(_translate("weatherInfo", "현재위치"))
        self.todayImage.setText(_translate("weatherInfo", "날씨사진"))
        #self.waterImage.setText(_translate("weatherInfo", "습도사진"))
        self.water.setText(_translate("weatherInfo", "습도"))
        self.weathercondition.setText(_translate("weatherInfo", "날씨상태"))
        self.tem.setText(_translate("weatherInfo", "온도"))
        #self.windImage.setText(_translate("weatherInfo", "풍속사진"))
        self.wind.setText(_translate("weatherInfo", "풍속"))
        self.pushButton.setText(_translate("weatherInfo", "닫기"))
        self.locationtext.setText(_translate("weatherInfo", self.parent().loc))

    def closeButtonClicked(self):
        self.close()

    def weather(self,weatherInfo):
        now=datetime.datetime.now() #현재 시각을 시스템에서 가져옴
        hour=now.hour #오전 오후 나타낼때 필요
        
        response = requests.get(self.parent().queryURL)

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
                if(item.get("category") == "PTY"):#강수형태: 없음(0) 비(1) 비+눈(2) 눈(3) 소나기(4) 빗방울(5) 빗방울/눈날림(6) 눈날림(7)
                        result3 = item
                        break
        for item in r_item:
                if(item.get("category") == "WSD"):#풍속 10이상 m/s
                        result4 = item
                        break
        for item in r_item:
                if(item.get("category") == "LGT"):#낙뢰 확률없음(0) 낮음(1) 보통(2) 높음(3)
                        result5 = item
                        break
        for item in r_item:
                if(item.get("category") == "REH"):#습도 단위: %
                        result6 = item
                        break
                    
        self.tem.setText("[ %.1f ℃ ]" %(float(result.get("fcstValue"))))
        self.water.setText("%s" %(int(result6.get("fcstValue"))) + "%")
        self.wind.setText("%s" %(int(result4.get("fcstValue"))) + "m/s")
        
        if hour > 5 and hour < 19: #낮시간대 
            if result2.get("fcstValue") == "1": #맑음
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/sun.png"))
                self.weathercondition.setText("맑음")
            elif result2.get("fcstValue") == "3": #구름많음
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/cloudy_day.png"))
                self.weathercondition.setText("구름많음")
            elif result2.get("fcstValue") == "4": #흐림
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                self.weathercondition.setText("흐림")
        elif result3.get("fcstValue") == "1" or result3.get("fcstValue") == "4": #비
            self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/drop.png"))
            self.weathercondition.setText("비")
        elif result3.get("fcstValue") == "2" or result3.get("fcstValue") == "3": #눈
            self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/snowflake.png"))
            self.weathercondition.setText("눈")
        elif float(result4.get("fcstValue")) >= 8: #풍속
            self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/wind.png"))
            self.weathercondition.setText("강한 바람")
        elif result5.get("fcstValue") == 3: #낙뢰
            self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/bolt.png"))
            self.weathercondition.setText("낙뢰")
        else:  #저녁 시간대 -> 밤
            if result2.get("fcstValue") == "1": #맑음
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/moon.png"))
                self.weathercondition.setText("맑음")
            elif result2.get("fcstValue") == "3": #구름많음
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/cloudy_night.png"))
                self.weathercondition.setText("구름많음")
            elif result2.get("fcstValue") == "4": #흐림
                self.todayImage.setPixmap(QtGui.QPixmap("weather_icon/clouds.png"))
                self.weathercondition.setText("흐림")
        self.windImage.setPixmap(QtGui.QPixmap("weather_icon/windspeed.png"))
        self.waterImage.setPixmap(QtGui.QPixmap("weather_icon/water.png"))     

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    weatherInfo = QtWidgets.QDialog()
    ui = Ui_weatherInfo()
    ui.setupUi(weatherInfo)
    weatherInfo.show()
    sys.exit(app.exec_())
