import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        loadUi('qtpy_1.ui', self)  # your_ui_file.ui에는 디자인한 UI의 파일명을 넣어야 함

        self.counter = 0  # 텍스트의 초기값

        # '+' 버튼 클릭 시 이벤트 연결
        self.pushButtonPlus.clicked.connect(self.increment)

        # '-' 버튼 클릭 시 이벤트 연결
        self.pushButtonMinus.clicked.connect(self.decrement)

    def increment(self):
        self.counter += 1
        self.update_label()

    def decrement(self):
        self.counter -= 1
        self.update_label()

    def update_label(self):
        self.label.setText(str(self.counter))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyCalculator()
    window.show()
    sys.exit(app.exec_())

