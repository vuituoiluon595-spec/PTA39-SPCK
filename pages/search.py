from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class SreachPage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        ui_path = self.root_dir + "/ui/sreach.ui"
        uic.loadUi(ui_path, self)

        # Khi nhấn Home
        self.pushButton.clicked.connect(self.open_home)

        self.show()

    def open_home(self):
        from pages.home import HomePage

        self.home = HomePage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )

        self.close()