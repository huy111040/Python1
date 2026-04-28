from nvvp import NVVP
from nvsx import NVSX

dsnv = []

def nhap_ds(filename):
    filepath = "Buoi_9_OPP/Demo_5/" + filename

    f = open(filepath, mode="r", encoding="utf-8")

    data = f.readlines()

    for row in data:
        row_data = row.split(",")
        if row_data[1].lower() == "v":
            nvvp = NVVP(row_data[0], int(row_data[2]), int(row_data[3]), float(row_data[4]))
            dsnv.append(nvvp)
        else:
            nvsx = NVSX(row_data[0], int(row_data[2]), int(row_data[3]))
            dsnv.append(nvsx)

    f.close()

def hien_thi_ds():
    print("Danh sách nhân viên:")
    for nv in dsnv:
        print(nv)
    print(f"Có {len(dsnv)} nhân viên trong danh sách")

def tinh_tong_tien():
    tong = 0
    for nv in dsnv:
        tong += nv.luong()
    print("Tổng tiền công ty sẽ trả là:", tong)

def ghi_file(filename):
    filepath = "Buoi_9_OPP/Demo_5/" + filename

    f = open(filepath, mode="w", encoding="utf-8")

    for nv in dsnv:
        if nv.so_nam_cong_tac > 7:
            f.write(nv.__str__())
            f.write("\n")

    f.close()


def menu():
    while True:
        print("\n===== QUẢN LÝ NHÂN VIÊN =====")
        print("1.Nhập danh sách nhân viên từ file")
        print("2.Tính tổng số tiền công ty phải trả")
        print("3.Ghi nhân viên có >7 năm công tác vào file")
        print("4.Hiển thị danh sách nhân viên")
        print("0.Thoát")
        print("=============================")

        chon = input("Chọn chức năng (0-4): ")\
        
        if chon == "1":
            nhap_ds("data.txt")
        elif chon == "2":
            tinh_tong_tien()
        elif chon == "3":
            ghi_file("nhanvien.txt")
        elif chon == "4":
            hien_thi_ds()
        elif chon == "0":
            return
        else:
            print("Chức năng không hợp lệ, mời chọn lại!")


if __name__ == "__main__":
    menu()