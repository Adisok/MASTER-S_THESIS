import sys

from GUI.drawer import Drawer
from GUI.file_operations import FileOperations
from GUI.grouped_pistons import GroupedPistons
from PyQt5.QtWidgets import *


# Define title of app
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
        self.menubar = QMenuBar()   # Defining toolbarmenu object
        self.buttons_on_schemat = []
        self.graphWidget = None # REMOVE IT!!
        self.plot_itself = None # REMOVE IT!!

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

        label1 = QLabel("Dane")
        label2 = QLabel("Wyniki")

        """  Creating main layout """
        # Creating Horizontal Layout for DATA
        hbox1 = QVBoxLayout()
        hbox1.addWidget(label1)
        hbox1.addWidget(self.textEditor1)
        hbox1.addStretch(1)
        hbox1.setSpacing(10)

        # Creating Horizontal Layout for RESULTS
        hbox2 = QVBoxLayout()
        hbox2.addWidget(label2)
        hbox2.addWidget(self.textEditor2)
        hbox2.addStretch(1)
        hbox2.setSpacing(10)

        # Creating Vertical Layout for PLOT
        process_table_widget = QTableWidget()
        process_table_widget.setRowCount(4)
        process_table_widget.setColumnCount(2)

        # Creating Schemas_Tab
        self.schemat_tab = QWidget()
        self.schemat_tab.layout = QHBoxLayout()


        self.schemat_widget = Drawer()
        self.schemat_widget.setLayout(QHBoxLayout())
        self.schemat_widget.setStyleSheet("background-color: #323232;")

        self.pistons_widget_scroll = QScrollArea()
        self.pistons_widget = GroupedPistons()
        self.pistons_widget.wynik.get_values.connect(self.return_value)

        self.pistons_widget_scroll.setWidget(self.pistons_widget)
        self.pistons_widget_scroll.setWidgetResizable(True)

        self.schemat_tab.layout.addWidget(self.pistons_widget_scroll, 2)
        self.schemat_tab.layout.addWidget(self.schemat_widget, 4)
        self.schemat_tab.setLayout(self.schemat_tab.layout)

        # Creating Data_Tab
        self.data_tab = QWidget()
        self.data_tab.layout = QHBoxLayout(self)

        tab1_insidelayout = QVBoxLayout(self)
        tab1_insidelayout.addLayout(hbox1)
        tab1_insidelayout.addLayout(hbox2)
        tab1_insidelayout.addStretch(1)
        tab1_insidelayout.setSpacing(20)

        self.data_tab.layout.addLayout(tab1_insidelayout)
        self.data_tab.layout.addWidget(process_table_widget)
        self.data_tab.setLayout(self.data_tab.layout)

        # Creating Tabs Layout
        tabs = QTabWidget()
        tabs.addTab(self.schemat_tab, "Schemat")
        tabs.addTab(self.data_tab, "Dane")

        # Creating MAIN Vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.menubar)
        vbox.addWidget(tabs)
        self.setLayout(vbox)

    def return_value(self):
        self.pistons_widget.wynik.values = self.schemat_widget.return_values()


    def stripMenu(self):
        """  Creating strip menu """
        s_menu1 = self.menubar.addMenu("Plik")        # Adding toolbar option1
        s_menu2 = self.menubar.addMenu("Eksportuj")   # Adding toolbar option2
        new_act1 = QAction("Otw??rz", self)            # Creating first option
        new_act2 = QAction("Zapisz", self)            # Creating second option
        new_act3 = QAction("Zamknij", self)           # Creating third option

        s_menu1.addAction(new_act1)
        new_act1.triggered.connect(
            lambda x=self.textEditor1, y=self.graphWidget, z=self.plot_itself:
            self.file_managing.get_file(textEditor=x, graphWidget=y, plot_itself=z)
        )
        new_act1.setShortcut("Ctrl+O")

        s_menu1.addAction(new_act2)
        new_act2.triggered.connect(
            lambda x=self.textEditor1, y=self:
            self.file_managing.save_file(textEditor=x, widget=y)
        )
        new_act2.setShortcut("Ctrl+S")

        s_menu1.addAction(new_act3)
        new_act3.triggered.connect(
            lambda x=app, y=self:
            self.file_managing.exit_file(app=x, widget=y)
        )
        new_act3.setShortcut("Ctrl+E")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SiMts()
    window.show()
    sys.exit(app.exec_())
