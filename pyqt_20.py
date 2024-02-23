# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\MoonS\Desktop\UIUIUI\pyqt_11.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# 이미지 생성 + 가격 + 개수

from PyQt5 import QtCore, QtGui, QtWidgets

#제품 정보담는 class
class Item:
    def __init__(self, name, price, img_path):
        self.name = name
        self.price = price
        self.img_path = img_path
        self.count = 0
#UI 셋업
class Ui_Calcu_1(object):
    def setupUi(self, Calcu_1):
        Calcu_1.setObjectName("Calcu_1")
        Calcu_1.resize(1280, 800)
        self.centralwidget = QtWidgets.QWidget(Calcu_1)
        self.centralwidget.setObjectName("centralwidget")
        self.Count_0 = QtWidgets.QTextEdit(self.centralwidget)
        self.Count_0.setGeometry(QtCore.QRect(300, 50, 81, 41))
        self.Count_0.setObjectName("Count_0")
        self.All = QtWidgets.QTextEdit(self.centralwidget)
        self.All.setGeometry(QtCore.QRect(440, 510, 101, 41))
        self.All.setObjectName("All")
        self.Price_0 = QtWidgets.QTextEdit(self.centralwidget)
        self.Price_0.setGeometry(QtCore.QRect(670, 50, 101, 41))
        self.Price_0.setObjectName("Price_0")
##################### 제품의 정보들을 담기 ################ <<<!!! 이미지 "파일 경로" 주의 !!!>>>
        self.items = [
            Item("kancho", 980, r"C:\Users\MoonS\Desktop\Items\ssunchip_img.png"),
            Item("ssunchip", 1400, r"C:\Users\MoonS\Desktop\Items\ssunchip_img.png"),
            Item("honeychip", 1600, r"C:\Users\MoonS\Desktop\Items\honeychip_img.png"),
            #Item()
        ]
#################### 제품 버튼 ##############
        self.kancho_button = QtWidgets.QPushButton(self.centralwidget)
        self.kancho_button.setGeometry(QtCore.QRect(10, 400, 75, 23))
        self.kancho_button.setObjectName("kancho_button")
        self.kancho_button.setText("Kancho")
        self.kancho_button.clicked.connect(lambda: self.update_item_info("kancho"))
        self.ssunchip_button = QtWidgets.QPushButton(self.centralwidget)
        self.ssunchip_button.setGeometry(QtCore.QRect(10, 420, 75, 23))
        self.ssunchip_button.setObjectName("ssunchip_button")
        self.ssunchip_button.setText("Ssunchip")
        self.ssunchip_button.clicked.connect(lambda: self.update_item_info("ssunchip"))
        self.honeychip_button = QtWidgets.QPushButton(self.centralwidget)
        self.honeychip_button.setGeometry(QtCore.QRect(10, 440, 75, 23))
        self.honeychip_button.setObjectName("honeychip_button")
        self.honeychip_button.setText("Honeychip")
        self.honeychip_button.clicked.connect(lambda: self.update_item_info("honeychip"))
############ X (delete) 버튼 ############
        self.delete_button = QtWidgets.QPushButton(self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(775, 140, 21, 21))
        self.delete_button.setObjectName("delete_button_1")
        self.delete_button.setText("X")
        self.delete_button.clicked.connect(self.delete_item_info)
########### + - 버튼 ################
        self.minus_1 = QtWidgets.QPushButton(self.centralwidget)
        self.minus_1.setGeometry(QtCore.QRect(220, 140, 75, 23))
        self.minus_1.setObjectName("minus_1")
        self.minus_1.clicked.connect(lambda: self.minus(0))
        self.plus_1 = QtWidgets.QPushButton(self.centralwidget)
        self.plus_1.setGeometry(QtCore.QRect(390, 140, 75, 23))
        self.plus_1.setObjectName("plus_1")
        self.plus_1.clicked.connect(lambda: self.plus(0))
################################### UI 셋업 ##############
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 461, 41))
        self.label.setObjectName("label")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(60, 50, 81, 41))
        self.textEdit_12.setObjectName("textEdit_12")
        self.Count_1 = QtWidgets.QLabel(self.centralwidget)
        self.Count_1.setGeometry(QtCore.QRect(310, 130, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Count_1.setFont(font)
        self.Count_1.setText("")
        self.Count_1.setObjectName("Count_1")
        self.Price_1 = QtWidgets.QLabel(self.centralwidget)
        self.Price_1.setGeometry(QtCore.QRect(670, 133, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Price_1.setFont(font)
        self.Price_1.setText("")
        self.Price_1.setObjectName("Price_1")
        self.Price_sum = QtWidgets.QLabel(self.centralwidget)
        self.Price_sum.setGeometry(QtCore.QRect(550, 510, 151, 41))
        self.Price_sum.setText("")
        self.Price_sum.setObjectName("Price_sum")
        ########### IMG 라벨 ##########
        self.img_1 = QtWidgets.QLabel(self.centralwidget)
        self.img_1.setGeometry(QtCore.QRect(50, 110, 101, 81))
        self.img_1.setText("")
        self.img_1.setObjectName("img_1")
                        
        Calcu_1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calcu_1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Calcu_1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calcu_1)
        self.statusbar.setObjectName("statusbar")
        Calcu_1.setStatusBar(self.statusbar)

        self.retranslateUi(Calcu_1)
        QtCore.QMetaObject.connectSlotsByName(Calcu_1)
############ 한글 변환 #########
    def retranslateUi(self, Calcu_1):
        _translate = QtCore.QCoreApplication.translate
        Calcu_1.setWindowTitle(_translate("Calcu_1", "총합 계산기"))
        self.Count_0.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">개  수</span></p></body></html>"))
        self.All.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">합  계</span></p></body></html>"))
        self.Price_0.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">가  격</span></p></body></html>"))
        self.minus_1.setText(_translate("Calcu_1", "-"))
        self.plus_1.setText(_translate("Calcu_1", "+"))
        self.label.setText(_translate("Calcu_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">갯수 +- 와 자동으로 합산액을 나타내어 준다.</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">물  건</span></p></body></html>"))
        self.selected_item_name = None
        self.count = [0]

    def delete_item_info(self):
        # 현재 선택된 아이템의 정보를 초기화
        count = self.count[0]
        selected_item = next((item for item in self.items if item.count == count), None)
        if selected_item:
            selected_item.count = 0
            self.Count_1.clear()
            self.Price_1.clear()
            self.img_1.clear()
            self.update_label()
            
        self.count = [0]
        self.selected_item_name = None
        

### img 업뎃 ####
    def update_item_info(self, item_name):
            for item in self.items:
                if item.name == item_name:
                        pixmap = QtGui.QPixmap(item.img_path)
                        self.img_1.setPixmap(pixmap)
                        self.img_1.setScaledContents(True)
                        
                        self.selected_item_name = item_name  # 변경된 부분
                        self.count[0] = 1
                        self.update_label()
                        break
############## + - 계산 함수 ###################
    def plus(self, index):
        self.count[index] += 1
        self.update_label()
    def minus(self, index):
        if self.count[index] > 0:
            self.count[index] -= 1
        self.update_label()
###################### 상품 정보 업데이트 #############
    def update_label(self):
        count = self.count[0]

        selected_item = next((item for item in self.items if item.name == self.selected_item_name), None)
        price_1 = selected_item.price * count if selected_item else 0

        self.Count_1.setText(str(count) + ' 개')
        self.Price_1.setText(str(price_1) + ' 원')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calcu_1 = QtWidgets.QMainWindow()
    ui = Ui_Calcu_1()
    ui.setupUi(Calcu_1)
    Calcu_1.show()
    sys.exit(app.exec_())