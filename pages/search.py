# ==========================================================
# search.py
# ----------------------------------------------------------
# Trang Tìm kiếm món ăn.
# Người dùng gõ chữ vào ô Search -> chương trình lọc ra
# những món có tên chứa chữ đó và hiển thị bằng các thẻ FoodCard.
#
# Trang này nhận thêm 2 dữ liệu quan trọng:
#   - data    : danh sách tất cả món ăn (từ home.py truyền sang)
#   - cur_acc : tài khoản đang đăng nhập
# ==========================================================

from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6 import uic

from pages.component import FoodCard   # thẻ món ăn dùng chung


class SreachPage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc, data=None):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc

        # Nếu không được truyền danh sách món, mặc định là list rỗng
        # (tránh lỗi khi data = None)
        self.data = data if data is not None else []

        # Nạp giao diện trang Search (dựa trên file search.ui)
        ui_path = self.root_dir + "/ui/search.ui"
        uic.loadUi(ui_path, self)

        # --- Gắn sự kiện cho các nút ở thanh bên trái ---
        self.pushButton.clicked.connect(self.open_home)        # Home
        self.pushButton_3.clicked.connect(self.open_favourite) # Favourite
        self.pushButton_5.clicked.connect(self.open_account)   # Account

        # --- Bắt sự kiện khi người dùng gõ vào ô tìm kiếm ---
        # Mỗi lần nội dung ô search thay đổi -> gọi lại hàm lọc.
        self.search_input.textChanged.connect(self.__loc_va_hien_thi)

        # Ban đầu (chưa gõ gì) -> hiển thị toàn bộ món ăn
        self.__hien_thi_cac_mon(self.data)

        self.show()

    # ------------------------------------------------------
    # Lọc món ăn theo chữ người dùng gõ
    # ------------------------------------------------------
    def __loc_va_hien_thi(self):
        # Lấy chữ trong ô search, .lower() để không phân biệt hoa/thường
        tu_khoa = self.search_input.toPlainText().strip().lower()

        if tu_khoa == "":
            # Ô tìm kiếm trống -> hiện tất cả
            ket_qua = self.data
        else:
            # Giữ lại những món có TÊN chứa từ khóa
            ket_qua = [m for m in self.data if tu_khoa in m.ten.lower()]

        self.__hien_thi_cac_mon(ket_qua)

    # ------------------------------------------------------
    # Vẽ danh sách món ăn ra vùng kết quả (dạng lưới)
    # ------------------------------------------------------
    def __hien_thi_cac_mon(self, danh_sach):
        # result_list là widget chứa kết quả (khai báo trong search.ui)

        # Bước 1: XÓA các card cũ (nếu có) để vẽ lại từ đầu.
        # Nếu result_list đã có layout thì ta gỡ hết widget bên trong ra.
        layout_cu = self.result_list.layout()
        if layout_cu is not None:
            while layout_cu.count() > 0:
                item = layout_cu.takeAt(0)
                if item.widget() is not None:
                    item.widget().deleteLater()
            grid = layout_cu
        else:
            # Chưa có layout -> tạo mới 1 layout lưới (grid)
            grid = QGridLayout(self.result_list)
            grid.setSpacing(15)

        # Bước 2: Thêm từng card vào lưới, mỗi hàng 3 card
        SO_COT = 3
        for i, mon in enumerate(danh_sach):
            hang = i // SO_COT   # số hàng
            cot = i % SO_COT     # số cột
            card = FoodCard(mon, self.root_dir)
            grid.addWidget(card, hang, cot)

    # ------------------------------------------------------
    # Các hàm chuyển trang
    # ------------------------------------------------------
    def open_home(self):
        from pages.home import HomePage

        self.home = HomePage(
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
        from pages.account import AccountPage

        self.account = AccountPage(
            self.main_window,
            self.root_dir,
            self.cur_acc
        )
        self.close()
