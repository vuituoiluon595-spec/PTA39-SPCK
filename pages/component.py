# ==========================================================
# component.py
# ----------------------------------------------------------
# File này chứa class FoodCard - đây là "thẻ món ăn" (card).
# Mỗi món ăn trên trang Home sẽ được vẽ ra bằng 1 FoodCard.
#
# Ý tưởng (rất giống lắp ghép LEGO):
#   - Ta đã thiết kế sẵn hình dạng của 1 card trong file
#     ui/component1.ui (có ảnh, tên món, loại, thời gian, độ khó).
#   - Ở đây ta tạo 1 class để "nạp" file .ui đó vào,
#     rồi điền dữ liệu của từng món ăn cụ thể lên.
# ==========================================================

from PyQt6.QtWidgets import QWidget      # QWidget = 1 khung giao diện cơ bản
from PyQt6.QtGui import QPixmap          # QPixmap = dùng để hiển thị ảnh
from PyQt6 import uic                    # uic = công cụ nạp file .ui vào code
import os


class FoodCard(QWidget):
    """
    FoodCard là 1 thẻ hiển thị thông tin của MỘT món ăn.

    Vì FoodCard kế thừa (extends) QWidget nên bản thân nó
    chính là 1 mảnh giao diện, có thể đem gắn (add) vào bất kỳ
    layout nào (ví dụ: lưới grid trong trang Home).
    """

    def __init__(self, mon_an, root_dir, parent=None):
        # Gọi __init__ của lớp cha (QWidget) để khởi tạo phần khung
        super().__init__(parent)

        # Lưu lại dữ liệu để dùng ở các hàm khác trong class
        self.mon_an = mon_an        # 1 đối tượng MonAn (xem home.py)
        self.root_dir = root_dir    # đường dẫn gốc của dự án

        # ----- Nạp giao diện đã thiết kế sẵn (component1.ui) -----
        # os.path.join giúp ghép đường dẫn đúng trên mọi hệ điều hành
        ui_path = os.path.join(self.root_dir, "ui", "component1.ui")
        uic.loadUi(ui_path, self)
        # Sau dòng trên, các widget trong .ui trở thành thuộc tính của self:
        #   self.label   -> ô hiển thị ẢNH món ăn
        #   self.label_2 -> LOẠI món (hàn / thái / việt)
        #   self.label_3 -> TÊN món
        #   self.label_4 -> THỜI GIAN nấu
        #   self.label_5 -> ĐỘ KHÓ

        # Điền dữ liệu thật của món ăn lên các label
        self.__hien_thi_du_lieu()

    # __ ở đầu tên hàm nghĩa là hàm "riêng tư" (private),
    # chỉ dùng bên trong class này.
    def __hien_thi_du_lieu(self):
        """Đổ thông tin của self.mon_an lên các ô giao diện."""

        # 1) ẢNH món ăn
        # mon_an.hinh_anh có dạng "/accets/imgs/img_1.jpg"
        # Ghép với root_dir để ra đường dẫn đầy đủ tới file ảnh.
        duong_dan_anh = self.root_dir + self.mon_an.hinh_anh
        anh = QPixmap(duong_dan_anh)     # đọc file ảnh
        self.label.setPixmap(anh)        # gắn ảnh vào ô label
        self.label.setScaledContents(True)  # cho ảnh co giãn vừa khung

        # 2) LOẠI món, TÊN món
        self.label_2.setText(self.mon_an.loai)
        self.label_3.setText(self.mon_an.ten)

        # 3) THỜI GIAN nấu, ví dụ 30 -> "30 phút"
        self.label_4.setText(str(self.mon_an.thoi_gian) + " phút")

        # 4) ĐỘ KHÓ (dễ / trung bình / khó)
        self.label_5.setText(self.mon_an.do_kho)
