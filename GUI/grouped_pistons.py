from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox
from buttons_data import data as buttons_data
from GUI.custom_buttons import Button


class GroupedPistons(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.groups = []
        self.setLayout(QVBoxLayout())
        self.group_buttons()

    def group_buttons(self):
        j=0
        for button in buttons_data:
            group = PistonGroups(button, group=j)
            self.layout().addWidget(group)
            self.groups.append(group)
            j += 1

    def add_removed_button(self, button_title):
        for group in self.groups:
            for i in group:
                if button_title == i.title:
                     return self.layout().addWidget(self.group.hlay.addWidget(Button(int(button_title))))


class PistonGroups(QGroupBox):
    def __init__(self, info, group, parent=None):
        super(PistonGroups, self).__init__(parent)
        title = info["title"]
        self.setTitle(title)
        self.hlay = QHBoxLayout(self)
        self.group_buttons = []
        for button_info in info["buttons"]:
            title = button_info["text"]
            path_icon = button_info["path_icon"]
            btn = Button(title, image_path=path_icon, group=group)
            self.group_buttons.append(btn)
            self.hlay.addWidget(btn)
        self.hlay.setContentsMargins(5, 5, 5, 5)
        self.setFixedSize(self.sizeHint())
