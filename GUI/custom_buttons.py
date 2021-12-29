import sys

from PyQt5.QtCore import Qt, QMimeData, QDataStream, QByteArray, QIODevice
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton, QWidget, QApplication

class Button(QPushButton):

    def __init__(self, title):
        super().__init__(title)
        self.title = title

    def mouseMoveEvent(self, e):

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos() - self.rect().topLeft())

        byteArray = QByteArray()
        stream = QDataStream(byteArray, QIODevice.WriteOnly)
        stream.writeQString(self.title)
        mimeData.setData('myApp/QtWidget', byteArray)

        dropAction = drag.exec_(Qt.MoveAction)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)

        self.button = Button('Button', self)
        self.button.move(100, 65)

        self.setWindowTitle('Click or Move')
        self.setGeometry(300, 300, 550, 450)

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        position = e.pos()
        self.button.move(position)

        e.setDropAction(Qt.MoveAction)
        e.accept()


def main():
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()


if __name__ == '__main__':
    main()