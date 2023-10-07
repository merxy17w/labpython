#viết chương trình nhập vào 2 số và so sánh 2 số đó
def SoSanh(num1:float, num2:float):
    if num1>num2:
        return "Lớn hơn"
    elif num1 < num2:
        return "Nhỏ hơn"
    else:
        return "Bằng"

num1 = float(input("Nhập số thứ nhất: "))
num2 = float(input("Nhập số thứ 2: "))
check= SoSanh(num1, num2)
print(f"Số {num1} {check} số {num2}")
    

