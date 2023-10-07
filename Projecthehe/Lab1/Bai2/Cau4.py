
import math
def laSoChinhPhuong(x):
	s = int(math.sqrt(x))
	return s*s == x
def laSoFibo(n):
	return laSoChinhPhuong(5*n*n + 4) or laSoChinhPhuong(5*n*n - 4)

n = int(input("Nhập n: "))
check = laSoFibo(n)
if check== True:
	print(f"{n} là số fibonacci")
else:
	print(f"{n} không là số fibonacci")

