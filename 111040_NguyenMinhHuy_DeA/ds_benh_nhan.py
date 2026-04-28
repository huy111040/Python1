from benh_nhan_noi_tru import BNNoiTru
from benh_nhan_ngoai_tru import BNNgoaiTru

ds = []


def load_ds():
    filename = "input.txt"
    f = open(filename,encoding="utf-8")

    date = f.readlines()

    for row in date:
        row_data = row.split(",")
        if row_data[0].upper() == "I":
            bn_noi_tru = BNNoiTru(row_data[1], row_data[2], int(row_data[3]), int(row_data[4]), int(row_data[5]))
            ds.append(bn_noi_tru)
        else:
            bn_ngoai_tru = BNNgoaiTru(row_data[1], row_data[2], int(row_data[3]), int(row_data[4]), int(row_data[5]))
            ds.append(bn_ngoai_tru)
    else:
        print(f"Đã load xong dữ liệu. Có {len(ds)} bệnh nhân trong danh sách.")

    f.close()

def them_benh_nhan():
    filename = "input.txt"
    f = open(filename, encoding="utf-8",mode="a")
    chon = input("Chọn loại bệnh nhân Nội trú (1) ,Ngoại trú (2) hay bỏ qua (Enter): ")
    ma = input("Nhập mã bệnh nhân: ")
    ho_ten = input("Nhập họ tên bệnh nhân: ")
    tien_thuoc = int(input("Nhập tiền thuốc: "))
    if chon == "1":
        phi_ngay = int(input("Nhập phí ngày: "))
        so_ngay_nam_vien = int(input("Nhập số ngày nằm viện: "))

        ds.append(BNNoiTru(ma, ho_ten, tien_thuoc, phi_ngay, so_ngay_nam_vien))
        f.write(f"\nI,{ma},{ho_ten},{tien_thuoc},{phi_ngay},{so_ngay_nam_vien}")
        print("Đã thêm bệnh nhân nội trú.")
    elif chon == "2":
        phi_kham = int(input("Nhập phí khám: "))
        phi_xet_nghiem = int(input("Nhập phí xét nghiệm: "))

        ds.append(BNNgoaiTru(ma, ho_ten, tien_thuoc, phi_kham, phi_xet_nghiem))
        f.write(f"\nO,{ma},{ho_ten},{tien_thuoc},{phi_kham},{phi_xet_nghiem}")
        print("Đã thêm bệnh nhân ngoại trú.")
    else:
        print("Bỏ qua thêm bệnh nhân.")

    f.close()


def in_ds():
    print("----- DANH SÁCH BỆNH NHÂN -----")
    for bn in ds:
        print(bn)


def tim_ghi():
    filename = "out_dsbnnt.txt "
    f = open(filename,"w",encoding="utf-8")

    for bn in ds:
        if bn.vien_phi() >= 3000 :
            f.write(bn.__str__() + "\n")


def im_ma():
    ma = input("nhap ma benh nhan can tim: ")
    for bn in ds:
        if bn.ma.__contains__(ma):

            print("Tim thay benh nhan: ")
            print(bn)
            return




def sap_xep_ma():
    ds.sort(key=lambda x: x.ma)
    print("Đã sắp xếp danh sách theo mã bệnh nhân.")
    in_ds()


def menu():
    while True:
        print("----- MENU ------")
        print("1. Load danh sách bệnh nhân từ file")
        print("2. Thêm bệnh nhân mới")
        print("3. In danh sách bệnh nhân")
        print("4. Ghi BN nội trú có viện phí >= 3000 ra file")
        print("5. Tìm bệnh nhân theo mã")
        print("6. Sắp xếp danh sách theo mã")
        print("7. Thoát")
        print("----------------")
        
        chon = input("Chọn chức năng (1-7): ")
        if chon == '1':
            load_ds()
        elif chon == '2':
            them_benh_nhan()
        elif chon == '3':
            in_ds()
        elif chon == '4':
            tim_ghi()
        elif chon == '5':
           im_ma()
        elif chon == '6':
            sap_xep_ma()
        elif chon == '7':
            print("Bye!")
            break
        else:
            print("Chọn sai ồi. Vui lòng chọn lại.")


if __name__ == '__main__':
    menu()