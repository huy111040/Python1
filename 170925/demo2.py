s = "i love python"

s_list = s.split()
print(s_list)

try:
    i = s_list.index("love")
    s_list[i] = ("like")
    print("ket qua: " + str(s_list))
except:
    print("khong tim thay tu love")
