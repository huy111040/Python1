import re

pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

email = input("Nhập email: ")

if re.match(pattern, email):
    print("Email hợp lệ")
else:
    print("Email không hợp lệ")