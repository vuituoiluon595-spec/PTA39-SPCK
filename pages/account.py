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

        # --- Hiển thị thông tin tài khoản đang đăng nhập ---
        # cur_acc là 1 dictionary, ví dụ:
        #   {"fullname": "Hai Nam", "email": "abc@gmail.com", ...}
        # .get(key, "") nghĩa là: lấy giá trị theo key,
        # nếu không có thì trả về chuỗi rỗng "" (tránh bị lỗi).
        self.fullname.setText("Tên: " + self.cur_acc.get("fullname", ""))
        # Phần info chỉ hiển thị email (sẽ nâng cấp thêm sau)
        self.info.setText("Email: " + self.cur_acc.get("email", ""))

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
        from pages.home import DANH_SACH_MON_AN   # lấy danh sách món ăn

        self.search = SreachPage(
            self.main_window,
            self.root_dir,
            self.cur_acc,
            DANH_SACH_MON_AN
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