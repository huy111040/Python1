def uoc_chung_lon_nhat(a, b):
    if b == 0:
        return a
    return uoc_chung_lon_nhat(b, a % b)
