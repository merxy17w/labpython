#1. Tính:
#a) (a + b),
#b) a/b,
#c) a^b
def TinhTongHaiSo(num1:float, num2:float):
    kq = num1 + num2
    return kq
def TinhThuongHaiSo(num1:float, num2:float):
    kq = (float)(num1 / num2)
    return kq
def TinhBinhPhuongHaiSo(num1:float, num2:float):
    kq = num1**num2
    return kq

num1 = float(input("Nhập vào số thứ nhất: "))
num2 = float(input("Nhập vào số thứ hai: "))
KetQuaTong = TinhTongHaiSo(num1, num2)
KetQuaThuong = TinhThuongHaiSo(num1, num2)
KetQuaBinhPhuong = TinhBinhPhuongHaiSo(num1, num2)
print(f"Tổng của số {num1} và {num2} là {KetQuaTong}")
print(f"Thương của số {num1} và {num2} là {KetQuaThuong}")
print(f"Bình phương của số {num1} và {num2} là {KetQuaBinhPhuong}")
