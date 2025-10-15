def nhap(thongbao="Nhập số: "):
    while True:
        try:
            so = float(input(thongbao))
            return so
        except:
            print("\033[31mHãy nhập số hợp lệ!\033[0m")

def tinh_tich(lst):
    tich = 1
    for x in lst:
        tich *= x
    return tich

def main():
    ds = []
    n = int(input("Nhập số lượng phần tử: "))
    for i in range(n):
        so = nhap(f"Nhập số thứ {i+1}: ")
        ds.append(so)

    print("Danh sách vừa nhập:", ds)
    print("Tích các giá trị trong list là:", tinh_tich(ds))

# Chạy chương trình
main()
