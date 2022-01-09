from PyQt5.QtCore import Qt, QMimeData, QDataStream, QByteArray, QIODevice, pyqtSignal
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton


class Button(QPushButton):
    moved = pyqtSignal()

    def __init__(self, title, second_title=None, group=None ,image_path=None):
        super().__init__(title)
        self.second_title = second_title
        self.title = title
        self.group_name=group
        self.setFixedHeight(100)
        self.setFixedWidth(100)
        if image_path is not None:
            self.setStyleSheet(f"background-image : url({image_path});")
        self.setAcceptDrops(True)


    def mouseMoveEvent(self, e):
        if e.buttons() != Qt.LeftButton:
            return
        mimeData = QMimeData()

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setHotSpot(e.pos())

        byteArray = QByteArray()
        stream = QDataStream(byteArray, QIODevice.WriteOnly)
        stream.writeQString(f'{self.title}, {self.second_title}, {self.group_name}')
        mimeData.setData('myApp/QtWidget', byteArray)

        dropAction = drag.exec_(Qt.MoveAction)
