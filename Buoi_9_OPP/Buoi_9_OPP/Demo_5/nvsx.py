from nhanvien import NhanVien

class NVSX(NhanVien):
    def __init__(self, ho_ten="", so_nam_cong_tac=0, so_san_pham=0):
        super().__init__(ho_ten, so_nam_cong_tac)
        self.so_san_pham = so_san_pham

    def luong(self):
        return self.so_san_pham * 10 + self.phu_cap

    def __str__(self):
        return super().__str__() + f", Số SP: {self.so_san_pham}"
