from abc import ABC, abstractmethod

class BacSi(ABC):
    def __init__(self, ma=0, ho_ten="", muc_luong=0):
        self.__ma = ma
        self.__ho_ten = ho_ten
        self.__muc_luong = muc_luong

    @property
    def get_ma(self):
        return self.__ma
 
    @property
    def ho_ten(self):
        return self.__ho_ten

    @property
    def muc_luong(self):
        return self.__muc_luong

    @abstractmethod
    def luong_hang_thang(self):
        pass


class BacSiToanTG(BacSi):
    pass

class BacSiBanTG(BacSi):
    pass

if __name__ == '__main__':
    list_bac_si =[]

    bsttg = BacSiToanTG("NV01","Nguyễn Văn A", 5000000,2000000,150000)
    bsbtg = BacSiBanTG("NV02","Nguyễn Thi C",15, 455000,90000,26)

    list_bac_si.append(bsbtg)
    list_bac_si.append(bsttg)

    for bs in list_bac_si:
        print(bs)