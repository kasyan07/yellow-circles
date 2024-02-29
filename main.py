from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
import sys
import random


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.drawing = False
        self.setWindowTitle('Окружность')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        self.drawing = True
        self.update()

    def paintEvent(self, event):
        self.size = random.randint(10, 100)
        if self.drawing:
            painter = QPainter()
            painter.begin(self)
            painter.setPen(QColor(255, 201, 14))
            painter.setBrush(QColor(255, 201, 14))
            self.x, self.y = random.randint(0, 500), random.randint(0, 500)
            painter.drawEllipse(self.x, self.y, self.size, self.size)
            painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
