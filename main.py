from PyQt5.QtWidgets import QApplication
from main_window import Ui_Dialog

if __name__ == '__main__':
    app = QApplication([])
    window = Ui_Dialog()
    window.show()
    app.exec_()
