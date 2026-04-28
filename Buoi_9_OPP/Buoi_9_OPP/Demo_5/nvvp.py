from nhanvien import NhanVien

class NVVP(NhanVien):
    def __init__(self, ho_ten="", so_nam_cong_tac=0, muc_luong=0, so_ngay_nghi=0.0):
        super().__init__(ho_ten, so_nam_cong_tac)
        self.muc_luong = muc_luong
        self.so_ngay_nghi = so_ngay_nghi

    def luong(self):
        return self.muc_luong - self.so_ngay_nghi * 10

    def __str__(self):
        return super().__str__() + f", ML: {self.muc_luong}, Số NN: {self.so_ngay_nghi}"
