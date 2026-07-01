from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from pages.search import SreachPage
from pages.account import AccountPage


class HomePage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        ui_path = self.root_dir + "/ui/home.ui"
        uic.loadUi(ui_path, self)

        # Search
        self.pushButton_2.clicked.connect(self.open_search)

        # Favourite
        self.pushButton_3.clicked.connect(self.open_favourite)

        # Account
        self.pushButton_5.clicked.connect(self.open_account)

        self.show()

    def open_search(self):
        self.search = SreachPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()

    def open_favourite(self):
        from pages.deatails import DetailsPage

        self.details = DetailsPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()

    def open_account(self):
        self.account = AccountPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()