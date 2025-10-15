mang = []  # khai báo biến toàn cục ban đầu


def tinh_tong_le():
    tong = sum(x for x in mang if x % 2 != 0)
    print("Tổng các phần tử lẻ:", tong)


def tinh_tong_index_chan():
    tong = sum(mang[i] for i in range(0, len(mang), 2))
    print("Tổng các phần tử ở vị trí chẵn:", tong)


def xoa_so_am():
    global mang
    mang = [x for x in mang if x >= 0]
    print("Mảng sau khi xoá số âm:", mang)


def thay_the_so_am():
    global mang
    mang = [0 if x < 0 else x for x in mang]
    print("Mảng sau khi thay số âm bằng 0:", mang)


def tim_max():
    if not mang:
        print("Mảng rỗng!")
    else:
        m = max(mang)
        vi_tri = [i for i, v in enumerate(mang) if v == m]
        print("Giá trị lớn nhất trong mảng:", m)
        print("Vị trí:", vi_tri)


def in_mang():
    print("Mảng hiện tại:", mang)


def nhap_du_lieu():
    global mang
    mang = []
    print("Nhập dữ liệu cho mảng (Enter để kết thúc):")
    while True:
        x = input("Nhập giá trị: ")
        if x == "":
            break
        try:
            mang.append(int(x))
        except ValueError:
            print("Vui lòng nhập số nguyên!")


def menu():
    while True:
        print(" MENU ")
        print("1. Tính tổng các phần tử là số lẻ trong mảng")
        print("2. Tổng các phần tử vị trí chẵn")
        print("3. Xoá các phần tử là số âm có trong mảng")
        print("4. Thay thế các phần tử âm có trong mảng bằng giá trị 0")
        print("5. Tìm vị trí của số lớn nhất trong mảng")
        print("6. In các số có trong mảng")
        print("7. Nhập dữ liệu cho mảng")
        print("0. Thoát")

        chon = input("Chọn chức năng (0-7): ")
        if chon == '1':
            tinh_tong_le()
        elif chon == '2':
            tinh_tong_index_chan()
        elif chon == '3':
            xoa_so_am()
        elif chon == '4':
            thay_the_so_am()
        elif chon == '5':
            tim_max()
        elif chon == '6':
            in_mang()
        elif chon == '7':
            nhap_du_lieu()
        elif chon == '0':
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ!")


menu()
