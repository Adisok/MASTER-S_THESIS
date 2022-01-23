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
        self.group_name = group
        self.setFixedHeight(100)
        self.setFixedWidth(100)
        self.image_path = image_path
        if "valve" in self.image_path:
            self.setFixedWidth(150)
        if "mono" in self.image_path or "bi" in self.image_path:
            if self.second_title == 0:
                self.state = 1  # Y1 i not(Y1)
            else:
                self.state = 0
        elif "piston" in self.image_path:
            self.left_state = 1
            self.right_state = 0
            if self.second_title is not None:
                self.left_index = self.second_title * 2 + 1
                self.right_index = self.left_index + 1

        if image_path is not None:
            self.setStyleSheet(f"background-image : url({image_path});border :3px solid white")
        if self.second_title is not None:
            self.setContextMenuPolicy(Qt.CustomContextMenu)
            self.customContextMenuRequested.connect(self.showMenu)
        self.setAcceptDrops(True)

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
        menu.addAction("change_initial_state", lambda: self.change_state())
        menu.exec_(self.cursor().pos())

    def change_state(self, wchich_one=None):
        if "piston" in self.image_path:
            if wchich_one == "left":
                self.left_state = int(not(self.left_state))
            elif wchich_one == "right":
                self.right_state = int(not(self.right_state))
        elif "mono" in self.image_path or "bi" in self.image_path:
            self.state = int(not(self.state))

    def change_picture(self):
        self.setStyleSheet(f"background-image : url(GUI/images/piston{self.left_state}); border :3px solid white")
        self.change_state()

