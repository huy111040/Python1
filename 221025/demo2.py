# Lớp cha
class Animal:
    def __init__(self, tenGoi, canNang):
        self.tenGoi = tenGoi
        self.canNang = canNang

    def an(self):
        print(f"{self.tenGoi} đang ăn...")

    def diChuyen(self):
        print(f"{self.tenGoi} đang di chuyển...")


# Lớp Cat kế thừa từ Animal
class Cat(Animal):
    def __init__(self, tenGoi, canNang, mauLong, mauMat):
        super().__init__(tenGoi, canNang)  # gọi constructor lớp cha
        self.mauLong = mauLong
        self.mauMat = mauMat

    def batChuot(self):
        print(f"{self.tenGoi} đang bắt chuột!")

    def leoCay(self):
        print(f"{self.tenGoi} đang leo cây!")

    def xuat(self):
        print(f"🐱 Mèo: {self.tenGoi}, {self.canNang}kg, Lông: {self.mauLong}, Mắt: {self.mauMat}")


# Lớp Fish kế thừa từ Animal
class Fish(Animal):
    def __init__(self, tenGoi, canNang, kieuVay, loaiNuoc):
        super().__init__(tenGoi, canNang)
        self.kieuVay = kieuVay
        self.loaiNuoc = loaiNuoc

    def boi(self):
        print(f"{self.tenGoi} đang bơi trong {self.loaiNuoc}!")

    def xuat(self):
        print(f"🐟 Cá: {self.tenGoi}, {self.canNang}kg, Vảy: {self.kieuVay}, Sống trong: {self.loaiNuoc}")


# -------------------------------
# Chạy thử
if __name__ == "__main__":
    cat1 = Cat("Mèo Mun", 4.2, "đen", "vàng")
    fish1 = Fish("Cá vàng", 0.2, "tròn", "nước ngọt")

    cat1.xuat()
    cat1.an()
    cat1.batChuot()
    cat1.leoCay()
    print()

    fish1.xuat()
    fish1.an()
    fish1.boi()
