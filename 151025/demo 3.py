class HanhKhach:
    def __init__(self, name="", sdt="", cmnd="", tien_ve=0.0):
        self.name = name
        self.sdt = sdt
        self.cmnd = cmnd
        self.tien_ve = tien_ve

    def xuat(self):
        print(f"Họ tên: {self.name}, SĐT: {self.sdt}, CMND: {self.cmnd}, Tiền vé: {self.tien_ve}")

ds = []
def nhap_danh_sach():
    n = int(input("Nhập số lượng hành khách: "))
    for _ in range(n):
        name = input("Họ tên: ")
        sdt = input("SĐT: ")
        cmnd = input("CMND: ")
        tien_ve = float(input("Tiền vé: "))
        ds.append(HanhKhach(name, sdt, cmnd, tien_ve))
    return ds


def hien_thi(ds):
    if len(ds) == 0:
        print("Danh sách hành khách rỗng.")
        return
    for hk in ds:
        hk.xuat()


def tim_kiem(ds):
    key = input("Nhập SĐT hoặc CMND cần tìm: ")
    found = False
    for hk in ds:
        if hk.sdt == key or hk.cmnd == key:
            hk.xuat()
            found = True
    if not found:
        print("Không tìm thấy hành khách.")


def sap_xep(ds):
    pass


def menu():
    while True:
        print("1. Nhập và tạo danh sách hành khách")
        print("2. Hiển thị thông tin tất cả hành khách")
        print("3. Tìm hành khách theo SĐT hoặc CMND")
        print("4. Sắp xếp danh sách hành khách theo tiền vé giảm dần")
        print("0. Thoát")
        chon = input("Chọn chức năng: ")
        if chon == "1":
            ds = nhap_danh_sach()
        elif chon == "2":
            hien_thi(ds)
        elif chon == "3":
            tim_kiem(ds)
        elif chon == "4":
            sap_xep(ds)
        elif chon == "0":
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    menu()