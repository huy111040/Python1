from abc import ABC, abstractmethod

class NhanVien(ABC):
    def __init__(self, ho_ten="", so_nam_cong_tac=0):
        self.ho_ten = ho_ten
        self.so_nam_cong_tac = so_nam_cong_tac

    @property
    def phu_cap(self):
        return 100 + self.so_nam_cong_tac * 20

    @abstractmethod
    def luong(self):
        pass

    def __str__(self):
        return f"HT: {self.ho_ten}, SNCT: {self.so_nam_cong_tac}, PC: {self.phu_cap}, Luong: {self.luong()}"
