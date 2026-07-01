# ==========================================================
# home.py
# ----------------------------------------------------------
# Trang chủ (Home). Trang này gồm:
#   - 3 tab: Món Thái, Món Hàn Quốc, Món Việt Nam
#   - Mỗi tab là 1 danh sách cuộn (scroll) chứa các thẻ món ăn
#
# File này cũng chứa:
#   1) class MonAn        -> "khuôn" mô tả 1 món ăn (lập trình OOP)
#   2) DANH_SACH_MON_AN   -> danh sách các món ăn mẫu
# ==========================================================

from PyQt6.QtWidgets import QMainWindow, QGridLayout
from PyQt6 import uic

from pages.search import SreachPage
from pages.account import AccountPage
from pages.component import FoodCard   # thẻ món ăn đã tách riêng


# ==========================================================
# 1) CLASS MÔ TẢ 1 MÓN ĂN (OOP)
# ----------------------------------------------------------
# Thay vì dùng dictionary rời rạc, ta gói mọi thông tin của
# 1 món ăn vào 1 đối tượng (object). Cách này gọn và dễ dùng:
#   mon.ten, mon.loai, mon.do_kho ...
# ==========================================================
class MonAn:
    def __init__(self, ten, loai, do_kho, thoi_gian, hinh_anh):
        self.ten = ten            # Tên món, ví dụ: "Tom Yum"
        self.loai = loai          # Loại: "Hàn", "Thái" hoặc "Việt"
        self.do_kho = do_kho      # Độ khó: "Dễ", "Trung bình", "Khó"
        self.thoi_gian = thoi_gian  # Thời gian nấu (phút), ví dụ: 30
        self.hinh_anh = hinh_anh  # Đường dẫn ảnh, ví dụ "/accets/imgs/img_1.jpg"


# ==========================================================
# 2) DANH SÁCH MÓN ĂN MẪU
# ----------------------------------------------------------
# Mỗi loại (Thái / Hàn / Việt) có 5 món.
# Ảnh dùng lại 3 file có sẵn trong thư mục accets/imgs
# (img_1.jpg, img_2.jpg, img_3.jpg).
#
# Lưu ý: thư mục ảnh trong dự án tên là "accets" (không phải
# "assets"), nên đường dẫn ở đây viết theo đúng tên thư mục
# thật để ảnh hiển thị được.
# ==========================================================
DANH_SACH_MON_AN = [
    # ----- 5 MÓN THÁI -----
    MonAn("Tom Yum (canh chua cay)", "Thái", "Trung bình", 40, "/accets/imgs/img_1.jpg"),
    MonAn("Pad Thai (mì xào Thái)",  "Thái", "Dễ",         25, "/accets/imgs/img_2.jpg"),
    MonAn("Cà ri xanh Thái",         "Thái", "Khó",        50, "/accets/imgs/img_3.jpg"),
    MonAn("Xôi xoài Thái",           "Thái", "Dễ",         20, "/accets/imgs/img_1.jpg"),
    MonAn("Gỏi đu đủ Som Tum",       "Thái", "Trung bình", 30, "/accets/imgs/img_2.jpg"),

    # ----- 5 MÓN HÀN QUỐC -----
    MonAn("Kimchi (cải muối)",       "Hàn", "Trung bình", 60, "/accets/imgs/img_3.jpg"),
    MonAn("Tteokbokki (bánh gạo cay)", "Hàn", "Dễ",       30, "/accets/imgs/img_1.jpg"),
    MonAn("Bibimbap (cơm trộn)",     "Hàn", "Trung bình", 35, "/accets/imgs/img_2.jpg"),
    MonAn("Gà rán Hàn Quốc",         "Hàn", "Khó",        45, "/accets/imgs/img_3.jpg"),
    MonAn("Canh kimchi",             "Hàn", "Dễ",         25, "/accets/imgs/img_1.jpg"),

    # ----- 5 MÓN VIỆT NAM -----
    MonAn("Phở bò",                  "Việt", "Khó",        90, "/accets/imgs/img_2.jpg"),
    MonAn("Bún chả",                 "Việt", "Trung bình", 40, "/accets/imgs/img_3.jpg"),
    MonAn("Gỏi cuốn",                "Việt", "Dễ",         20, "/accets/imgs/img_1.jpg"),
    MonAn("Cơm tấm sườn",            "Việt", "Trung bình", 35, "/accets/imgs/img_2.jpg"),
    MonAn("Bánh xèo",                "Việt", "Trung bình", 45, "/accets/imgs/img_3.jpg"),
]


# ==========================================================
# 3) TRANG HOME
# ==========================================================
class HomePage(QMainWindow):

    def __init__(self, main_window, root_dir, cur_acc):
        super().__init__()

        self.main_window = main_window
        self.root_dir = root_dir
        self.cur_acc = cur_acc      # tài khoản đang đăng nhập

        # Nạp giao diện trang Home
        ui_path = self.root_dir + "/ui/home.ui"
        uic.loadUi(ui_path, self)

        # --- Gắn sự kiện cho các nút ở thanh bên trái ---
        self.pushButton_2.clicked.connect(self.open_search)     # Search
        self.pushButton_3.clicked.connect(self.open_favourite)  # Favourite
        self.pushButton_5.clicked.connect(self.open_account)    # Account

        # --- Đổ các thẻ món ăn vào từng tab ---
        # Mỗi tab có 1 widget danh sách riêng (đặt tên trong home.ui):
        #   thailan_list   -> tab Món Thái
        #   hanquoc_list_2 -> tab Món Hàn Quốc
        #   vietnam_list   -> tab Món Việt Nam
        # Ta lọc danh sách theo loại rồi vẽ card vào đúng tab.
        self.__do_card_vao_list(self.thailan_list,   "Thái")
        self.__do_card_vao_list(self.hanquoc_list_2, "Hàn")
        self.__do_card_vao_list(self.vietnam_list,   "Việt")

        self.show()

    # ------------------------------------------------------
    # Hàm dùng chung để đổ card vào 1 danh sách của 1 tab
    # ------------------------------------------------------
    def __do_card_vao_list(self, list_widget, loai):
        """
        list_widget : widget chứa danh sách (vd: self.thailan_list)
        loai        : chỉ lấy các món có loai này ("Thái"/"Hàn"/"Việt")
        """

        # Lọc ra những món đúng loại cần hiển thị
        cac_mon = [m for m in DANH_SACH_MON_AN if m.loai == loai]

        # Tạo 1 layout dạng LƯỚI (grid) để xếp card thành hàng và cột
        grid = QGridLayout(list_widget)
        grid.setSpacing(15)   # khoảng cách giữa các card

        SO_COT = 3   # mỗi hàng đặt 3 card

        # Duyệt từng món, tính vị trí (hàng, cột) rồi thêm card vào grid
        for i, mon in enumerate(cac_mon):
            hang = i // SO_COT   # phép chia lấy phần nguyên -> số hàng
            cot = i % SO_COT     # phép chia lấy phần dư -> số cột

            card = FoodCard(mon, self.root_dir)   # tạo 1 thẻ món ăn
            grid.addWidget(card, hang, cot)       # đặt vào ô (hang, cot)

    # ------------------------------------------------------
    # Các hàm chuyển trang
    # ------------------------------------------------------
    def open_search(self):
        # Chuyển sang trang Search, truyền kèm danh sách món + tài khoản
        self.search = SreachPage(
            self.main_window,
            self.root_dir,
            self.cur_acc,
            DANH_SACH_MON_AN
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
