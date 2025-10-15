class SinhVien:
    def __init__(self, ho_ten="", diem=0.0):
        self.ho_ten = ho_ten
        self.diem = diem

    def nhap(self):
        self.ho_ten = input("Nhập họ tên: ")
        while True:
            try:
                self.diem = float(input("Nhập điểm: "))
                if 0 <= self.diem <= 10:
                    break
                else:
                   print("Nhap diem tu 1 den 10")
               
            except :
                print("Vui lòng nhập số hợp lệ cho điểm.")
                continue

    def xuat(self):
        print(f"Họ tên: {self.ho_ten}, Điểm: {self.diem}")

    def tinh_xep_loai(self):
        if self.diem < 5.0:
            return "Yếu"
        elif self.diem < 7.0:
            return "Trung bình"
        elif self.diem < 8.0:
            return "Khá"
        elif self.diem < 9.0:
            return "Giỏi"


if __name__ == "__main__":
    sv1 = SinhVien()
    sv2 = SinhVien("Bình", 6.5)
    sv2.xuat()
    sv1.nhap()
    sv1.xuat()
