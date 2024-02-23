import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt, QTimer, pyqtSignal, pyqtSlot
from PyQt5.QtGui import QFont, QImage, QPixmap

# 카메라
class Camera(QWidget):
    update_frame_signal = pyqtSignal(QImage)

    def __init__(self):
        super().__init__()

        self.init_ui()
        self.init_camera()

    def init_ui(self):
        self.setWindowTitle('Camera')
        self.setGeometry(800, 20, 300, 300)

        # 이미지를 표시할 라벨
        self.label = QLabel(self)
        self.label.setFixedSize(500, 500)
        self.label.setAlignment(Qt.AlignTop | Qt.AlignRight)

        # 텍스트를 표시할 라벨
        self.text_label = QLabel("사용 방법 \n 1. 전원을 켜고 사용자 등록을 해주세요.\n 2. 물건을 담고 수량 조절을 해주세요.\n 3. 마지막으로 수량과 합산액이 맞는지 확인하여 주세요.", self)
        self.text_label.setAlignment(Qt.AlignBottom | Qt.AlignCenter)

        # 수직 레이아웃에 이미지 라벨과 텍스트 라벨 추가
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.text_label)

    def init_camera(self):
        self.cap = cv2.VideoCapture(0)  # 카메라 장치 번호 (0은 기본 카메라)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(50)  # 50ms마다 업데이트

    def update_frame(self):
        ret, frame = self.cap.read()

        if ret:
            rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            h, w, ch = rgb_image.shape
            bytes_per_line = ch * w
            qt_image = QImage(rgb_image.data, w, h, bytes_per_line, QImage.Format_RGB888)

            self.update_frame_signal.emit(qt_image)

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

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 1280, 800)
        self.setWindowTitle('스마트 카트 GUI')
    
        # 전체 레이아웃
        main_layout = QVBoxLayout(self)

        # 상단 레이아웃
        top_layout = QHBoxLayout()

        # 카메라 레이아웃
        camera_layout = QVBoxLayout()
        self.camera_widget = Camera()
        self.camera_widget.update_frame_signal.connect(self.update_camera_frame)
        camera_layout.addWidget(self.camera_widget, 1, alignment=Qt.AlignmentFlag.AlignTop)
        top_layout.addLayout(camera_layout)

        # 테이블 위젯
        self.tableWidget = QTableWidget(self)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setColumnCount(6)

        # 열 이름 설정
        self.tableWidget.setHorizontalHeaderLabels(['상품', '', '수량', '', '가격', ''])

        # 열 너비 설정
        self.tableWidget.setColumnWidth(0, 260)  # 상품 열
        self.tableWidget.setColumnWidth(1, 25)  # '-' 버튼 열
        self.tableWidget.setColumnWidth(2, 130)  # 수량 열
        self.tableWidget.setColumnWidth(3, 25)  # '+' 버튼 열
        self.tableWidget.setColumnWidth(4, 130)  # 가격 열
        self.tableWidget.setColumnWidth(5, 65)  # '삭제' 버튼 열

        top_layout.addWidget(self.tableWidget, 2)
        main_layout.addLayout(top_layout)

        # 제품 버튼 추가
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
        self.totalPriceLabel = QLabel('총합 가격: 0원', self)
        self.totalPriceLabel.setFont(QFont('Arial', 20))
        main_layout.addWidget(self.totalPriceLabel, alignment=Qt.AlignmentFlag.AlignRight)

    @pyqtSlot(QImage)
    def update_camera_frame(self, qt_image):
        pixmap = QPixmap.fromImage(qt_image)
        self.camera_widget.label.setPixmap(pixmap)

    def handleProductButton(self, product_index):
        existing_rows = [row for row in range(self.tableWidget.rowCount()) if self.tableWidget.item(row, 0).text() == self.products[product_index].name]

        if existing_rows:
            # 이미 추가된 상품이라면 변화 X
            pass
        else:
            # 추가된 상품이 아니라면 행 추가
            self.addProductRow(product_index)

    def addProductRow(self, product_index):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

        # 현재 누른 버튼에 해당하는 상품 정보 가져오기
        currentProduct = self.products[product_index]

        # 상품명, 수량, 가격 설정
        item_name = QTableWidgetItem(currentProduct.name)
        self.tableWidget.setItem(rowPosition, 0, item_name)

        # '-' 버튼 생성
        minusButton = QPushButton('-', self)
        minusButton.clicked.connect(lambda _, row=rowPosition: self.adjustQuantity(row, -1))
        self.tableWidget.setCellWidget(rowPosition, 1, minusButton)

        # 수량 표시 레이블
        quantityLabel = QTableWidgetItem('1')
        self.tableWidget.setItem(rowPosition, 2, quantityLabel)

        # '+' 버튼 생성
        plusButton = QPushButton('+', self)
        plusButton.clicked.connect(lambda _, row=rowPosition: self.adjustQuantity(row, 1))
        self.tableWidget.setCellWidget(rowPosition, 3, plusButton)

        # 삭제 버튼 생성
        deleteButton = QPushButton('삭제', self)
        deleteButton.clicked.connect(lambda _, row=rowPosition: self.removeRow(row))
        self.tableWidget.setCellWidget(rowPosition, 5, deleteButton)

        # 초기 수량에 따라 가격 계산
        self.updatePrice(rowPosition)

    def adjustQuantity(self, row, amount):
        # 수량 조절 기능
        currentQuantity = int(self.tableWidget.item(row, 2).text())
        newQuantity = max(currentQuantity + amount, 0)
        self.tableWidget.item(row, 2).setText(str(newQuantity))

        # 수량이 변경될 때마다 가격 업데이트
        self.updatePrice(row)

    def updatePrice(self, row):
        # 가격 업데이트
        item_name = self.tableWidget.item(row, 0).text()
        currentProduct = next((product for product in self.products if product.name == item_name), None)

        if currentProduct:
            currentQuantity = int(self.tableWidget.item(row, 2).text())
            newPrice = currentProduct.price * currentQuantity

            # 가격 아이템이 없을 때에는 새로 생성
            price_item = self.tableWidget.item(row, 4)
            if price_item is None:
                price_item = QTableWidgetItem(str(newPrice))
                self.tableWidget.setItem(row, 4, price_item)
            else:
                price_item.setText(str(newPrice))

        # 총합 가격 업데이트
        total_price = sum([int(self.tableWidget.item(i, 4).text()) for i in range(self.tableWidget.rowCount())])
        self.totalPriceLabel.setText(f'총합 가격: {total_price}원')

    def removeRow(self, row):
        # 행 삭제 기능
        self.tableWidget.removeRow(row)

        # 삭제된 행 이후의 행들의 인덱스를 조정
        for i in range(row, self.tableWidget.rowCount()):
            # 수량 조절 기능
            currentQuantity = int(self.tableWidget.item(i, 2).text())
            newQuantity = max(currentQuantity, 0)
            self.tableWidget.item(i, 2).setText(str(newQuantity))

            # 가격 업데이트
            currentProduct = next((product for product in self.products if product.name == self.tableWidget.item(i, 0).text()), None)

            if currentProduct:
                currentQuantity = int(self.tableWidget.item(i, 2).text())
                newPrice = currentProduct.price * currentQuantity

                # 가격 아이템이 없을 때에는 새로 생성
                price_item = self.tableWidget.item(i, 4)
                if price_item is None:
                    price_item = QTableWidgetItem(str(newPrice))
                    self.tableWidget.setItem(i, 4, price_item)
                else:
                    price_item.setText(str(newPrice))

        # 총합 가격 업데이트
        total_price = sum([int(self.tableWidget.item(i, 4).text()) for i in range(self.tableWidget.rowCount())])
        self.totalPriceLabel.setText(f'총합 가격: {total_price}원')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec_())