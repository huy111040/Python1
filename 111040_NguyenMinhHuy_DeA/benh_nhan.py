from abc import ABC, abstractmethod

class BenhNhan(ABC):
    def __init__(self, ma="",ho_ten="",tien_thuoc=0):
        self.__ma = ma
        self.__ho_ten = ho_ten
        self.__tien_thuoc = tien_thuoc

    def get_ma(self):
        return self.__ma

    def set_ma(self, new_value):
        self.__ma = new_value

    ma = property(get_ma, set_ma)

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, new_value):
        self.__ho_ten = new_value

    ho_ten = property(get_ho_ten, set_ho_ten)

    def get_tien_thuoc(self):
        return self.__tien_thuoc

    def set_tien_thuoc(self, new_value):
        self.__tien_thuoc = new_value

    tien_thuoc = property(get_tien_thuoc, set_tien_thuoc)

    @abstractmethod
    def vien_phi(self):
         pass

    def __str__(self):
        return f"Ma: {self.ma}, Ho ten: {self.ho_ten}, Tien thuoc: {self.get_tien_thuoc()}"