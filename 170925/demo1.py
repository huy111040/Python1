s = input("nhập chuỗi: ")
s_list = list(s);
c = s_list.pop(len(s) // 2)
print("ký tự đã xoá: ", c)

m = min(s_list)
s_list.remove(m)
print("ký tự nhỏ nhất đã xoá: ", m)
print("chuỗi hiện tại: " + str(s_list))
try:
    i = s_list.index('a')
except:
    # pass
    print("khong có gia tri muốn tìm")
print("ket thuc chương trình")
