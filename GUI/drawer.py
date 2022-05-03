from PyQt5.QtCore import Qt, QRectF, QLineF
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsView, QMenu, QGraphicsLineItem
from PyQt5.QtGui import QPainterPathStroker

from GUI.custom_buttons import Button


class GraphicsLineItem(QGraphicsLineItem):
    def __init__(self, source, destination, parent=None):
        super().__init__(parent)
        self.source = source
        self.destination = destination

        self.move()

        self.source.moved.connect(self.move)
        self.destination.moved.connect(self.move)

    def contextMenuEvent(self, event):
        menu = QMenu()
        menu.addAction("Delete", self.remove)
        menu.exec_(self.cursor().pos())

    def remove(self):
        self.scene().removeItem(self)

    def shape(self):
        p = super(GraphicsLineItem, self).shape()
        stroker = QPainterPathStroker()
        stroker.setWidth(20)
        return stroker.createStroke(p)

    def move(self):
        self.setLine(QLineF(self.source.pos(), self.destination.pos()))


class Drawer(QGraphicsView):
    def __init__(self, parent=None):
        super(Drawer, self).__init__(parent)
        self.setScene(QGraphicsScene(self))
        self.setAcceptDrops(True)
        self.setSceneRect(QRectF(self.viewport().rect()))
        self.source = None
        self.buttons = []
        self.valves_count = 0
        self.pistons_count = 0

    def return_values(self, process_algorithm_maker):
        """
        Zwraca algorytm sterowania krok po kroku
        :return:
        """
        algorithm = process_algorithm_maker.make_algorithm()
        flow = [algorithm_part for algorithm_part in algorithm]
        return flow

    def add_button(self, button_to_add, position, image_path):
        if "valve" in image_path:
            self.buttons.append(
                Button(
                    title=str(button_to_add),
                    second_title=self.valves_count,
                    image_path=image_path,
                    parent=self,
                )
            )
            self.valves_count += 1
        if "piston" in image_path:
            self.buttons.append(
                Button(
                    title=str(button_to_add),
                    second_title=self.pistons_count,
                    image_path=image_path,
                    parent=self,
                )
            )
            self.pistons_count += 1

        self.buttons[-1].move(position)
        self.buttons[-1].connectionRequested.connect(self.connectButton)
        self.buttons[-1].show()

    def dragEnterEvent(self, e):
        e.accept()

    def dragMoveEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        btn = e.source()
        position = e.pos()
        if btn not in self.buttons:
            self.add_button(btn.title, position=position, image_path=btn.image_path)
        else:
            btn.move(position)
        e.setDropAction(Qt.MoveAction)
        e.accept()

    def clearScene(self):
        self.scene().clear()
        self.source = None

    def connectButton(self, button):
        # Do not connect a button with itself
        if not self.source or button == self.source:
            self.source = button
            return
        line = GraphicsLineItem(self.source, button)
        self.scene().addItem(line)
        self.source = None
