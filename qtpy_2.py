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
    def __init__(self):
        self.rows = []
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
            Item("kancho", 980, r"C:\Users\MoonS\Desktop\Items\kancho_img.png"),
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

################################### UI 셋업 ##############
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 461, 41))
        self.label.setObjectName("label")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(60, 50, 81, 41))
        self.textEdit_12.setObjectName("textEdit_12")
        self.Price_sum = QtWidgets.QLabel(self.centralwidget)
        self.Price_sum.setGeometry(QtCore.QRect(550, 510, 151, 41))
        self.Price_sum.setText("")
        self.Price_sum.setObjectName("Price_sum")

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
        self.label.setText(_translate("Calcu_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">갯수 +- 와 자동으로 합산액을 나타내어 준다.</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">물  건</span></p></body></html>"))
        self.selected_item_name = None
        self.count = [0]
    def add_row_widgets(self, row_index):
        # 이미지 라벨
        img_label = QtWidgets.QLabel(self.centralwidget)
        img_label.setGeometry(QtCore.QRect(50, 110 + (row_index - 1) * 100, 101, 81))
        img_label.setText("")
        img_label.setObjectName(f"img_{row_index}")

        # - 버튼
        minus_button = QtWidgets.QPushButton(self.centralwidget)
        minus_button.setGeometry(QtCore.QRect(220, 140 + (row_index - 1) * 100, 75, 23))
        minus_button.setObjectName(f"minus_{row_index}")
        minus_button.setText("-")
        minus_button.clicked.connect(lambda: self.minus(row_index - 1))

        # 개수 라벨
        count_label = QtWidgets.QLabel(self.centralwidget)
        count_label.setGeometry(QtCore.QRect(310, 130 + (row_index - 1) * 100, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        count_label.setFont(font)
        count_label.setText("")
        count_label.setObjectName(f"Count_{row_index}")

        # + 버튼
        plus_button = QtWidgets.QPushButton(self.centralwidget)
        plus_button.setGeometry(QtCore.QRect(390, 140 + (row_index - 1) * 100, 75, 23))
        plus_button.setObjectName(f"plus_{row_index}")
        plus_button.setText("+")
        plus_button.clicked.connect(lambda: self.plus(row_index - 1))

        # 가격 라벨
        price_label = QtWidgets.QLabel(self.centralwidget)
        price_label.setGeometry(QtCore.QRect(670, 133 + (row_index - 1) * 100, 101, 31))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        price_label.setFont(font)
        price_label.setText("")
        price_label.setObjectName(f"Price_{row_index}")

        # X 버튼
        delete_button = QtWidgets.QPushButton(self.centralwidget)
        delete_button.setGeometry(QtCore.QRect(775, 140 + (row_index - 1) * 100, 21, 21))
        delete_button.setObjectName(f"delete_button_{row_index}")
        delete_button.setText("X")
        delete_button.clicked.connect(lambda: self.delete_item_info(row_index - 1))

        # 여기에서 버튼을 참조할 수 있도록 설정
        setattr(self, f"img_{row_index}", img_label)
        setattr(self, f"minus_{row_index}", minus_button)
        setattr(self, f"Count_{row_index}", count_label)
        setattr(self, f"plus_{row_index}", plus_button)
        setattr(self, f"Price_{row_index}", price_label)
        setattr(self, f"delete_button_{row_index}", delete_button)

        # 생성한 행을 self.rows에 추가
        self.rows.append(Item(f"item_{row_index}", 0, ""))

    def delete_item_info(self, row_index):
        # 현재 선택된 아이템의 정보를 초기화
        count = self.count[row_index]
        selected_item = next((item for item in self.items if item.count == count), None)
        if selected_item:
            selected_item.count = 0
            count_label = getattr(self, f"Count_{row_index + 1}")
            price_label = getattr(self, f"Price_{row_index + 1}")
            img_label = getattr(self, f"img_{row_index + 1}")

            count_label.clear()
            price_label.clear()
            img_label.clear()
            self.update_label(row_index)
            
        self.count[row_index] = 0
        self.selected_item_name = None

### img 업뎃 ####
    def update_item_info(self, item_name):
        row_index = len(self.rows)
        self.add_row_widgets(row_index + 1)
        
        for index in range(len(self.rows)):
            if self.rows[index].name == item_name:
                pixmap = QtGui.QPixmap(self.rows[index].img_path)
                img_label = getattr(self, f"img_{index + 1}")
                img_label.setPixmap(pixmap)
                img_label.setScaledContents(True)

                self.selected_item_name = item_name
                self.count[index] = 1
                self.update_label(index)
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
    def update_label(self, index):
        count = self.count[index]

        selected_item = next((item for item in self.items if item.name == self.selected_item_name), None)
        price = selected_item.price * count if selected_item else 0

        count_label = getattr(self, f"Count_{index + 1}")
        price_label = getattr(self, f"Price_{index + 1}")

        count_label.setText(str(count) + ' 개')
        price_label.setText(str(price) + ' 원')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calcu_1 = QtWidgets.QMainWindow()
    ui = Ui_Calcu_1()
    try:
        ui.setupUi(Calcu_1)
        Calcu_1.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("An error occurred:", e)
    ui.setupUi(Calcu_1)
    Calcu_1.show()
    sys.exit(app.exec_())




    ############ 수정 방법 1 ############## -> 해결 안됨