#Viết chương trình cho nhập vào 1 số nguyên dương có 2 chữ số, xuất ra tổng 2 chữ số của số đó
def TinhTong(num:int):
    num1 = num // 10 # chia lấy phần nguyên
    num2 = num % 10 # chia lấy phần dư

    kq = num1+num2
    return kq
while True:
    num = int(input("Nhập vào 1 số bất kỳ: "))
    kq = TinhTong(num)
    if(num >= 10 and num < 99):
        print(f"Tổng các chữ số của số {num} là {kq}") 
        break
    else:
        print ("Nhập lại!")

'''kq = TinhTong(num)
if num < 10:
    print("Vui lòng nhập lại số trong khoảng 10 - 99")
    num = int(input("Nhập vào 1 số bất kỳ: "))
elif num > 99:    
    print("Vui lòng nhập lại số trong khoảng 10 - 99")
    num = int(input("Nhập vào 1 số bất kỳ: "))
else:
    print(f"Tổng các chữ số của số {num} là {kq}")  ''' 