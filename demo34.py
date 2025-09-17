s = input("Nhập các số, cách nhau bởi dấu phẩy: ")
numbers = [int(i) for i in s.split(",")]
tong = sum(numbers)

print("Tổng =", tong)
