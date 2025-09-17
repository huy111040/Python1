n = input("Nhập số nguyên n (0<=n<=1000): ")
s_encoded = 'ABCDEFGHKL'

s_decoded = ""
for i in n:
    s_decoded += s_encoded[int(i)]

print("Mã hoá:", s_decoded)



