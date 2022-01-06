from PyQt5.QtCore import Qt, QLine, QPoint
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPen, QImage, QColor
from numpy import ones, vstack
from numpy.linalg import lstsq


class Drawer(QWidget):

    def __init__(self, parent=None):
        super(Drawer, self).__init__(parent)
        self.j = 0
        self.firstPoint = self.lastPoint = None
        self.lines = dict()
        self.pairs_buttons_and_list = dict()
        self.reset_image()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.firstPoint = event.pos()
        if event.button() == Qt.RightButton:
            mouse_pos = event.pos()
            for i in range(len(self.lines)):
                if mouse_pos.y() > self.lines[i][1](x=mouse_pos.x())+10 \
                        or mouse_pos.y() > self.lines[i][1](x=mouse_pos.x())-10:
                    try:
                        self.lines[i] = self.lines[i+1]
                    except KeyError:
                        del self.lines[i]
            self.reset_image()
            self.updateImage()

    def mouseMoveEvent(self, event):
        if self.firstPoint:
            self.lastPoint = event.pos()
            self._line = QLine(self.firstPoint, self.lastPoint)
            self.update()

    def mouseReleaseEvent(self, event):
        buttons = self.children()[1:]
        if len(buttons) > 0 and self.lastPoint:
            for i in buttons:
                if ((x := i.x()) + i.width() > self.lastPoint.x() > x and (y := i.y()) + i.height() > self.lastPoint.y() > y):
                    self.connect_line_and_button(i, self._line)

        if self.firstPoint and self.lastPoint:
            self.updateImage()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        dirtyRect = event.rect()
        painter.drawImage(dirtyRect, self.image, dirtyRect)
        if self.firstPoint and self.lastPoint:
            painter.drawLine(self.firstPoint, self.lastPoint)

    def connect_line_and_button(self, button, line):
        if button.title in self.pairs_buttons_and_list.keys():
            self.pairs_buttons_and_list[button.title] = dict(self.pairs_buttons_and_list[str(button.title)], **{str(self.j): line})
        else:
            self.pairs_buttons_and_list[button.title] = {str(self.j): line}

    def move_line_and_button(self, button, move):
        if len(self.lines) > 0:
            title = str(button.title)
            for i in range(len(self.pairs_buttons_and_list[title])):
                line = self.pairs_buttons_and_list[title][str(i)]
                line.setP2(move + QPoint(50, 50))
                self.draw_all_lines()
                self.update()

    def updateImage(self):
        if self.firstPoint and self.lastPoint:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))

            p1 = self._line.p1()
            p2 = self._line.p2()
            points = [(p1.x(), p1.y()), (p2.x(), p2.y())]

            x_coords, y_coords = zip(*points)
            A = vstack([x_coords, ones(len(x_coords))]).T
            a, b = lstsq(A, y_coords, rcond=None)[0]
            function = lambda x, a=a, b=b: a*x + b

            self.lines[self.j] = [self._line, function]
            self.j += 1

            painter.drawLine(self._line)
            painter.end()
            self.firstPoint = self.lastPoint = None
            self.update()
        else:
            self.draw_all_lines()
            self.update()

    def reset_image(self):
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(QColor("#323232"))

    def draw_all_lines(self):
        self.reset_image()
        painter = QPainter(self.image)
        painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
        for i in self.lines.values():
            painter.drawLine(i[0])
        painter.end()
        self.j = len(self.lines)
        self.firstPoint = self.lastPoint = None
