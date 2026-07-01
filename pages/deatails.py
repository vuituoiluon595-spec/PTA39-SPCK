from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic

from pages.search import SreachPage
from pages.account import AccountPage


class DetailsPage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        ui_path = self.root_dir + "/ui/Favourite.ui"
        uic.loadUi(ui_path, self)

        # Home
        self.pushButton.clicked.connect(self.open_home)

        # Search
        self.pushButton_2.clicked.connect(self.open_search)

        # Account
        self.pushButton_5.clicked.connect(self.open_account)

        self.show()

    def open_home(self):
        from pages.home import HomePage

        self.home = HomePage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()

    def open_search(self):
        from pages.home import DANH_SACH_MON_AN   # lấy danh sách món ăn

        self.search = SreachPage(
            self.main_window,
            self.root_dir,
            self.cur_acc,
            DANH_SACH_MON_AN
        )
        self.close()

    def open_account(self):
        self.account = AccountPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()