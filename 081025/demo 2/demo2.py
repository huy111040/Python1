with open("input.txt", "r") as f:
    lines = f.readlines()

results = []

for line in lines:
    line = line.strip()
    if not line:
        continue  # bỏ qua dòng trống
    money, months = map(float, line.split())

    if months == 3:
        rate = 0.5 / 100
    elif months == 6:
        rate = 0.8 / 100
    elif months >= 12:
        rate = 1.2 / 100
    else:
        rate = 0

    interest = money * rate * (months / 12)

    results.append(f"Tiền {int(money)} gửi {int(months)} tháng có lãi là {int(interest)} đồng\n")

with open("output.txt", "w", encoding="utf-8") as f:
    f.writelines(results)
print(results)
print(" Đã tính xong! Kết quả được ghi vào file output.txt")
