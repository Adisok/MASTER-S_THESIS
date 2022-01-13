from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QPushButton

from rules import Rules


class RuleChecker(QPushButton):
    get_values = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("WYNIK")
        self.values = None


    def mousePressEvent(self, e) :
        print("CHECKING")
        self.get_values.emit()
        print(self.values)
        self.check_for_rules(values=self.values)

    def check_for_rules(self, values):
        rozwiazanie = []
        for i in range(1, 21):
            if Rules[i](values["Y"], values["fp"], values["fk"]):
                rozwiazanie.append(Rules[i].__name__)
        self.setText(f"{values}\n{rozwiazanie[0]}")