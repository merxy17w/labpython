n = int(input("Nhap so luong ma so sinh vien ban muon them vao danh sach: "))

mang = []
for i in range(n):
    maSo = int(input('Ma so: '))
    mang.append(maSo)
print(f"Danh sach ma so sinh vien sau khi nhap la: {mang}")

def remove_trung(n):
    mang = []
    seen = set()
    for i in n:
        if i not in seen:
            mang.append(i)
            seen.add(i)
    return mang

n = int(input("Nhap so luong ma so sinh vien ban muon them vao danh sach: "))
chuoi = []
for i in range(n):
    maSo = int(input('Ma so: '))
    chuoi.append(maSo)
print(chuoi)
chuoi1 = remove_trung(chuoi)
print(chuoi1)

def tachTen(ten):
    dsten = ten.split(" ")
    return dsten[0], dsten[1]

mangTen = []
n = input('Nhap ten vao mang: ')
mangTen.append(n)
print(f"danh sach ten chua tach: {mangTen}")
mangTen = tachTen(n)
print(f"danh sach ten da tach: {mangTen}")


ten =  input("Nhap ten: ")
tam = ten.split(" ")
