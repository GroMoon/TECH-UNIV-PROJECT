# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtpy_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Calcu_1(object):
    def setupUi(self, Calcu_1):
        Calcu_1.setObjectName("Calcu_1")
        Calcu_1.resize(800, 600)
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

###################카운팅 +-####################
        self.minus_1 = QtWidgets.QPushButton(self.centralwidget)
        self.minus_1.setGeometry(QtCore.QRect(220, 120, 75, 23))
        self.minus_1.setObjectName("minus_1")
        self.minus_1.clicked.connect(lambda: self.minus(0))
        self.plus_1 = QtWidgets.QPushButton(self.centralwidget)
        self.plus_1.setGeometry(QtCore.QRect(390, 120, 75, 23))
        self.plus_1.setObjectName("plus_1")
        self.plus_1.clicked.connect(lambda: self.plus(0))
        self.minus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.minus_2.setGeometry(QtCore.QRect(220, 190, 75, 23))
        self.minus_2.setObjectName("minus_2")
        self.minus_2.clicked.connect(lambda: self.minus(1))
        self.plus_2 = QtWidgets.QPushButton(self.centralwidget)
        self.plus_2.setGeometry(QtCore.QRect(390, 190, 75, 23))
        self.plus_2.setObjectName("plus_2")
        self.plus_2.clicked.connect(lambda: self.plus(1))
        self.minus_3 = QtWidgets.QPushButton(self.centralwidget)
        self.minus_3.setGeometry(QtCore.QRect(220, 260, 75, 23))
        self.minus_3.setObjectName("minus_3")
        self.minus_3.clicked.connect(lambda: self.minus(2))
        self.plus_3 = QtWidgets.QPushButton(self.centralwidget)
        self.plus_3.setGeometry(QtCore.QRect(390, 260, 75, 23))
        self.plus_3.setObjectName("plus_3")
        self.plus_3.clicked.connect(lambda: self.plus(2))
        self.minus_4 = QtWidgets.QPushButton(self.centralwidget)
        self.minus_4.setGeometry(QtCore.QRect(220, 330, 75, 23))
        self.minus_4.setObjectName("minus_4")
        self.minus_4.clicked.connect(lambda: self.minus(3))
        self.plus_4 = QtWidgets.QPushButton(self.centralwidget)
        self.plus_4.setGeometry(QtCore.QRect(390, 330, 75, 23))
        self.plus_4.setObjectName("plus_4")
        self.plus_4.clicked.connect(lambda: self.plus(3))
        #######################################

##############가격 계산#############
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 461, 41))
        self.label.setObjectName("label")
        self.Price_1 = QtWidgets.QLabel(self.centralwidget)
        self.Price_1.setGeometry(QtCore.QRect(670, 115, 101, 41))
        self.Price_1.setObjectName("Price_1")
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Price_1.setFont(font)
        self.Price_1.setText("")
        self.Price_1.setObjectName("Price_1")
        self.Price_2 = QtWidgets.QLabel(self.centralwidget)
        self.Price_2.setGeometry(QtCore.QRect(670, 185, 101, 31))
        self.Price_2.setObjectName("Price_2")
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Price_2.setFont(font)
        self.Price_2.setText("")
        self.Price_2.setObjectName("Price_2")
        self.Price_3 = QtWidgets.QLabel(self.centralwidget)
        self.Price_3.setGeometry(QtCore.QRect(670, 255, 101, 31))
        self.Price_3.setObjectName("Price_3")
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Price_3.setFont(font)
        self.Price_3.setText("")
        self.Price_3.setObjectName("Price_3")
        self.Price_4 = QtWidgets.QLabel(self.centralwidget)
        self.Price_4.setGeometry(QtCore.QRect(670, 325, 101, 31))
        self.Price_4.setObjectName("Price_4")
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Price_4.setFont(font)
        self.Price_4.setText("")
        self.Price_4.setObjectName("Price_4")
        self.textEdit_12 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_12.setGeometry(QtCore.QRect(60, 50, 81, 41))
        self.textEdit_12.setObjectName("textEdit_12")
        self.Price_sum = QtWidgets.QLabel(self.centralwidget)
        self.Price_sum.setGeometry(QtCore.QRect(570, 510, 151, 41))
        self.Price_sum.setObjectName("Price_sum")
##################### 개수 카운팅(시각적 라벨) ###############
        self.count = [0, 0, 0, 0]

        self.Count_1 = QtWidgets.QLabel(self.centralwidget)
        self.Count_1.setGeometry(QtCore.QRect(310, 110, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Count_1.setFont(font)
        self.Count_1.setText("")
        self.Count_1.setObjectName("Count_1")

        self.Count_2 = QtWidgets.QLabel(self.centralwidget)
        self.Count_2.setGeometry(QtCore.QRect(310, 180, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Count_2.setFont(font)
        self.Count_2.setText("")
        self.Count_2.setObjectName("Count_2")

        self.Count_3 = QtWidgets.QLabel(self.centralwidget)
        self.Count_3.setGeometry(QtCore.QRect(310, 250, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Count_3.setFont(font)
        self.Count_3.setText("")
        self.Count_3.setObjectName("Count_3")

        self.Count_4 = QtWidgets.QLabel(self.centralwidget)
        self.Count_4.setGeometry(QtCore.QRect(310, 320, 61, 41))
        font = QtGui.QFont()
        font.setFamily("AcadEref")
        font.setPointSize(14)
        self.Count_4.setFont(font)
        self.Count_4.setText("")
        self.Count_4.setObjectName("Count_4")
##########################################################

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
        self.minus_2.setText(_translate("Calcu_1", "-"))
        self.plus_2.setText(_translate("Calcu_1", "+"))
        self.minus_3.setText(_translate("Calcu_1", "-"))
        self.plus_3.setText(_translate("Calcu_1", "+"))
        self.minus_4.setText(_translate("Calcu_1", "-"))
        self.plus_4.setText(_translate("Calcu_1", "+"))
        self.label.setText(_translate("Calcu_1", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">갯수 +- 와 자동으로 합산액을 나타내어 준다.</span></p></body></html>"))
        self.textEdit_12.setHtml(_translate("Calcu_1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">물  건</span></p></body></html>"))
### +- 계산 함수###################
    def plus(self, index):
        self.count[index] += 1
        self.update_label()

    def minus(self, index):
        if self.count[index] > 0:
            self.count[index] -= 1
        self.update_label()
        
################################### 데이터 업데이트 
    def update_label(self):
        self.Count_1.setText(str(self.count[0]) + " 개")
        self.Count_2.setText(str(self.count[1]) + " 개")
        self.Count_3.setText(str(self.count[2]) + " 개")
        self.Count_4.setText(str(self.count[3]) + " 개")
        self.Price_1.setText(str(self.count[0] * 500) + " 원")
        

# 해야될 거 >> 영수증 참고해서 뭐시기
# >> 상품 받아오기 + 상품 정보 담기
# >> 카운팅 한번에 안되도록(알파요소)
# 1. 카메라로부터 값을 받아옴 >> 2. 받아온 값 == 저장된 상품값이면 GUI 표시 >> 3. 항목별 내림올림

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calcu_1 = QtWidgets.QMainWindow()
    ui = Ui_Calcu_1()
    ui.setupUi(Calcu_1)
    Calcu_1.show()
    sys.exit(app.exec_())