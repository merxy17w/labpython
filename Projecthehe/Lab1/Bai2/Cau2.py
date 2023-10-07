#2. Tính diện tích hình chữ nhật khi biết bán kính
def TinhDienTichHinhChuNhat (a:float, b:float):
    kq = a *b
    return kq
while True:
    a = float(input("Nhập vào chiều dài hình chữ nhật: "))
    b = float(input("Nhập vào chiều rộng hình chữ nhật: "))
    
    if a >0 and b > 0:
        kq = TinhDienTichHinhChuNhat(a, b)
        print(f"Diện tích của hình chữ nhật có chiều dài {a} và chiều rộng {b} là {kq}")
        break
    else:
        print('Chiều dài và chiều rộng không hợp lệ, mời nhập lại!')
