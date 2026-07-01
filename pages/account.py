from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class AccountPage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        # Load giao diện
        ui_path = self.root_dir + "/ui/account.ui"
        uic.loadUi(ui_path, self)

        # Home
        self.pushButton.clicked.connect(self.open_home)

        # Search
        self.pushButton_2.clicked.connect(self.open_search)

        # Favourite
        self.pushButton_3.clicked.connect(self.open_favourite)

        # Account (đang ở màn này nên không cần chuyển)
        # self.pushButton_5

        self.show()

    # ==========================
    # Home
    # ==========================
    def open_home(self):
        from pages.home import HomePage

        self.home = HomePage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()

    # ==========================
    # Search
    # ==========================
    def open_search(self):
        from pages.search import SreachPage

        self.search = SreachPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()

    # ==========================
    # Favourite
    # ==========================
    def open_favourite(self):
        from pages.deatails import DetailsPage

        self.details = DetailsPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()