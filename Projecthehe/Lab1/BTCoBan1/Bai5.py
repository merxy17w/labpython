#Viết chương trình cho người dùng nhập vào 1 số nguyên và xuất ra màn hình thông báo số đó là số chẵn hay là số lẻ
def KiemTraTinhChanLe(num:int):
    if num % 2 == 0:
        return "số chẵn"
    else:
        return "số lẻ"
num = int(input("Nhập vào 1 số bất kỳ: ")) 
check = KiemTraTinhChanLe(num)
print(f"Số {num} là số {check}")