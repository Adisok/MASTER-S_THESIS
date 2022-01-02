from PyQt5.QtCore import Qt, QMimeData, QDataStream, QByteArray, QIODevice
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):

    def __init__(self, title):
        super().__init__(title)
        self.title = title
        self.setFixedHeight(100)
        self.setFixedWidth(100)
        self.setStyleSheet(f"background-image : url(GUI/images/test.jpg);")

    def mouseMoveEvent(self, e):

        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos())

        byteArray = QByteArray()
        stream = QDataStream(byteArray, QIODevice.WriteOnly)
        stream.writeQString(self.title)
        mimeData.setData('myApp/QtWidget', byteArray)

        dropAction = drag.exec_(Qt.MoveAction)
