import sys
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel, QSizePolicy, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import locale
locale.setlocale(locale.LC_ALL, 'ko_KR.UTF-8')

# 1920x1080 기준

# 예/아니오 안내문 클래스
class CustomMessageBox(QDialog):
    def __init__(self, text, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        label = QLabel(text)
        label.setWordWrap(True)
        label.setStyleSheet("font-size: 50px;")
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(label)

        button_layout = QHBoxLayout()

        yes_button = QPushButton("예")
        yes_button.setFixedSize(100, 50)
        yes_button.clicked.connect(self.accept)
        button_layout.addWidget(yes_button)

        no_button = QPushButton("아니오")
        no_button.setFixedSize(100, 50)
        no_button.clicked.connect(self.reject)
        button_layout.addWidget(no_button)

        layout.addLayout(button_layout)
        
        # 다이얼로그의 크기 조절
        self.setFixedSize(700, 300)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()


        # 상품 정보
        self.products = [
            Product('칸쵸', 980),
            Product('허니버터칩', 1600),
            Product('썬칩', 1400)
        ]

        # 최근 목록을 표시할 TableWidget
        self.recentTableWidget = QTableWidget(self)
        self.recentTableWidget.setColumnCount(2)
        self.recentTableWidget.setHorizontalHeaderLabels(['상품', '가격'])

        # 열 너비 설정
        self.recentTableWidget.setColumnWidth(0, 350)
        self.recentTableWidget.setColumnWidth(1, 250)

        # 크기 설정
        self.recentTableWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.recentTableWidget.setMinimumWidth(600)
        self.recentTableWidget.setMinimumHeight(300)

        # 추가 정보를 담을 위젯 (QLabel 사용)
        self.additionalInfoWidget = QLabel('추가 정보를 여기에 표시\n광고, 쿠폰, 안내문 등\n\n\n\n\n\n\n', self)
        self.additionalInfoWidget.setFont(QFont('Arial', 30))
        self.additionalInfoWidget.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.additionalInfoWidget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1920, 1080)
        self.setWindowTitle('스마트 카트 GUI')

        # 전체 레이아웃
        main_layout = QVBoxLayout(self)

        # 상단 레이아웃
        top_layout = QHBoxLayout()

        # 테이블 위젯
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnCount(6)

        # 열 이름 설정
        self.tableWidget.setHorizontalHeaderLabels(['상품', '', '수량', '', '가격', ''])

        # 열 너비 설정
        self.tableWidget.setColumnWidth(0, 490)
        self.tableWidget.setColumnWidth(1, 140)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 140)
        self.tableWidget.setColumnWidth(4, 265)
        self.tableWidget.setColumnWidth(5, 120)

        top_layout.addWidget(self.tableWidget, 2)
        main_layout.addLayout(top_layout)

        # 제품 버튼 추가 (추후 버튼 제거 예정)
        button_layout = QHBoxLayout()
        self.kanchoButton = QPushButton('칸쵸', self)
        self.kanchoButton.setFixedSize(100, 50)
        self.kanchoButton.clicked.connect(lambda _, index=0: self.handleProductButton(index))

        self.honeychipButton = QPushButton('허니버터칩', self)
        self.honeychipButton.setFixedSize(100, 50)
        self.honeychipButton.clicked.connect(lambda _, index=1: self.handleProductButton(index))

        self.ssunchipButton = QPushButton('썬칩', self)
        self.ssunchipButton.setFixedSize(100, 50)
        self.ssunchipButton.clicked.connect(lambda _, index=2: self.handleProductButton(index))

        button_layout.addWidget(self.kanchoButton)
        button_layout.addWidget(self.honeychipButton)
        button_layout.addWidget(self.ssunchipButton)

        main_layout.addLayout(button_layout)

        # 총합 가격 레이블
        self.totalPriceLabel = QLabel('총 액 : 0 원', self)
        self.totalPriceLabel.setStyleSheet("QLabel { color : red; font-size: 80px; font-weight: bold; }")
        main_layout.addWidget(self.totalPriceLabel, alignment=Qt.AlignmentFlag.AlignRight)

        # 최근 목록 및 추가 정보 레이아웃
        recent_layout = QVBoxLayout()
        recent_label = QLabel('최근 목록', self)
        recent_label.setFont(QFont('Arial', 30))
        recent_layout.addWidget(recent_label)
        recent_layout.addWidget(self.recentTableWidget)

        # 최근 목록 아래에 추가 정보를 담을 위젯 추가
        recent_layout.addWidget(self.additionalInfoWidget)

        top_layout.addLayout(recent_layout)
        main_layout.addLayout(recent_layout)

    def handleProductButton(self, product_index):
        existing_rows = [row for row in range(self.tableWidget.rowCount()) if self.tableWidget.item(row, 0).text() == self.products[product_index].name]

        if existing_rows:
            # 이미 추가된 상품이라면 변화 X
            pass
        else:
            # 추가된 상품이 아니라면 행 추가
            self.addProductRow(product_index)

    def updatePrice(self, row):
        # 현재 행의 상품명 가져오기
        currentProduct = self.tableWidget.item(row, 0).text()

        # 현재 행의 수량 가져오기
        currentQuantity = int(self.tableWidget.item(row, 2).text())

        # 현재 행의 상품 가격 가져오기
        currentProductPrice = next((product.price for product in self.products if product.name == currentProduct), 0)

        # 가격 계산
        newPrice = currentQuantity * currentProductPrice

        # 기존에 가격 아이템이 있는지 확인
        price_item = self.tableWidget.item(row, 4)

        if price_item is None:
            # 가격 아이템이 없을 때 새로 생성하여 추가
            price_str = locale.format_string("%d", newPrice, grouping=True) + ' 원'
            price_item = QTableWidgetItem(price_str)
            price_item.setFont(QFont('Arial', 30))
            self.tableWidget.setItem(row, 4, price_item)
        else:
            # 가격 아이템이 이미 있는 경우 업데이트
            price_item.setText(locale.format_string("%d", newPrice, grouping=True) + ' 원')

    def addProductRow(self, product_index):
        existing_rows = [row for row in range(self.tableWidget.rowCount()) if self.tableWidget.item(row, 0).text() == self.products[product_index].name]

        if existing_rows:
            # 이미 추가된 상품이라면 기존 행에서 수량만 증가
            rowPosition = existing_rows[0]
            currentQuantity = int(self.tableWidget.item(rowPosition, 2).text())
            newQuantity = min(currentQuantity + 1, 99)
            self.tableWidget.item(rowPosition, 2).setText(str(newQuantity))

            # 이미 존재하는 행에 대해 PushButton 시그널 연결 업데이트
            self.updatePushButtonConnections(rowPosition)
        else:
            # 추가된 상품이 아니라면 새로운 행 추가
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)

            # 현재 누른 버튼에 해당하는 상품 정보 가져오기
            currentProduct = self.products[product_index]

            # 상품명, 수량, 가격 설정
            item_name = QTableWidgetItem(currentProduct.name)
            item_name.setFont(QFont('Arial', 55, QFont.Bold))
            self.tableWidget.setItem(rowPosition, 0, item_name)

            # '-' 버튼 생성
            minusButton = QPushButton('-', self)
            minusButton.clicked.connect(lambda _, row=rowPosition: self.adjustQuantity(row, -1))
            minusButton.setFont(QFont('Arial', 40, QFont.Bold))
            self.tableWidget.setCellWidget(rowPosition, 1, minusButton)

            # 수량 표시 레이블
            currentQuantityItem = self.tableWidget.item(rowPosition, 2)
            currentQuantity = int(currentQuantityItem.text()) if currentQuantityItem else 1
            quantityLabel = QTableWidgetItem(str(currentQuantity))
            quantityLabel.setFont(QFont('Arial', 40))
            quantityLabel.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(rowPosition, 2, quantityLabel)

            # '+' 버튼 생성
            plusButton = QPushButton('+', self)
            plusButton.clicked.connect(lambda _, row=rowPosition: self.adjustQuantity(row, 1))
            plusButton.setFont(QFont('Arial', 40, QFont.Bold))
            self.tableWidget.setCellWidget(rowPosition, 3, plusButton)

            # 삭제 버튼 생성
            deleteButton = QPushButton('삭제', self)
            deleteButton.clicked.connect(lambda _, row=rowPosition: self.removeRow(row))
            deleteButton.setFont(QFont('Arial', 30, QFont.Bold))
            self.tableWidget.setCellWidget(rowPosition, 5, deleteButton)

            # 초기 수량에 따라 가격 계산
            self.updatePrice(rowPosition)
            self.updatePushButtonConnections(rowPosition)

            # 행 높이 설정
            desired_height = 140
            self.tableWidget.setRowHeight(rowPosition, desired_height)

            # 최근 목록에도 추가, 상품 가격 업데이트
            self.addToRecentTable(currentProduct.name, currentProduct.price)
            self.updateTotalPrice()

    def updatePushButtonConnections(self, row):
        # '-' 버튼
        minusButton = self.tableWidget.cellWidget(row, 1)
        if minusButton:
            minusButton.clicked.disconnect()
            minusButton.clicked.connect(lambda _, row=row: self.adjustQuantity(row, -1))

        # '+' 버튼
        plusButton = self.tableWidget.cellWidget(row, 3)
        if plusButton:
            plusButton.clicked.disconnect()
            plusButton.clicked.connect(lambda _, row=row: self.adjustQuantity(row, 1))

        # 삭제 버튼
        deleteButton = self.tableWidget.cellWidget(row, 5)
        if deleteButton:
            deleteButton.clicked.disconnect()
            deleteButton.clicked.connect(lambda _, row=row: self.removeRow(row))

    def adjustQuantity(self, row, delta):
        currentQuantityItem = self.tableWidget.item(row, 2)
        if currentQuantityItem is not None:
            currentQuantity = int(currentQuantityItem.text())
            newQuantity = max(min(currentQuantity + delta, 99), 1)
            currentQuantityItem.setText(str(newQuantity))
            self.updatePrice(row)

            if newQuantity == 1:
                self.removeRow(row)
            else:
                currentQuantityItem.setText(str(newQuantity))
                self.updatePrice(row)
                self.updateTotalPrice()

    def removeRow(self, row):
        if self.tableWidget.item(row, 0) is None:
            return

        itemName = self.tableWidget.item(row, 0).text()

        # 사용자에게 확인을 받고 삭제 여부 결정
        custom_message_box = CustomMessageBox(f'"{itemName}"을(를) 삭제하시겠습니까?', self)
        result = custom_message_box.exec_()

        if result == QDialog.Accepted:
            # 삭제된 행 이후의 행들의 인덱스를 조정
            for i in range(row, self.tableWidget.rowCount()):
                if self.tableWidget.item(i, 2) is not None:
                    # 수량 조절 기능
                    currentQuantity = int(self.tableWidget.item(i, 2).text())
                    newQuantity = max(currentQuantity, 0)
                    self.tableWidget.item(i, 2).setText(str(newQuantity))

                    # 가격 업데이트
                    self.updatePrice(i)

            # 행 삭제 기능
            self.tableWidget.removeRow(row)

            # 총합 가격 업데이트
            self.updateTotalPrice()

            # 행 삭제 후 푸쉬버튼 연결 업데이트
            for i in range(row, self.tableWidget.rowCount()):
                self.updatePushButtonConnections(i)

    def updateTotalPrice(self):
        total_price = sum([int(item.text().replace(',', '').replace('원', '')) for row in range(self.tableWidget.rowCount()) for item in [self.tableWidget.item(row, 4)]])
        formatted_price = locale.format_string("%d", total_price, grouping=True)
        self.totalPriceLabel.setStyleSheet("QLabel { color : red; font-size: 80px; font-weight: bold; }")
        self.totalPriceLabel.setText(f'총 액 : {formatted_price} 원')

    def addToRecentTable(self, name, price):
        # 최근 목록에 추가
        rowPosition = 0
        self.recentTableWidget.insertRow(rowPosition)

        name_item = QTableWidgetItem(name)
        price_str = locale.format_string("%d", price, grouping=True) + ' 원'
        price_item = QTableWidgetItem(str(price_str))
        self.recentTableWidget.setItem(rowPosition, 0, name_item)
        self.recentTableWidget.setItem(rowPosition, 1, price_item)

        # 스크롤을 최상단으로 이동시켜서 가장 최근에 추가된 항목이 상단에 나타나도록 함
        vertical_scrollbar = self.recentTableWidget.verticalScrollBar()
        vertical_scrollbar.setValue(vertical_scrollbar.minimum())

        # 행 높이 설정
        desired_height = 60
        self.recentTableWidget.setRowHeight(rowPosition, desired_height)

        # 글자 크기 설정
        font = QFont('Arial', 25)  
        name_item.setFont(font)
        price_item.setFont(font)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.showFullScreen()
    sys.exit(app.exec_())