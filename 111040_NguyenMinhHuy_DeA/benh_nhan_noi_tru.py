from benh_nhan import BenhNhan

class BNNoiTru(BenhNhan):
    def __init__(self, ma="", ho_ten="", tien_thuoc=0, phi_ngay=0, so_ngay_nam_vien=0):
        super().__init__(ma, ho_ten, tien_thuoc)
        self.__phi_ngay = phi_ngay
        self.__so_ngay_nam_vien = so_ngay_nam_vien

    def get_phi_ngay(self):
        return self.__phi_ngay

    def set_phi_ngay(self, new_value):
        self.__phi_ngay = new_value

    phi_ngay = property(get_phi_ngay, set_phi_ngay)

    def get_so_ngay_nam_vien(self):
        return self.__so_ngay_nam_vien

    def set_so_ngay_nam_vien(self, new_value):
        self.__so_ngay_nam_vien = new_value

    so_ngay_nam_vien = property(get_so_ngay_nam_vien, set_so_ngay_nam_vien)

    def vien_phi(self):
        phu_phi = 50 if self.so_ngay_nam_vien <10 else 100
        return self.tien_thuoc * self.so_ngay_nam_vien + self.phi_ngay * self.so_ngay_nam_vien + phu_phi

    def __str__(self):
        return f"{super().__str__()}, Phi ngay: {self.phi_ngay}, So ngay nam vien: {self.so_ngay_nam_vien}"
