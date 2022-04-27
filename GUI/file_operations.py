import sys

from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QFileDialog, QMessageBox


class FileOperations:
    def __init__(self):
        pass

    def _get_data(self, graphWidget, plot_itself):
        """Preparing data to plot"""
        prep_datx, prep_daty = [], []

        for i in self.data.split("\n")[0]:
            prep_daty.append(int(i))
        for j in self.data.split("\n")[1]:
            prep_datx.append(int(j))

        graphWidget.setXRange(0, max(prep_datx))
        graphWidget.setYRange(0, 1)
        ay = graphWidget.getAxis("left")
        ay.setTicks([[(0, "0"), (1, "1")], []])
        plot_itself.setData(prep_datx, prep_daty)

    def get_file(self, textEditor, graphWidget, plot_itself):
        """Opening file"""
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec():
            file_name = dialog.selectedFiles()
            if file_name[0].endswith(".txt"):
                with open(file_name[0], "r") as f:
                    self.data = f.read()
                    textEditor.setPlainText(self.data)
                    f.close()
                    self._get_data(graphWidget, plot_itself)
            else:
                pass

    def save_file(self, textEditor, widget):
        """Saving file"""
        name = QFileDialog.getSaveFileName(
            widget, "Zapisz Plik", filter="Dane Textowe (*.txt)"
        )
        with open(name[0].split("/")[-1], "w") as f:
            text = textEditor.toPlainText()
            f.write(text)
            f.close()

    def exit_file(self, app, widget):
        """Closing application"""
        choice = QMessageBox.question(
            widget,
            "Koniec",
            "Ciemność, widzę ciemność, ciemność widzę",
            QMessageBox.Yes | QMessageBox.No,
        )
        if choice == QMessageBox.Yes:
            sys.exit(app.exec_())
        else:
            pass
