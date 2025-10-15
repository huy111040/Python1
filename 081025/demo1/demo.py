f = open("input.txt", "r")
data = f.read().split(",")
print(data)
if len(data) == 0:
    print("khong co du lieu")
else:
    result = sum(map(int, data))
    print(f"ket qua: {result}")
    f.close()
    f = open("output.txt", "w")
    f.write(f"ket qua: {result}")
    f.close()
