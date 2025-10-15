def nhap(thongbao="Nhập số: "):
    while True:
        try:
            so = float(input(thongbao))
            return so
        except:
            print("\033[31mHãy nhập số\033[0m")


def tinh_tong():
    try:
        so_1 = nhap("Nhập số thứ nhất: ")
        so_2 = nhap("Nhập số thứ hai: ")
        print(f"Tổng hai số {so_1} + {so_2} =", (so_1 + so_2))

    except:
        print("\033[31mCó lỗi trong quá trình tính toán\033[0m")


def tinh_hieu():
    try:
        so_1 = nhap("Nhập số thứ nhất: ")
        so_2 = nhap("Nhập số thứ hai: ")
        print(f"Hiệu hai số {so_1} - {so_2} = ", (so_1 - so_2))

    except:
        print("\033[31mCó lỗi trong quá trình tính toán\033[0m")


def tinh_tich():
    try:
        so_1 = nhap("Nhập số thứ nhất: ")
        so_2 = nhap("Nhập số thứ hai: ")
        print(f"Tích của hai số {so_1} * {so_2} =", (so_1 * so_2))

    except:
        print("\033[31mCó lỗi trong quá trình tính toán\033[0m")


def tinh_thuong():
    try:
        so_1 = nhap("Nhập số thứ nhất: ")
        so_2 = nhap("Nhập số thứ hai: ")
        if so_2 == 0:
            print("Không thể chia cho 0")
        else:
            print(f"Thương của hai số {so_1} / {so_2} = %0.2f" % (so_1 / so_2))

    except:
        print("\033[31mCó lỗi trong quá trình tính toán\033[0m")


def tinh_luy_thua():
    try:
        so_1 = nhap("Nhập số thứ nhất: ")
        so_2 = nhap("Nhập số thứ hai: ")
        print(f"{so_1} mũ {so_2} = %0.2f" % (so_1 ** so_2))

    except:
        print("\033[31mCó lỗi trong quá trình tính toán\033[0m")


def menu():
    while True:
        print("1. Tính tổng")
        print("2. Tính hiệu")
        print("3. Tính tích")
        print("4. Tính thương")
        print("5. Tính luỹ thừa")
        print("6. Thoát")

        chon = input("Mời bạn chọn: ")
        if chon == "1":
            tinh_tong()
        elif chon == "2":
            tinh_hieu()
        elif chon == "3":
            tinh_tich()
        elif chon == "4":
            tinh_thuong()
        elif chon == "5":
            tinh_luy_thua()
        elif chon == "6":
            print("Thoát chương trình")
            quit()
        else:
            print("Bạn chọn sai, mời chọn lại")



if __name__ == "__main__":
    menu()
