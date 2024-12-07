from random import randint
from sys import argv, exit

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QPoint


class CircleRandomColor(QMainWindow):

    def __init__(self) -> None:

        super().__init__()
        uic.loadUi('UI.ui', self)  # Я бы подключил ui файл, как класс python, но у меня нет pyuic6 :(
        self.ready = False
        self.initUI()

        self.Button: QPushButton

    def initUI(self) -> None:

        self.setGeometry(150, 150, 500, 500)
        self.setWindowTitle('Желтые окружности')
        self.Button.clicked.connect(self.draw_circle)

    def draw_circle(self) -> None:

        self.ready = True
        self.update()

    def paintEvent(self, a0) -> None:

        if not self.ready:

            return None

        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        x_coord = randint(0, 500)
        y_coord = randint(0, 500)
        radius = randint(0, 50)

        qp = QPainter()

        qp.begin(self)
        qp.setBrush(color)
        qp.drawEllipse(QPoint(x_coord, y_coord), radius, radius)

        qp.end()

        self.ready = False


if __name__ == '__main__':

    app = QApplication(argv)
    circle = CircleRandomColor()
    circle.show()
    exit(app.exec())
