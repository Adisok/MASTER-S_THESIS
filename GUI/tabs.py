from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QTabWidget, QWidget, QHBoxLayout, QScrollArea, QTextEdit

from GUI.drawer import Drawer
from GUI.grouped_pistons import GroupedPistons

ALGORYTHM_TAM_INDEX = 1

class TabWidget(QDialog):
    update_algorytm = pyqtSignal(QTabWidget)

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Tab Widget Application')

        # if the target widget of the layout is provided as an init argument, the
        # layout will be automatically set to it
        vbox = QVBoxLayout(self)

        tabwidget = QTabWidget()
        vbox.addWidget(tabwidget)

        # Creating Schemas_Tab
        self.schemat_tab = QWidget()
        self.schemat_tab.layout = QHBoxLayout()

        self.schemat_widget = Drawer()
        self.schemat_widget.setLayout(QHBoxLayout())
        self.schemat_widget.setStyleSheet("background-color: white;")
        # 323232;")

        self.pistons_widget_scroll = QScrollArea()
        self.pistons_widget = GroupedPistons()
        self.pistons_widget.wynik.get_values.connect(self.return_value)

        self.pistons_widget_scroll.setWidget(self.pistons_widget)
        self.pistons_widget_scroll.setWidgetResizable(True)

        self.schemat_tab.layout.addWidget(self.pistons_widget_scroll, 2)
        self.schemat_tab.layout.addWidget(self.schemat_widget, 4)
        self.schemat_tab.setLayout(self.schemat_tab.layout)

        # Creating algoythm tab layout
        self.algorythm_tab = QTextEdit()
        self.algorythm_tab.layout = QHBoxLayout()

        tabwidget.addTab(self.schemat_tab, "Schemat")
        tabwidget.addTab(self.algorythm_tab, "Algorytm")

        tabwidget.tabBarClicked.connect(lambda: self.update_algorytm.emit(self))

    def return_value(self):
        self.pistons_widget.wynik.values = self.schemat_widget.return_values()


