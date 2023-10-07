#3. Xuất tất cả các số nguyên tố trong 1 khoảng cho trước
# hướng giải: Nhập vào 2 số a, b, sao cho a nhỏ hơn b, in ra tất cả các số nguyên tố trong khoảng
# số nguyên tố khi và chỉ khi chia hết cho 1 và chính nó, số nguyên tố nhỏ nhất là số 2
import math
def KiemTraSoNguyenTo (num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True 
def LietKeSoNguyenTo(a,b):
    for i in range(a,b+1):
        if(KiemTraSoNguyenTo(i)):
            print(i, end=' ')

while True:
        a = int(input("Nhập vào số a: "))
        b = int(input("Nhập vào số b: "))
        
        if a < 0 or b <0:
            print("Vui lòng nhập số lớn hơn 0!")
        elif a > b:
            print("Số thứ nhất lớn hơn số thứ hai!")
        else:
            LietKeSoNguyenTo(a,b)
            break


