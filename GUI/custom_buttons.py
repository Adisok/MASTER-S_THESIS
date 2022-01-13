from PyQt5.QtCore import Qt, QMimeData, QDataStream, QByteArray, QIODevice, pyqtSignal
from PyQt5.QtGui import QDrag
from PyQt5.QtWidgets import QPushButton, QMenu


class Button(QPushButton):
    moved = pyqtSignal()
    connectionRequested = pyqtSignal(QPushButton)

    def __init__(self, title, second_title=None, group=None, image_path=None, parent=None, width=100):
        super().__init__(title, parent)
        self.second_title = second_title
        self.title = title
        self.group_name=group
        self.setFixedHeight(100)
        self.setFixedWidth(100)
        if "valve" in image_path:
            self.setFixedWidth(150)
        self.image_path = image_path
        if image_path is not None:
            self.setStyleSheet(f"background-image : url({self.image_path});")
        self.setAcceptDrops(True)
        if self.second_title is not None:
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.showMenu)

        self.state = 0


    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            mimeData = QMimeData()
            drag = QDrag(self)
            drag.setMimeData(mimeData)
            drag.setHotSpot(e.pos())

            byteArray = QByteArray()
            stream = QDataStream(byteArray, QIODevice.WriteOnly)
            stream.writeQString(f'{self.title}, {self.second_title}, {self.group_name}')
            mimeData.setData('myApp/QtWidget', byteArray)

            drag.exec_(Qt.MoveAction)

            self.moved.emit()


    def showMenu(self):
        menu = QMenu()
        menu.addAction("connect", lambda: self.connectionRequested.emit(self))
        menu.exec_(self.cursor().pos())
