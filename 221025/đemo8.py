class SinhVien:
    def __init__(self, idsv, ho_ten, diem):
        self.__IDSv = idsv
        self.__ho_ten = ho_ten
        self.__diem = diem
        self.__hoc_luc = self.__xep_loai()

    def get_idsv(self):
        return self.__IDSv

    def set_idsv(self, value):
        self.__IDSv = value

    IDSv = property(get_idsv, set_idsv)

    def get_ho_ten(self):
        return self.__ho_ten

    def set_ho_ten(self, value):
        self.__ho_ten = value

    ho_ten = property(get_ho_ten, set_ho_ten)


    def get_diem(self):
        return self.__diem

    def set_diem(self, value):
        self.__diem = value
        self.__hoc_luc = self.__xep_loai()

    diem = property(get_diem, set_diem)


    def get_hoc_luc(self):
        return self.__hoc_luc

    hoc_luc = property(get_hoc_luc)

    def __xep_loai(self):
        if self.__diem <= 5.0:
            return "Yếu"
        elif self.__diem <= 7.0:
            return "Trung bình"
        elif self.__diem <= 8.0:
            return "Khá"
        elif self.__diem <= 9.0:
            return "Giỏi"


    def xuat(self):
        print(f"{self.__IDSv:<10}{self.__ho_ten:<25}{self.__diem:<10}{self.__hoc_luc}")


if __name__ == "__main__":
    ds = []
    try:
        with open("inp.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue 

                parts = [p.strip() for p in line.split(",")]
                if len(parts) == 3:
                    idsv = parts[0]
                    ten = parts[1]
                    diem = float(parts[2])
                    ds.append(SinhVien(idsv, ten, diem))
    except FileNotFoundError:
        print("Không tìm thấy file inp.txt!")
        ds = []

    if ds:
        print(f"{'IDSV':<10}{'Họ tên':<25}{'Điểm':<10}{'Học lực'}")
        for sv in ds:
            if sv.hoc_luc in ["Khá", "Giỏi"]:
                sv.xuat()
    else:
        print("Không có dữ liệu sinh viên!")