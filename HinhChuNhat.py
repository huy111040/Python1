dai = int(input("Nhập chiều dài: "))
rong = int(input("Nhập chiều rộng: "))

print("Hình chữ nhật:")
for i in range(rong):
    print("* " * dai)

print("Hình chữ nhật rỗng:")
for i in range(rong):
    if i == 0 or i == rong - 1:
        print("* " * dai)
    else:
        print("* " + "  " * (dai - 2) + "*")
