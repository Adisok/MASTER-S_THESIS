from PyQt5.QtWidgets import QWidget, QVBoxLayout

from GUI.custom_buttons import Button


class GroupedPistons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setLayout(QVBoxLayout())
        self.add_buttons()

    def add_buttons(self):
        self.test_buttons = []
        for i in range(10):
            self.test_buttons.append(Button(f'{i}'))
            self.layout().addWidget(self.test_buttons[i])

    def add_removed_button(self, button_title):
        return self.layout().addWidget(self.test_button.append(Button(int(button_title))))