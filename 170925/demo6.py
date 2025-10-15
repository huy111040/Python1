s = " xin chaoaca ban65 aw2g52"

tam = ""
ket_qua = []
for i in s:
    if i.isdigit():
        tam += i
    else:
        if len(tam) > 0:
            ket_qua.append(tam)
            tam = ""
    if len(tam) > 0:
        ket_qua.append(tam)
    print("ketqua: ", str(ket_qua))
