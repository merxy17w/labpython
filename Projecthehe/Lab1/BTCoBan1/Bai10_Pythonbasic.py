#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
#Sample value of n is 5
#Expected Result : 615
def TinhToan(num:int):
    num1 = int( "%s" % num )
    num2 = int( "%s%s" % (num,num) )
    num3 = int( "%s%s%s" % (num,num,num) )
    kq = (num1+num2+num3)
    return kq
    
num = int(input("Nhập vào 1 số: "))
kq = TinhToan(num)
print(f"Kết quả là: {kq}")