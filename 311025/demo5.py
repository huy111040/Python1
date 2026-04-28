class NhanVien:
    def __init__(self, ho_ten, so_nam_ct):
        self.ho_ten = ho_ten
        self.so_nam_ct = so_nam_ct

    @property
    def phu_cap(self):
        return 100 + self.so_nam_ct * 20

    def tinh_luong(self):
        return 0  # phương thức trừu tượng (ghi đè ở lớp con)

    def thu_nhap(self):
        return self.tinh_luong() + self.phu_cap

    def __str__(self):
        return f"Họ tên: {self.ho_ten}, Năm CT: {self.so_nam_ct}, Phụ cấp: {self.phu_cap}"


# --- Nhân viên sản xuất ---
class NVSX(NhanVien):
    def __init__(self, ho_ten, so_nam_ct, so_sp):
        super().__init__(ho_ten, so_nam_ct)
        self.so_sp = so_sp

    def tinh_luong(self):
        return self.so_sp * 10

    def __str__(self):
        return f"[Sản xuất] {super().__str__()}, Số SP: {self.so_sp}, Lương: {self.tinh_luong()}"


# --- Nhân viên văn phòng ---
class NVVP(NhanVien):
    def __init__(self, ho_ten, so_nam_ct, muc_luong, so_ngay_nghi):
        super().__init__(ho_ten, so_nam_ct)
        self.muc_luong = muc_luong
        self.so_ngay_nghi = so_ngay_nghi

    def tinh_luong(self):
        return self.muc_luong - self.so_ngay_nghi * 10

    def __str__(self):
        return f"[Văn phòng] {super().__str__()}, Mức lương: {self.muc_luong}, Ngày nghỉ: {self.so_ngay_nghi}, Lương: {self.tinh_luong()}"


# --- MENU CHÍNH ---
def doc_danh_sach():
    ds = []
    print("Nhập danh sách nhân viên (nhập trống để dừng):")
    while True:
        loai = input("Loại NV (SX/VP, trống để dừng): ").strip().upper()
        if loai == "":
            break
        ho_ten = input("Họ tên: ")
        so_nam = int(input("Số năm công tác: "))
        if loai == "SX":
            so_sp = int(input("Số sản phẩm: "))
            ds.append(NVSX(ho_ten, so_nam, so_sp))
        elif loai == "VP":
            muc_luong = float(input("Mức lương: "))
            so_ngay_nghi = int(input("Số ngày nghỉ: "))
            ds.append(NVVP(ho_ten, so_nam, muc_luong, so_ngay_nghi))
    return ds


def tong_thu_nhap(ds):
    tong = sum(nv.thu_nhap() for nv in ds)
    print(f"Tổng tiền công ty sẽ trả: {tong}")


def luu_nv_tren_7_nam(ds):
    with open("nhanvien.txt", "w", encoding="utf-8") as f:
        for nv in ds:
            if nv.so_nam_ct > 7:
                f.write(str(nv) + "\n")
    print("Đã lưu nhân viên có >7 năm công tác vào nhanvien.txt")


def xuat_thong_tin(ds):
    for nv in ds:
        print(nv)
        print("-" * 60)


# --- CHẠY MENU ---
def main():
    ds = []
    while True:
        print("\n=== MENU QUẢN LÝ NHÂN VIÊN ===")
        print("1. Nhập danh sách nhân viên")
        print("2. Tính tổng tiền công ty phải trả")
        print("3. Lưu nhân viên có >7 năm công tác")
        print("4. Xuất danh sách nhân viên")
        print("5. Thoát")

        chon = input("Chọn: ")
        if chon == "1":
            ds = doc_danh_sach()
        elif chon == "2":
            tong_thu_nhap(ds)
        elif chon == "3":
            luu_nv_tren_7_nam(ds)
        elif chon == "4":
            xuat_thong_tin(ds)
        elif chon == "5":
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
