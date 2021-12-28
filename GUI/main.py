import sys

from GUI.file_operations import FileOperations
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class SiMts(QWidget):

    def __init__(self):
        super().__init__()
        self.file_managing = FileOperations()

        # Definie size of window
        self.left = 200
        self.top = 200
        self.title = "nazwa robocza"
        self.width = 1024
        self.height = 200

        self.data = [[0], [0]]
        self.plot_itself = None
        self.graphWidget = None

        self.textEditor1 = QTextEdit()  # Defining data TextBox
        self.textEditor2 = QTextEdit()  # Defining results TextBox
        self.menubar = QMenuBar(self)   # Defining toolbarmenu object
        self.tab1 = QWidget()           # Defining tab for data,results and plot
        self.tab2 = QWidget()           # Defining tab for schematic

        self.stripMenu()  # Creating Strip Menu

        self.doLayout()  # Creating Layout

    def doLayout(self):
        """  Defining Layout parameters """
        # Setting Window Title, and geometry
        self.setAcceptDrops(True)
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Creating widgets
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

        # Creating Tabs Layous
        tabs = QTabWidget()
        tabs.addTab(self.tab1, "Dane")
        tabs.addTab(self.tab2, "Schemat")

        self.tab1.layout = QHBoxLayout(self)

        tab1_insidelayout = QVBoxLayout(self)
        tab1_insidelayout.addLayout(hbox1)
        tab1_insidelayout.addLayout(hbox2)
        tab1_insidelayout.addStretch(1)
        tab1_insidelayout.setSpacing(20)
        self.tab1.layout.addLayout(tab1_insidelayout)
        self.tab1.layout.addWidget(process_table_widget)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QHBoxLayout(self)


        list_widget = QListWidget()
        list_widget.setAcceptDrops(True)
        list_widget.setDragEnabled(True)
        list_widget.setSpacing(20)

        icon_list = QListWidget()
        icon2 = QPixmap("test1.jpg")

        icon_widget = QLabel()
        icon_widget1 = QLabel()


        #icon_widget.setPixmap(icon)
        icon_widget1.setPixmap(icon2)

        #icon_widget.setGeometry(200, 200, 200, 200)
        # icon_widget.setAcceptDrops(True)
        # icon_widget.setDragEnabled(True)
        # icon_widget.setViewMode(QListWidget.IconMode)

        #icon_list.addItem(QListWidgetItem(icon_widget))
        #icon_list.addItem(icon_widget1)
        self.tab2.layout.addWidget(icon_widget, 2)
        self.tab2.layout.addWidget(list_widget, 4)

        self.tab2.setLayout(self.tab2.layout)

        # Creating MAIN Vertical layout
        vbox = QVBoxLayout()

        vbox.addWidget(self.menubar)
        vbox.addWidget(tabs)

        self.setLayout(vbox)

    def stripMenu(self):
        """  Creating strip menu """
        s_menu1 = self.menubar.addMenu("Plik")        # Adding toolbar option1
        s_menu2 = self.menubar.addMenu("Eksportuj")     # Adding toolbar option2
        new_act1 = QAction("Otwórz", self)            # Creating first option
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

    def schematic(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = SiMts()
    window.show()
    sys.exit(app.exec_())
