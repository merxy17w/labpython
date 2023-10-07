#4. Write a Python program that calculates the area of a circle based on the radius entered by the user.
import math
def TinhDienTich(banKinh:float):
    # if banKinh>0:
    #     dienTich = 2*banKinh*3.14
    #     return dienTich
    return (2*banKinh*3.14) if banKinh > 0 else (" ")
    
while True:
    banKinh=(float(input("Nhập vào bán kính: ")))
    
    if banKinh >0:
        kq = TinhDienTich(banKinh)
        print(f"Diện tích của hình tròn có bán kính {banKinh} là {kq}")
        break
    else:
        print("Vui lòng nhập lại bán kính: ")
        