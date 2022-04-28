import sys

from GUI.drawer import Drawer
from GUI.file_operations import FileOperations
from GUI.grouped_pistons import GroupedPistons
from PyQt5.QtWidgets import (
    QApplication,
    QAction,
    QWidget,
    QTabWidget,
    QTextEdit,
    QMenuBar,
    QLabel,
    QHBoxLayout,
    QScrollArea,
    QVBoxLayout,
    QTableWidget,
)


# Define title of app
from GUI.tabs import TabWidget
from math_maker import RuleChecker

TITLE = "PneuSim"

# Define size of window
LEFT = 200
TOP = 200
WIDTH = 1024
HEIGHT = 200


class SiMts(QWidget):
    def __init__(self):
        super().__init__()
        self.file_managing = FileOperations()
        self.first_point = None
        self.textEditor1 = QTextEdit()  # Defining data TextBox
        self.textEditor2 = QTextEdit()  # Defining results TextBox
        self.menubar = QMenuBar()  # Defining toolbarmenu object
        self.buttons_on_schemat = []
        self.graphWidget = None  # REMOVE IT!!
        self.plot_itself = None  # REMOVE IT!!

        self.stripMenu()  # Creating Strip Menu
        self.doLayout()  # Creating Layout

    def doLayout(self):
        self.setMouseTracking(True)
        """  Defining Layout parameters """
        # Setting Window Title, and geometry
        self.setWindowTitle(TITLE)
        self.setAcceptDrops(True)
        self.setGeometry(LEFT, TOP, WIDTH, HEIGHT)

        #### Creating widgets ####
        # Data TextBox
        self.textEditor1.setFixedSize(250, 250)
        self.textEditor1.setReadOnly(True)

        # Results TextBox
        self.textEditor2.setFixedSize(250, 250)
        self.textEditor2.setReadOnly(True)

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

        # Creating tab
        self.tabs = TabWidget()
        self.tabs.update_algorytm.connect(self.update_algorytm_tab)

        # Creating MAIN Vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.menubar)
        vbox.addWidget(self.tabs)
        self.setLayout(vbox)

    def return_value(self):
        self.pistons_widget.wynik.values = self.schemat_widget.return_values()

    def update_algorytm_tab(self):
        print("ELO", self.schemat_widget.return_values())
        self.tabs.algorythm_tab.setText(" ".join(self.schemat_widget.return_values()))


    def stripMenu(self):
        """Creating strip menu"""
        s_menu1 = self.menubar.addMenu("Plik")  # Adding toolbar option1
        s_menu2 = self.menubar.addMenu("Eksportuj")  # Adding toolbar option2
        new_act1 = QAction("Otwórz", self)  # Creating first option
        new_act2 = QAction("Zapisz", self)  # Creating second option
        new_act3 = QAction("Zamknij", self)  # Creating third option

        s_menu1.addAction(new_act1)
        new_act1.triggered.connect(
            lambda x=self.textEditor1, y=self.graphWidget, z=self.plot_itself: self.file_managing.get_file(
                textEditor=x, graphWidget=y, plot_itself=z
            )
        )
        new_act1.setShortcut("Ctrl+O")

        s_menu1.addAction(new_act2)
        new_act2.triggered.connect(
            lambda x=self.textEditor1, y=self: self.file_managing.save_file(
                textEditor=x, widget=y
            )
        )
        new_act2.setShortcut("Ctrl+S")

        s_menu1.addAction(new_act3)
        new_act3.triggered.connect(
            lambda x=app, y=self: self.file_managing.exit_file(app=x, widget=y)
        )
        new_act3.setShortcut("Ctrl+E")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SiMts()
    window.show()
    sys.exit(app.exec_())
