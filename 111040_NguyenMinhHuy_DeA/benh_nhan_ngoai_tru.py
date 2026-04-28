from benh_nhan import BenhNhan

class BNNgoaiTru(BenhNhan):
    def __init__(self, ma="", ho_ten="", tien_thuoc=0, phi_kham=0, phi_xet_nghiem=0):
        super().__init__(ma, ho_ten, tien_thuoc)
        self.__phi_kham = phi_kham
        self.__phi_xet_nghiem = phi_xet_nghiem

    def get_phi_kham(self):
        return self.__phi_kham

    def set_phi_kham(self, new_value):
        self.__phi_kham = new_value

    phi_kham = property(get_phi_kham, set_phi_kham)

    def get_phi_xet_nghiem(self):
        return self.__phi_xet_nghiem

    def set_phi_xet_nghiem(self, new_value):
        self.__phi_xet_nghiem = new_value

    phi_xet_nghiem = property(get_phi_xet_nghiem, set_phi_xet_nghiem)

    def vien_phi(self):
        return self.tien_thuoc + self.phi_kham + self.phi_xet_nghiem

    def __str__(self):
        return f"{super().__str__()}, Phi kham: {self.phi_kham}, Phi xet nghiem: {self.phi_xet_nghiem}"
